# Type de donnée:
# int, float, object, datetime (date et heure)
# 
# astype(): hanovana ny type de donnée an'ny colonne
import pandas as pd

df = pd.DataFrame({
    "Age": ["20", "30"],
    "Date": ["2025-01-01", "2024-03-24"]
})
# conversion string -> int
df["Age"] = df["Age"].astype(int)

# conversion string-> datetime
df["Date"] = pd.to_datetime(df["Date"])

print(df)