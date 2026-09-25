# Apply: hampiharana fonction amin'ny valeur tsirairay ao amin'ny DataFrame
import pandas as pd

df = pd.DataFrame({
    "Age": [18, 56, 24]
})

df["age_x2"] = df["Age"].apply(lambda x: x * 2)
print(df)

df2 = pd.DataFrame({
    "Total": [4_000_000, 5_000_000, 3_000_000]
})

df2["Categorie"] = df2["Total"].apply(lambda x: "Grande vente" if x > 3_000_000 else "Petite vente")
print(df2)