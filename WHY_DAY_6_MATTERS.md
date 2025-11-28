# 📌 Why Day 6 Matters

Day 6 is the **backend foundation** for the Day 7 Streamlit app.  
It prepares everything so the app is clean, fast, and professional.

---

## What Day 6 Does

- **Prediction Pipeline**: `preprocess(df)` & `predict_sales(df)` ready for Streamlit.  
- **Evaluation Outputs**: saves `results_predictions.csv`, `metrics.csv`, and `top_worst_predictions.csv`.  
- **Avoids Heavy Computation**: Streamlit only loads results & images.  
- **Professional Structure**: clean folders, reusable code, modular workflow.

---

## Architecture Overview
```
|-- model/xgb_retail_model.pkl
|-- data/cleaned_dataset.csv
|-- images/ (plots)
|-- outputs/results_predictions.csv
|-- outputs/metrics.csv
|-- outputs/top_worst_predictions.csv
|-- 6.py # Backend processing (Day 6)
|-- 7.py # will be Streamlit UI (Day 7)
```



**Day 6 → prepares everything**  
**Day 7 → displays everything**

---