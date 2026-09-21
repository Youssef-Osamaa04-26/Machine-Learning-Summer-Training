# ==========================================
# File: pages/3_📊_Is_Sold_Classification.py
# Page: Is_Sold Classification
# ==========================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Is_Sold Classification", page_icon="📊", layout="wide")

# ==========================================
# Load Model
# ==========================================
@st.cache_resource
def load_classifier():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cls_path = os.path.join(base_path, '..', '3_Modeling', '02_Classification')
    
    classifier = joblib.load(os.path.join(cls_path, 'is_sold_classifier_final.pkl'))
    features = joblib.load(os.path.join(cls_path, 'is_sold_features_final.pkl'))
    
    return classifier, features

try:
    classifier, cls_features = load_classifier()
except Exception as e:
    st.error(f"Error loading classifier: {e}")
    st.stop()

# ==========================================
# Page Content
# ==========================================
st.title("📊 Is_Sold Classification")
st.markdown("### Predict if a property will be sold.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📍 Location & Type")
    location = st.selectbox(
        "Location",
        ['Nasr City', 'Maadi', '5th Settlement', 'Sheikh Zayed', 'New Cairo'],
        key='cls_location'
    )
    property_type = st.selectbox(
        "Property Type",
        ['Apartment', 'Villa', 'Duplex', 'Penthouse'],
        key='cls_type'
    )
    area = st.number_input("Area (SqM)", 50, 500, 200, step=10, key='cls_area')

with col2:
    st.markdown("#### 🏠 Property Details")
    bedrooms = st.slider("Bedrooms", 1, 5, 3, key='cls_bed')
    bathrooms = st.slider("Bathrooms", 1, 3, 2, key='cls_bath')
    days = st.number_input("Days on Market", 0, 200, 60, step=5, key='cls_days')
    price = st.number_input("Price (EGP)", 1000000, 15000000, 8000000, step=100000, key='cls_price')

st.markdown("---")

# ==========================================
# Predict Button
# ==========================================
if st.button("📊 Predict Sold Status", use_container_width=True):
    # Feature Engineering
    total_rooms = bedrooms + bathrooms
    area_per_bed = area / bedrooms if bedrooms > 0 else 0
    bath_ratio = bathrooms / bedrooms if bedrooms > 0 else 0
    is_luxury = 1 if (area > 300 and bedrooms >= 4) else 0
    price_per_sqm = price / area if area > 0 else 0
    is_expensive = 1 if price_per_sqm > 35000 else 0
    
    # Days category
    if days <= 30:
        days_fast, days_medium, days_slow = 1, 0, 0
    elif days <= 90:
        days_fast, days_medium, days_slow = 0, 1, 0
    else:
        days_fast, days_medium, days_slow = 0, 0, 1
    
    # Create input
    input_dict = {
        'Area_SqM': area,
        'Bedrooms': bedrooms,
        'Bathrooms': bathrooms,
        'Price_EGP': price,
        'Days_On_Market': days,
        'Total_Rooms': total_rooms,
        'Area_per_Bedroom': area_per_bed,
        'Bathroom_Ratio': bath_ratio,
        'Is_Luxury': is_luxury,
        'Price_per_SqM': price_per_sqm,
        'Is_Expensive': is_expensive,
    }
    
    for col in cls_features:
        if col not in input_dict:
            if col.startswith('Location_'):
                input_dict[col] = 1 if col == f'Location_{location}' else 0
            elif col.startswith('Property_Type_'):
                input_dict[col] = 1 if col == f'Property_Type_{property_type}' else 0
            elif col.startswith('Days_Category_'):
                if 'Fast' in col:
                    input_dict[col] = days_fast
                elif 'Medium' in col:
                    input_dict[col] = days_medium
                elif 'Slow' in col:
                    input_dict[col] = days_slow
                else:
                    input_dict[col] = 0
            else:
                input_dict[col] = 0
    
    input_df = pd.DataFrame([input_dict])[cls_features]
    
    # Predict
    prediction = classifier.predict(input_df)[0]
    proba = classifier.predict_proba(input_df)[0]
    
    # ==========================================
    # Display Result
    # ==========================================
    st.markdown("---")
    st.markdown("## 🎯 Prediction Result")
    
    if prediction == 1:
        st.markdown(
            f'<div style="padding: 2rem; border-radius: 10px; background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%); color: white; text-align: center; font-size: 2.5rem; font-weight: bold; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">✅ Property WILL BE SOLD</div>',
            unsafe_allow_html=True
        )
        st.success(f"Confidence: **{proba[1]:.2%}**")
    else:
        st.markdown(
            f'<div style="padding: 2rem; border-radius: 10px; background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); color: white; text-align: center; font-size: 2.5rem; font-weight: bold; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">❌ Property Will NOT Be Sold</div>',
            unsafe_allow_html=True
        )
        st.info(f"Confidence: **{proba[0]:.2%}**")
    
    # ==========================================
    # Metrics Row
    # ==========================================
    st.markdown("### 📊 Probability Breakdown")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(
            label="❌ Not Sold Probability",
            value=f"{proba[0]:.2%}"
        )
    with col_b:
        st.metric(
            label="✅ Sold Probability",
            value=f"{proba[1]:.2%}"
        )
    
    # ==========================================
    # Plotly Bar Chart (Better looking)
    # ==========================================
    fig = go.Figure(data=[
        go.Bar(
            x=['Not Sold', 'Sold'],
            y=[proba[0], proba[1]],
            marker_color=['#e74c3c', '#2ecc71'],
            text=[f'{proba[0]:.2%}', f'{proba[1]:.2%}'],
            textposition='outside',
            textfont=dict(size=16, color='white'),
            width=0.5
        )
    ])
    
    fig.update_layout(
        title={
            'text': 'Prediction Probability',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': 'white'}
        },
        xaxis_title="Status",
        yaxis_title="Probability",
        yaxis=dict(range=[0, 1]),
        template='plotly_dark',
        height=400,
        showlegend=False,
        font=dict(color='white')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # ==========================================
    # Gauge Chart (Alternative)
    # ==========================================
    st.markdown("### 🎯 Sold Probability Gauge")
    
    gauge_fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=proba[1] * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Probability of Being Sold (%)", 'font': {'size': 18, 'color': 'white'}},
        delta={'reference': 50},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#2ecc71"},
            'steps': [
                {'range': [0, 30], 'color': "#e74c3c"},
                {'range': [30, 70], 'color': "#f39c12"},
                {'range': [70, 100], 'color': "#2ecc71"}
            ],
            'threshold': {
                'line': {'color': "white", 'width': 4},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))
    
    gauge_fig.update_layout(
        template='plotly_dark',
        height=300,
        font=dict(color='white')
    )
    
    st.plotly_chart(gauge_fig, use_container_width=True)
    
    # ==========================================
    # Model Info
    # ==========================================
    st.info("Model Used: **Gradient Boosting Classifier (62% Accuracy)**")