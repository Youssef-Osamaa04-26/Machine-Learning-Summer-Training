# Data Dictionary

| Column | Type | Description |
|--------|------|-------------|
| Property_ID | Text | Unique identifier for each property |
| Location | Categorical | Property location (5 areas) |
| Property_Type | Categorical | Apartment / Villa / Duplex / Penthouse |
| Area_SqM | Numeric | Area in square meters |
| Bedrooms | Numeric | Number of bedrooms (1-5) |
| Bathrooms | Numeric | Number of bathrooms (1-3) |
| Price_EGP | Numeric | Price in Egyptian Pounds |
| Is_Sold | Categorical | Yes / No |
| Days_On_Market | Numeric | Number of days on market |

## Dataset Info
- **Rows:** 250
- **Columns:** 9
- **Source:** Real Estate Company
- **Target:** Price_EGP (Regression) or Is_Sold (Classification)