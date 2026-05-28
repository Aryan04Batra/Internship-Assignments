import pandas as pd
dates = ["2025-01-01", "2025-02-15", "2025-03-20"]
ts = pd.to_datetime(dates)
print("Time Series:")
print(ts)
print("\nType:")
print(type(ts))