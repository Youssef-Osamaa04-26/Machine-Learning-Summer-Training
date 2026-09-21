# ==========================================
# File: pages/5_🤖_Models_Comparison.py
# Page: Models Comparison
# ==========================================

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Models Comparison", page_icon="🤖", layout="wide")

st.title("🤖 Models Comparison")
st.markdown("### Compare all the ML models we built.")
st.markdown("---")

# ==========================================
# Regression Models
# ==========================================
st.markdown("## 📊 Regression Models (Price Prediction)")

reg_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                         '..', '3_Modeling', '01_Regression')

# Comparison Chart
comparison_path = os.path.join(reg_path, 'model_comparison.png')
if os.path.exists(comparison_path):
    st.image(comparison_path, use_container_width=True)
else:
    st.warning("Comparison chart not found")

# Comparison Table
csv_path = os.path.join(reg_path, 'final_comparison.csv')
if os.path.exists(csv_path):
    df_comp = pd.read_csv(csv_path)
    st.dataframe(df_comp, use_container_width=True)
else:
    st.warning("Comparison CSV not found")

st.markdown("---")

# ==========================================
# Classification Models
# ==========================================
st.markdown("## 🎯 Classification Models (Is_Sold)")

st.markdown("""
| Version | Model | Accuracy | Notes |
|---------|-------|----------|-------|
| V1 | Random Forest | 58% | Baseline |
| V1 | XGBoost | 50% | Baseline |
| V2 | Gradient Boosting | **62%** | + Feature Engineering |
| V2 | Random Forest | 56% | + Feature Engineering |
| V3 | **Gradient Boosting** | **62%** | + 10-Fold CV |
""")

# Confusion Matrix
cls_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                         '..', '3_Modeling', '02_Classification')
confusion_path = os.path.join(cls_path, 'is_sold_confusion_matrix_v3.png')
if os.path.exists(confusion_path):
    st.image(confusion_path, use_container_width=True)
else:
    st.warning("Confusion matrix not found")

st.markdown("---")

# ==========================================
# Insights
# ==========================================
st.markdown("## 💡 Key Insights")

st.markdown("""
### Regression (Price Prediction)
- **Best Model:** Linear Regression (R² = -0.033)
- **Problem:** All models have negative R²
- **Reason:** Data lacks strong correlations between features and price

### Classification (Is_Sold)
- **Best Model:** Gradient Boosting (62% Accuracy)
- **CV Mean:** 54.8%
- **Strength:** Predicts "Not Sold" correctly 83% of the time

### Overall Conclusions
1. **Classification outperforms Regression** on this dataset
2. **Feature Engineering** improved results from 58% to 62%
3. **Cross-Validation** confirmed the results
4. **Data limitation** is the main constraint
""")