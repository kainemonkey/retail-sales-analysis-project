import pandas as pd
import numpy as np
import joblib
import os











# -----------------------------
# Create necessary folders
# -----------------------------
os.makedirs("outputs", exist_ok=True)

# -----------------------------
# Load model
# -----------------------------
MODEL_PATH = "xgb_retail_model.pkl"



print("🔄 Loading model...")
model = joblib.load(MODEL_PATH)
print("✅ Model loaded successfully!")


# -----------------------------
# Preprocessing Function
# -----------------------------
def preprocess(df):
    cols_to_drop = [
        'PromoInterval', 'CompetitionOpenDate', 'Date'
    ]
    df = df.drop(columns=cols_to_drop, errors="ignore")

    # Fix StateHoliday mapping
    df['StateHoliday'] = df['StateHoliday'].replace(
        {'0': 0, 'a': 1, 'b': 2, 'c': 3, 0: 0}
    )

    return df


# -----------------------------
# Prediction Pipeline
# -----------------------------
def predict_sales(input_df):
    processed = preprocess(input_df)
    preds = model.predict(processed)
    return preds


# ------------------------
# Load test data
# -----------------------------

print("📁 Loading dataset...")
data = pd.read_csv("cleaned_dataset.csv")

X_test = data.drop(['Sales', 'Date'], axis=1)
y_test = data['Sales']

X_test = preprocess(X_test)

print("✅ Data ready for prediction.")


# -----------------------------
# Generate Predictions
# -----------------------------

print("🔮 Running predictions...")

preds = predict_sales(X_test)


results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": preds

})
results["Error"] = results["Actual"] - results["Predicted"]

results["Abs_Error"] = abs(results["Error"])


# Save results
results.to_csv("outputs/results_predictions.csv", index=False)

print("📄 Saved → outputs/results_predictions.csv")


# -----------------------------
# Compute Metrics
# ---------------------------

rmse = np.sqrt((results["Error"] ** 2).mean())

mape = (abs(results["Error"]) / results["Actual"]).mean()

mean_error = results["Error"].mean()

metrics = pd.DataFrame([{
    "RMSE": rmse,
    "MAPE": mape,
    "Mean Error": mean_error
}])



metrics.to_csv("outputs/metrics.csv", index=False)
print("📊 Saved → outputs/metrics.csv")







# -----------------------------
# Save worst predictions
# -----------------------------

worst = results.nlargest(10, "Abs_Error")
worst.to_csv("outputs/top_worst_predictions.csv", index=False)

print("⚠️ Worst predictions → outputs/top_worst_predictions.csv")










# -----------------------------
# Save best predictions
# -----------------------------
best = results.nsmallest(10, "Abs_Error")


best.to_csv("outputs/top_best_predictions.csv", index=False)
print("✅ Best predictions → outputs/top_best_predictions.csv")




