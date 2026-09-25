# 🏠 Real Estate ML Project

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30-red)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0-green)

## 📌 Overview

A complete **Machine Learning project** for predicting real estate prices and classifying whether properties will be sold in Greater Cairo, Egypt.

**Team Size:** 9 Members  
**Duration:** Summer Training 2026  
**Best Model:** Gradient Boosting Classifier (62% Accuracy)

---

## 🎯 Project Objectives

1. **Price Prediction (Regression)** — Predict property price based on features
2. **Sale Status Classification** — Predict if a property will be sold (Yes/No)
3. **Interactive Web App** — Build a Streamlit app for live predictions
4. **Data Analysis** — Extract insights from real estate data

---

## 📊 Dataset

| Metric | Value |
|--------|-------|
| Properties | 250 |
| Features | 9 |
| Locations | 5 |
| Property Types | 4 |
| Missing Values | 0 |
| Duplicates | 0 |

**Locations:** Nasr City, New Cairo, Maadi, Sheikh Zayed, 5th Settlement  
**Property Types:** Apartment, Villa, Duplex, Penthouse

### Data Dictionary

| Column | Type | Description |
|--------|------|-------------|
| Property_ID | Text | Unique identifier |
| Location | Categorical | Property location (5 districts) |
| Property_Type | Categorical | Apartment / Villa / Duplex / Penthouse |
| Area_SqM | Numeric | Area in square meters |
| Bedrooms | Numeric | Number of bedrooms (1-5) |
| Bathrooms | Numeric | Number of bathrooms (1-3) |
| Price_EGP | Numeric | Price in EGP (Regression Target) |
| Is_Sold | Categorical | Sold? Yes/No (Classification Target) |
| Days_On_Market | Numeric | Days listed on market |

---

## 📁 Project Structure

```
Real_Estate_ML_Project/
│
├── 1_Data/                          # Raw and cleaned data
│   ├── raw_data.csv
│   ├── cleaned_data.csv
│   └── data_dictionary.md
│
├── 2_EDA/                           # Exploratory Data Analysis
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_analysis.ipynb
│   ├── chart_1_price_by_location.png
│   ├── chart_2_property_type_pie.png
│   ├── chart_3_price_histogram.png
│   ├── chart_4_area_vs_price.png
│   ├── chart_5_correlation_heatmap.png
│   └── eda_insights.md
│
├── 3_Modeling/                      # Machine Learning Models
│   │
│   ├── 01_Regression/               # Price Prediction
│   │   ├── 01_youssef_linear_dt.ipynb
│   │   ├── 02_adel_rf_xgb.ipynb
│   │   ├── 03_farid_tuning_best.ipynb
│   │   ├── best_model.pkl
│   │   ├── scaler.pkl
│   │   ├── feature_columns.pkl
│   │   ├── model_info.pkl
│   │   ├── final_comparison.csv
│   │   └── *.png
│   │
│   └── 02_Classification/           # Sale Status Prediction
│       ├── 04_is_sold_classification.ipynb
│       ├── 05_feature_engineering.ipynb
│       ├── 06_cross_validation.ipynb
│       ├── is_sold_classifier_final.pkl
│       ├── is_sold_features_final.pkl
│       └── *.png
│
├── 4_Streamlit_App/                 # Interactive Web App
│   ├── app.py
│   ├── style.css
│   ├── requirements.txt
│   ├── assets/
│   └── pages/
│       ├── 1_🏠_Home.py
│       ├── 2_💰_Price_Prediction.py
│       ├── 3_📊_Is_Sold_Classification.py
│       ├── 4_📈_EDA_Insights.py
│       └── 5_🤖_Models_Comparison.py
│
├── 5_Presentation/                  # Slides and Report
    ├── Real_Estate_Presentation.pptx
    └── Real_Estate_ML_Report_EN (1).pdf

---

## 🤖 Models Trained

### Regression Models (Price Prediction)

| # | Model | R² | MAE | RMSE |
|---|-------|-----|-----|------|
| 1 | **Linear Regression** 🏆 | **-0.033** | 3,157,737 | 3,866,100 |
| 2 | Tuned XGBoost | -0.044 | 3,231,462 | 3,886,699 |
| 3 | Tuned Random Forest | -0.066 | 3,248,975 | 3,926,591 |
| 4 | Random Forest | -0.109 | 3,309,401 | 4,004,579 |
| 5 | XGBoost | -0.345 | 3,759,825 | 4,410,333 |
| 6 | Decision Tree | -0.475 | 3,583,859 | 4,619,457 |

### Classification Models (Sale Status Prediction)

| Version | Model | Accuracy | Notes |
|---------|-------|----------|-------|
| V1 | Random Forest | 58% | Baseline |
| V1 | XGBoost | 50% | Baseline |
| V2 | Random Forest | 56% | + Feature Engineering |
| V2 | **Gradient Boosting** 🏆 | **62%** | + Feature Engineering |
| V2 | XGBoost | 52% | + Feature Engineering |
| V3 | **Gradient Boosting (Final)** 🏆 | **62%** | + 10-Fold CV |

**Winner:** Gradient Boosting Classifier  
**Test Accuracy:** 62%  
**CV Mean:** 54.8%

---

## 📈 Key EDA Insights

1. **Average Price:** 8,470,125 EGP
2. **Price Range:** 1,566,150 — 14,997,927 EGP
3. **Most Common Type:** Apartment (50.8%)
4. **Least Common Type:** Duplex (11.6%)
5. **Highest Avg Price:** 5th Settlement (8,785,033 EGP)
6. **Lowest Avg Price:** Sheikh Zayed (7,899,658 EGP)
7. **Weak Correlation** between Area and Price (r = 0.059)
8. **No Outliers** detected using 1.5×IQR rule

---

## 🚀 Streamlit App

A **5-page interactive web app** for non-technical users.

| Page | Function |
|------|----------|
| 🏠 Home | Project overview |
| 💰 Price Prediction | Estimate property price |
| 📊 Is_Sold Classification | Predict sale probability |
| 📈 EDA Insights | View charts and insights |
| 🤖 Models Comparison | Compare all models |

### How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Navigate to app folder
cd 4_Streamlit_App

# 3. Run the app
streamlit run app.py

# 4. Open in browser
# http://localhost:8501