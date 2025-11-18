# Retail Sales Analysis Project

## Overview
This project aims to analyze and forecast retail store sales using historical sales and store metadata.  
The dataset combines daily sales records with store-level attributes such as promotions, assortment type, competition, and more.

# ⚠️ **Note:** Project is under development and will be updated daily.

---

## Day 1 – Progress
- Loaded train (daily sales) and store datasets using Python (pandas).  
- Merged datasets on `Store` ID, repeating store info for each day.  
- Checked data types and converted `Date` column to datetime.  
- Inspected missing values and planned handling.  
- Visualized missing values using a heatmap (Seaborn).  
- Checked for duplicate rows and removed if any.  
- Explored dataset shapes and basic statistics.  
- Saved cleaned and merged dataset for further analysis.  

---

## Day 2 – Progress  

### ✔️ Data Cleaning  
- Handled missing values across major fields:  
  - `CompetitionDistance`  
  - `CompetitionOpenSinceMonth` / `CompetitionOpenSinceYear`  
  - `Promo2SinceWeek`, `Promo2SinceYear`, `PromoInterval`  
- Standardized `StateHoliday` values by converting categorical labels (`a`, `b`, `c`, `0`) into numeric format.  
- Ensured **0 missing values** remain in the dataset.  

### ✔️ Feature Engineering  
- Extracted time-based features from `Date`:
  - `Year`, `Month`, `Day`, `WeekOfYear`, `DayOfYear`.  
- Created competition-related features:
  - **CompetitionOpenDate**  
  - **DaysSinceCompetitionOpen**  
- Created promo-related feature:
  - **IsPromoMonth** based on store-specific promotion intervals.  
- Applied one-hot encoding to categorical fields:
  - `StoreType`  
  - `Assortment`
- Verified final dataset: **29 clean, structured, ML-ready features**.  

- Exported the cleaned dataset:  
  **`cleaned_dataset.csv`**

---



## Day 3 – Progress (Completed Today)

### Exploratory Data Analysis (EDA)
- Analyzed only open stores (`Open == 1`)  
- Created 7 clear visualizations (saved in `/images` folder)  
- Key findings:  
  - Promotions increase sales by **39%**  
  - December has the highest sales every year (Christmas peak)  
  - Store type 'b' has the best performance  
  - Monday is the strongest day, Sunday the weakest  
  - Sales and Customers are very strongly linked (correlation 0.82)  

- Added `day3_explanations.txt` – short notes for each image  
- Notebook: `3_eda.ipynb`  



## Next Steps (will come regularly)
- Perform exploratory data analysis (EDA) with visualizations.  
- Analyze sales trends based on year, month, week, and store behavior.  
- Study the impact of promotions, holidays, and competition.  
- Prepare modeling features and split dataset for training.  
- Build machine learning models for sales forecasting.  
- Evaluate and compare model performance.  
- Deploy or create a dashboard for real-time sales analysis.
- AND MANY MORE....
---

## Tech Stack
- Python (pandas, numpy, matplotlib, seaborn)  
- Jupyter Notebook  
- Git & GitHub  

---








## Dataset Credit
The datasets used in this project are from the **Rossmann Store Sales** dataset available on [Kaggle](https://www.kaggle.com/c/rossmann-store-sales).  

All credits go to the original dataset creators. This project is for learning and analysis purposes only.
