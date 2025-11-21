# Retail Sales Analysis Project

## Overview
This project aims to analyze and forecast retail store sales using historical sales and store metadata. 
The dataset combines daily sales records with store-level attributes such as promotions, assortment type, competition, and more.

# ⚠️ **Note:** Project is under development and will be updated daily.

---

## Day 1 – Progress
- Loaded train (daily sales) and store datasets using Python (pandas). 
- Merged datasets on `Store` ID, repeating store info for each day. 
- Converted `Date` column to datetime and checked data types. 
- Inspected missing values and visualized them using a heatmap (Seaborn). 
- Checked for duplicate rows. 
- Explored dataset shape and basic statistics. 
- Saved cleaned and merged dataset for further analysis. 

---

## Day 2 – Progress

### ✔️ Data Cleaning
- Handled missing values for: 
  `CompetitionDistance`, 
  `CompetitionOpenSinceMonth` / `CompetitionOpenSinceYear`, 
  `Promo2SinceWeek`, `Promo2SinceYear`, `PromoInterval`
- Standardized `StateHoliday` values (converted categorical → numeric).
- Ensured **0 missing values** remain in the dataset.

### ✔️ Feature Engineering
- Extracted time-based features: 
  `Year`, `Month`, `Day`, `WeekOfYear`, `DayOfYear`
- Created competition-related features: 
  `CompetitionOpenDate`, `DaysSinceCompetitionOpen`
- Created promotion feature: 
  `IsPromoMonth` (based on PromoInterval logic)
- Applied one-hot encoding for:
  `StoreType`, `Assortment`
- Final dataset ready with **29 structured ML features**.

Exported as → **`cleaned_dataset.csv`**

---

## Day 3 – Progress (Completed Today)

### Exploratory Data Analysis (EDA)
- Focused only on open stores (`Open == 1`)
- Created **7 visualizations** (saved in `/images`)
- Key findings:
  - Promotions increase sales by **39%**
  - December dominates every year (Christmas spike)
  - Store type **"b"** outperforms all others
  - Monday strongest / Sunday weakest (many stores closed)
  - Sales ↔ Customers correlation: **0.82**

Added → `day3_explanations.txt` 
Notebook → `3_eda.ipynb`

---

## Day 4 – Progress (Modeling Day)

### ✔️ Train/Test Split + Data Prep
- Removed closed-store rows 
- Fixed PromoInterval logic → improved `IsPromoMonth`
- Dropped object/date columns (`Date`, `CompetitionOpenDate`, etc.)
- Final modeling dataset: **844,392 rows × 26 features**

### 🤖 Baseline Models Built
**Linear Regression** - RMSE: **1295** - MAE: **940** - Score: **82.6%**

**HistGradientBoostingRegressor** - RMSE: **929** - Score: **91.0%**

**XGBoost (Base Model)** - RMSE: **870** - Score: **92.1%**

**XGBoost (After RandomizedSearchCV Tuning)** - Best Score: **93.6%** - Best Params: 
  - `max_depth=6` 
  - `n_estimators=200` 
  - `learning_rate=0.05` 
  - `subsample=0.7`

### 📊 Visualizations Produced
- XGBoost feature importance 
- Permutation importance 
- Actual vs Predicted (LR, HGBR, XGB) 
- Residual distribution 
- Learning curve 
- Histograms of important numeric columns 

### 🔮 First Future Prediction
Store 1 — **Aug 1, 2015 → ~2120 €** (Predicted using tuned XGBoost)

Notebook → `4_modeling.ipynb`

---

## Day 5 – Progress (Evaluation & Diagnostics)

### 🔍 Error Analysis & Robustness
- Addressed feature mismatches between Train and Test sets (Fixed `StateHoliday` & object column issues).
- Performed **Residual Analysis**: Calculated the difference between Actual and Predicted values.
- Identified that the model tracks trends well but struggles with extreme outliers/rare holidays.

### 📈 Visual Verification
- Plotted **Actual vs. Predicted Sales** for specific stores (Store 1).
- Confirmed model captures weekly seasonality and trends effectively (visual alignment).

### 🛠️ Operationalization
- Configured `.gitignore` to exclude large model files (`.pkl`, `.joblib`) and datasets.
- Explored model serialization using `joblib` for saving/loading trained models.

Notebook → `5_evaluation.ipynb` (or appended to `4_modeling.ipynb`)

---

## Next Steps (will come regularly)
- Feature engineering v2 (lags, rolling windows)
- Multi-step forecasting 
- Advanced models (LSTM, Prophet, CatBoost) 
- Compare all ML models 
- Build dashboard (Streamlit / PowerBI) 
- Deployment + final report 

---

## Tech Stack
- Python (pandas, numpy, matplotlib, seaborn, sklearn, XGBoost, joblib) 
- Jupyter Notebook 
- Git & GitHub 

---

## Dataset Credit
Dataset used: **Rossmann Store Sales** (Kaggle) 
This project is for learning and analysis purposes only.

---