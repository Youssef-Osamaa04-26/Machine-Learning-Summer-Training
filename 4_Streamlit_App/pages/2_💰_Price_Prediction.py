# ==========================================
# File: pages/2_💰_Price_Prediction.py
# Page: Price Prediction
# ==========================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(page_title="Price Prediction", page_icon="💰", layout="wide")

# ==========================================
# Load Model
# ==========================================
@st.cache_resource
def load_regression_model():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(base_path, '..', '3_Modeling', '01_Regression')
    
    model = joblib.load(os.path.join(model_path, 'best_model.pkl'))
    scaler = joblib.load(os.path.join(model_path, 'scaler.pkl'))
    feature_columns = joblib.load(os.path.join(model_path, 'feature_columns.pkl'))
    model_info = joblib.load(os.path.join(model_path, 'model_info.pkl'))
    
    return model, scaler, feature_columns, model_info

try:
    model, scaler, feature_columns, model_info = load_regression_model()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# ==========================================
# Page Content
# ==========================================
st.title("💰 Property Price Prediction")
st.markdown("### Enter property details to get an estimated price.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📍 Location & Type")
    location = st.selectbox(
        "Location",
        ['Nasr City', 'Maadi', '5th Settlement', 'Sheikh Zayed', 'New Cairo']
    )
    property_type = st.selectbox(
        "Property Type",
        ['Apartment', 'Villa', 'Duplex', 'Penthouse']
    )
    area = st.number_input("Area (SqM)", 50, 500, 200, step=10)

with col2:
    st.markdown("#### 🏠 Property Details")
    bedrooms = st.slider("Bedrooms", 1, 5, 3)
    bathrooms = st.slider("Bathrooms", 1, 3, 2)
    days = st.number_input("Days on Market", 0, 200, 60, step=5)

st.markdown("---")

if st.button("💰 Predict Price", use_container_width=True):
    input_dict = {
        'Area_SqM': area,
        'Bedrooms': bedrooms,
        'Bathrooms': bathrooms,
        'Days_On_Market': days,
    }
    
    for col in feature_columns:
        if col not in input_dict:
            if col.startswith('Location_'):
                input_dict[col] = 1 if col == f'Location_{location}' else 0
            elif col.startswith('Property_Type_'):
                input_dict[col] = 1 if col == f'Property_Type_{property_type}' else 0
            else:
                input_dict[col] = 0
    
    input_df = pd.DataFrame([input_dict])[feature_columns]
    
    if model_info['needs_scaling']:
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)[0]
    else:
        prediction = model.predict(input_df)[0]
    
    st.markdown("---")
    st.markdown(
        f'<div style="padding: 2rem; border-radius: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-align: center; font-size: 2.5rem; font-weight: bold; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">💵 {prediction:,.0f} EGP</div>',
        unsafe_allow_html=True
    )
    st.balloons()
    
    st.markdown("### 📋 Property Details")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("📍 Location", location)
        st.metric("🏢 Type", property_type)
    with c2:
        st.metric("📐 Area", f"{area} SqM")
        st.metric("🛏️ Bedrooms", bedrooms)
    with c3:
        st.metric("🚿 Bathrooms", bathrooms)
        st.metric("📅 Days", days)
    
    st.info(f"Model Used: **{model_info['model_name']}**")