# Retail Sales Analysis Project

## Overview
This project analyzes and forecasts retail store sales using historical sales data and store-level metadata.  
The dataset combines daily sales records with store attributes such as promotions, assortment type, competition, and more.  

This project demonstrates the full **ML lifecycle**: data cleaning, feature engineering, exploratory data analysis, modeling, evaluation, and deployment via a Streamlit dashboard.  

⚠️ **Note:** Project was developed as a 7-day and continues to be updated for enhancements.

---

## Project Progress

### **Day 1 – Data Loading & Initial Inspection**
- Loaded train (daily sales) and store datasets using Python (pandas).  
- Merged datasets on `Store` ID.  
- Converted `Date` column to datetime and inspected data types.  
- Checked for missing values, duplicates, and basic statistics.  
- Saved merged and cleaned dataset for further processing.

---

### **Day 2 – Data Cleaning & Feature Engineering**
- Handled missing values for:  
  `CompetitionDistance`, `CompetitionOpenSinceMonth`, `CompetitionOpenSinceYear`, `Promo2SinceWeek`, `Promo2SinceYear`, `PromoInterval`  
- Standardized `StateHoliday` (categorical → numeric)  
- Extracted time-based features: `Year`, `Month`, `Day`, `WeekOfYear`, `DayOfYear`  
- Created competition features: `CompetitionOpenDate`, `DaysSinceCompetitionOpen`  
- Created promotion feature: `IsPromoMonth`  
- One-hot encoded `StoreType` and `Assortment`  
- Final dataset: **29 ML-ready features**  

Exported as → **`cleaned_dataset.csv`**

---

### **Day 3 – Exploratory Data Analysis (EDA)**
- Focused on open stores (`Open == 1`)  
- Generated **7 visualizations** highlighting:  
  - Promotions increase sales by **~39%**  
  - December is the peak month  
  - Store type **"b"** outperforms others  
  - Weekday trends: Monday strongest, Sunday weakest  
  - Sales ↔ Customers correlation: **0.82**  
- Saved visualizations in `/images`  

Added → `day3_explanations.txt`  
Notebook → `3_eda.ipynb`

---

### **Day 4 – Modeling**
- Removed closed-store rows and fixed PromoInterval logic  
- Dropped irrelevant columns (`Date`, `CompetitionOpenDate`)  
- Training dataset: **844,392 rows × 26 features**  
- Models trained:  
  - **Linear Regression** → RMSE: 1295, MAE: 940, Score: 82.6%  
  - **HistGradientBoostingRegressor** → RMSE: 929, Score: 91.0%  
  - **XGBoost (tuned)** → RMSE: 870, Score: 93.6%  

- Visualizations produced: feature importance, residuals, learning curves, actual vs predicted  

Notebook → `4_modeling.ipynb`

---

### **Day 5 – Evaluation & Diagnostics**
- Performed error analysis and residual checks  
- Fixed feature mismatches between train and test sets  
- Visualized actual vs predicted sales for key stores  
- Configured `.gitignore` and serialized XGBoost model using `joblib`  

Notebook → `5_evaluation.ipynb`

---

### **Day 6 – Production Pipeline**
- Built a robust prediction pipeline:  
  - `preprocess()` → prepares input data  
  - `predict_sales()` → runs XGBoost predictions  
- Generated output artifacts:  
  - `results_predictions.csv` → actual vs predicted sales  
  - `metrics.csv` → RMSE, MAPE (~12%), mean error  
  - `top_best_predictions.csv` / `top_worst_predictions.csv`  
- Pipeline ensures **scalability, modularity, and real-time readiness**  

Pipeline code → `day6_pipeline.py`

---

### **Day 7 – Streamlit Dashboard**
- Created a **fully interactive dashboard** for retail sales forecasting:  
  - Upload your own CSV or use the **sample dataset (100 rows)**  
  - Run predictions with one click  
  - Visualize actual vs predicted sales, error distributions, best/worst predictions  
  - Download predictions CSV for further analysis  
- Dashboard uses **Plotly** and **Matplotlib/Seaborn** for interactive and static visualizations  

App code → `7_app.py`  
Demo & repo → [GitHub Link](https://github.com/y-india/retail-sales-analysis-project)

---

## Tech Stack
- **Python:** pandas, numpy, matplotlib, seaborn, scikit-learn, XGBoost, joblib  
- **Jupyter Notebook**  
- **Streamlit** for interactive dashboard  
- **Git & GitHub**  

---

## Dataset Credit
- **Rossmann Store Sales** (Kaggle)  
- Used for learning and analysis purposes only.  

---

## Next Steps
- Feature engineering v2 (lags, rolling windows)  
- Multi-step forecasting  
- Advanced models: LSTM, Prophet, CatBoost  
- Deployment improvements and cloud integration  

---

## Quick Start
1. Clone the repository:  
```bash
git clone https://github.com/y-india/retail-sales-analysis-project.git
```
2. Navigate to the project folder:
```bash
cd retail-sales-analysis-project
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the Streamlit app:
```bash
streamlit run 7_app.py
```
5. Use the dashboard to upload your CSV or try the included sample dataset (test_dataset_100.csv)
