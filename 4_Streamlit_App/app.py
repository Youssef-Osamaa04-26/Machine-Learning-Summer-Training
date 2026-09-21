# ==========================================
# File: app.py
# Main Entry Point
# Team: Peter + Tony
# ==========================================

import streamlit as st

# ==========================================
# Page Config
# ==========================================
st.set_page_config(
    page_title="Real Estate Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# Custom CSS
# ==========================================
def load_css():
    css = """
    <style>
        .main-header {
            font-size: 3rem;
            background: linear-gradient(90deg, #3498db, #2ecc71);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
            text-align: center;
            padding: 1rem;
        }
        .sub-header {
            font-size: 1.5rem;
            color: #34495e;
            margin: 1rem 0;
        }
        .result-box {
            padding: 2rem;
            border-radius: 10px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            font-size: 2rem;
            font-weight: bold;
            margin: 1rem 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        .stButton > button {
            background: linear-gradient(90deg, #3498db, #2ecc71);
            color: white;
            font-weight: bold;
            border-radius: 10px;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

load_css()

# ==========================================
# Main Home Page
# ==========================================
st.markdown('<h1 class="main-header">🏠 Real Estate Predictor</h1>', unsafe_allow_html=True)
st.markdown(
    '<p style="text-align: center; color: #7f8c8d; font-size: 1.2rem;">'
    'Machine Learning Project - Team of 9 Members'
    '</p>',
    unsafe_allow_html=True
)

st.markdown("---")

st.markdown("## 👋 Welcome!")
st.markdown("""
This application uses **Machine Learning** to:
- 💰 **Predict property prices** in Egypt
- 📊 **Classify whether properties will be sold**
- 📈 **Visualize data insights**
- 🤖 **Compare different ML models**

**Use the sidebar to navigate!**
""")

st.markdown("---")

# ==========================================
# Quick Stats
# ==========================================
st.markdown("## 📊 Project at a Glance")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("🏠 Properties", "250")
with col2:
    st.metric("🤖 Models", "8")
with col3:
    st.metric("💰 Best R²", "-0.033")
with col4:
    st.metric("📊 Best Accuracy", "62%")

st.markdown("---")

# ==========================================
# Team
# ==========================================
st.markdown("## 👥 Team")

st.markdown("""
| Team | Members |
|------|---------|
| **Data & EDA** | Mohamed Qorany, Yahia |
| **Modeling** | Youssef, Mohamed Adel, Farid |
| **Streamlit** | Peter, Tony |
| **Presentation** | Mohamed Abu Alaa, Omar |
""")

st.markdown("---")
st.info("👈 Use the sidebar to navigate to other pages!")

# Footer
st.markdown(
    "<div style='text-align: center; color: gray; padding: 1rem;'>"
    "🏠 Real Estate ML Project | 2026"
    "</div>",
    unsafe_allow_html=True
)