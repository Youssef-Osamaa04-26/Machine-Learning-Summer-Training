# ==========================================
# File: pages/1_🏠_Home.py
# Page: Home
# ==========================================

import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

st.title("🏠 Welcome to Real Estate Predictor")
st.markdown("---")

st.markdown("""
## 🎯 About the Project

This is a **Machine Learning project** that predicts real estate prices 
and classifies whether properties will be sold in the Egyptian market.

## 📊 Dataset

- **Size:** 250 properties
- **Features:** 9 columns
- **Locations:** 5 (Nasr City, Maadi, 5th Settlement, Sheikh Zayed, New Cairo)
- **Property Types:** 4 (Apartment, Villa, Duplex, Penthouse)

## 🎯 What We Did

1. **Data Cleaning & EDA** — Explored the dataset
2. **Regression Models** — 6 models for price prediction
3. **Classification Models** — 2 models for Is_Sold prediction
4. **Streamlit App** — Built this interactive interface

## 🏆 Results

| Task | Best Model | Score |
|------|------------|-------|
| Price Prediction | Linear Regression | R² = -0.033 |
| Is_Sold Classification | Gradient Boosting | **62% Accuracy** |

## 🚀 Get Started

Use the **sidebar** to navigate:
- 💰 **Price Prediction** — Get instant price estimates
- 📊 **Is_Sold Classification** — Predict if a property will be sold
- 📈 **EDA Insights** — Explore the data
- 🤖 **Models Comparison** — Compare all models
""")

st.markdown("---")
st.success("Use the sidebar to navigate!")