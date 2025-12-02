import pandas as pd
import numpy as np

np.random.seed(42)  # For reproducibility

n_rows = 100

data = {
    "Store": np.random.randint(1, 11, size=n_rows),  # Store IDs 1-10
    "DayOfWeek": np.random.randint(1, 8, size=n_rows),  # Days 1-7
    "Open": np.random.choice([0,1], size=n_rows, p=[0.1, 0.9]),
    "Promo": np.random.choice([0,1], size=n_rows, p=[0.6, 0.4]),
    "StateHoliday": np.random.choice([0,'a','b','c'], size=n_rows, p=[0.8,0.05,0.05,0.1]),
    "SchoolHoliday": np.random.choice([0,1], size=n_rows, p=[0.8,0.2]),
    "Sales": np.random.randint(2000, 10000, size=n_rows),  # Synthetic sales
    "Date": pd.date_range(start='2023-01-01', periods=n_rows)
}

df = pd.DataFrame(data)
df.to_csv("test_dataset_100.csv", index=False)

print("✅ test_dataset_100.csv created with 100 rows!")
