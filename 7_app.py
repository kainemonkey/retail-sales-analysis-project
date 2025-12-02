import streamlit as st
import pandas as pd
import joblib
import numpy as np
from day6_pipeline import preprocess, predict_sales
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns












st.title("📊 Retail Sales Forecasting Dashboard")

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load("xgb_retail_model.pkl")

model = load_model()




















st.subheader("💡 Example: How your dataset should look")
example_data = pd.DataFrame({
    "Store": [1, 2],
    "DayOfWeek": [5, 4],
    "Customers": [500, 600],
    "Open": [1, 1],
    "Promo": [1, 0],
    "StateHoliday": [0, 'a'],
    "SchoolHoliday": [0, 0],
    "CompetitionDistance": [200, 500],
    "CompetitionOpenSinceMonth": [9, 11],
    "CompetitionOpenSinceYear": [2010, 2012],
    "Promo2": [0, 1],
    "Promo2SinceWeek": [0, 14],
    "Promo2SinceYear": [0, 2015],
    "Year": [2023, 2023],
    "Month": [1, 1],
    "Day": [1, 2],
    "WeekOfYear": [1, 1],
    "DayOfYear": [1, 2],
    "DaysSinceCompetitionOpen": [5000, 4000],
    "IsPromoMonth": [0, 1],
    "StoreType_b": [0, 1],
    "StoreType_c": [1, 0],
    "StoreType_d": [0, 0],
    "Assortment_b": [1, 0],
    "Assortment_c": [0, 1]
})

st.dataframe(example_data)











# -----------------------------
# Dataset selection
# -----------------------------
use_sample = st.checkbox("Use Sample Dataset (100 rows)", value=True)
uploaded_file = st.file_uploader("Or upload your CSV file", type="csv")

if use_sample:
    data = pd.read_csv("test_dataset_100.csv")
elif uploaded_file:
    data = pd.read_csv(uploaded_file)
else:
    st.info("Upload a CSV file or select sample dataset to continue.")
    data = None

























# -----------------------------
# Run Predictions
# -----------------------------
if data is not None:
    st.write("✅ Dataset Preview:")
    st.dataframe(data.head())

    if st.button("Run Predictions"):
        # Drop columns not expected during prediction
        X = data.drop(columns=['Sales', 'Date'], errors='ignore')

        # Ensure all expected features exist
        expected_features = [
            'Store','DayOfWeek','Customers','Open','Promo','StateHoliday','SchoolHoliday',
            'CompetitionDistance','CompetitionOpenSinceMonth','CompetitionOpenSinceYear',
            'Promo2','Promo2SinceWeek','Promo2SinceYear','Year','Month','Day','WeekOfYear',
            'DayOfYear','DaysSinceCompetitionOpen','IsPromoMonth','StoreType_b','StoreType_c',
            'StoreType_d','Assortment_b','Assortment_c'
        ]
        for col in expected_features:
            if col not in X.columns:
                X[col] = 0


        # Reorder to match model
        X = X[expected_features]


        X = preprocess(X)
        preds = predict_sales(X)

        # Prepare results
        results = data.copy()
        results["Predicted_Sales"] = preds
        results["Error"] = results.get("Sales", 0) - preds
        results["Abs_Error"] = results["Error"].abs()

        # Metrics
        rmse = np.sqrt((results["Error"] ** 2).mean())
        mape = (results["Abs_Error"] / (results.get("Sales", 1))).mean()
        mean_error = results["Error"].mean()

        st.subheader("📊 Metrics")
        st.write(f"RMSE: {rmse:.2f}")
        st.write(f"MAPE: {mape*100:.2f}%")
        st.write(f"Mean Error: {mean_error:.2f}")

        # Best & Worst predictions
        st.subheader("Top 5 Best Predictions")
        st.dataframe(results.nsmallest(5, "Abs_Error"))

        st.subheader("Top 5 Worst Predictions")
        st.dataframe(results.nlargest(5, "Abs_Error"))

        # Download results
        csv = results.to_csv(index=False).encode()
        st.download_button(
            label="📥 Download Predictions CSV",
            data=csv,
            file_name="predictions.csv",
            mime="text/csv",
        )

        # Show results
        st.subheader("📊 Predictions")
        st.dataframe(results)

# Visualizations
        st.subheader("📊 Visualizations")

        st.subheader("📈 Actual vs Predicted Sales")
        if 'Sales' in results.columns:
            if 'Date' in results.columns:
                results['Date'] = pd.to_datetime(results['Date'])
                results_sorted = results.sort_values('Date')
                st.line_chart(results_sorted.set_index('Date')[['Sales', 'Predicted_Sales']])
            else:
                st.line_chart(results[['Sales', 'Predicted_Sales']])
        else:
            st.info("Upload a dataset with 'Sales' column to view Actual vs Predicted chart.")

        st.subheader("📊 Top 10 Worst Predictions by Error")
        worst = results.nlargest(10, "Abs_Error")
        st.bar_chart(worst.set_index('Store')['Abs_Error'])

        st.subheader("🔹 Predicted vs Actual Scatter Plot")
        if 'Sales' in results.columns:
            st.pyplot(results.plot.scatter(x='Sales', y='Predicted_Sales', alpha=0.6, figsize=(6,4)).figure)
        else:
            st.info("Upload a dataset with 'Sales' column to view Predicted vs Actual scatter plot.")

        if 'Sales' in results.columns and 'Date' in results.columns:
            fig = px.scatter(results, x='Sales', y='Predicted_Sales', color='Store',
                             title="Predicted vs Actual Sales", hover_data=['Date'])
            st.plotly_chart(fig)