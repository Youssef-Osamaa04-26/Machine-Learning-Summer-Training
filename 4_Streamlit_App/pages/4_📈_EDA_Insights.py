# ==========================================
# File: pages/4_📈_EDA_Insights.py
# Page: EDA Insights
# ==========================================

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="EDA Insights", page_icon="📈", layout="wide")

st.title("📈 EDA Insights")
st.markdown("### Explore the dataset and visualizations.")
st.markdown("---")

# Load Data
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                         '..', '1_Data', 'cleaned_data.csv')
df = pd.read_csv(data_path)

# Overview
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("🏠 Total Properties", f"{len(df)}")
with col2:
    st.metric("💰 Avg Price", f"{df['Price_EGP'].mean():,.0f}")
with col3:
    st.metric("📐 Avg Area", f"{df['Area_SqM'].mean():.0f} SqM")
with col4:
    st.metric("📅 Avg Days", f"{df['Days_On_Market'].mean():.0f}")

st.markdown("---")

# Charts
eda_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                         '..', '2_EDA')

tab1, tab2, tab3, tab4 = st.tabs([
    "📍 Price by Location", 
    "🏢 Property Types", 
    "📊 Price Distribution",
    "🔥 Correlations"
])

with tab1:
    chart_path = os.path.join(eda_path, 'chart_1_price_by_location.png')
    if os.path.exists(chart_path):
        st.image(chart_path, use_container_width=True)
    else:
        st.warning("Chart not found")

with tab2:
    chart_path = os.path.join(eda_path, 'chart_2_property_type_pie.png')
    if os.path.exists(chart_path):
        st.image(chart_path, use_container_width=True)
    else:
        st.warning("Chart not found")

with tab3:
    chart_path = os.path.join(eda_path, 'chart_3_price_histogram.png')
    if os.path.exists(chart_path):
        st.image(chart_path, use_container_width=True)
    else:
        st.warning("Chart not found")

with tab4:
    chart_path = os.path.join(eda_path, 'chart_5_correlation_heatmap.png')
    if os.path.exists(chart_path):
        st.image(chart_path, use_container_width=True)
    else:
        st.warning("Chart not found")

st.markdown("---")

# Insights
st.markdown("### 💡 Key Insights")
st.markdown("""
1. **Apartments** are the most common property type (50.8%)
2. **5th Settlement** has the highest average price (8,785,033 EGP)
3. **Sheikh Zayed** has the lowest average price (7,899,658 EGP)
4. **Area and Price** have weak correlation (0.059)
5. **Average price:** 8,470,125 EGP
6. **Price range:** 1,566,150 - 14,997,927 EGP
""")

st.markdown("---")

# Data Preview
st.markdown("### 📋 Data Preview")
st.dataframe(df.head(20), use_container_width=True)