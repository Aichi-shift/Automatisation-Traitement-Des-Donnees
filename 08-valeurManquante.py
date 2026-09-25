# Valeur m  manquante:
# NaN (Not A Number), none
# 
# isnull(): hamantarana ny cellulle misy valeur manquante
# True raha misy
# False raha tsy misy valeur manquante
# 
import pandas as pd
df = pd.DataFrame({
    "Nom": ["Rakoto", "Rabe", None],
    "Age": [20, 30, 15],
    "Ville": [None, "Toamasina", "tana"]
}) 

print(df.isnull())

# isan'ny valeur manquante
print(df.isnull().sum())

# dropna(): hamafana ligne na colonne misy valeur manquante
df2 = df.dropna()
print(df2.head())

# fillna(): hanoloana valeur manquante
print(df.fillna(0))

df["Age"] = df["Age"].fillna(10)
print(df.head()) 


moyenne = df["Age"].mean()
df["Age"] = df["Age"].fillna(moyenne)

