# Normalisation des données
import pandas as pd

df = pd.DataFrame({
    "Nom": ["Rakoto", "RABE", "LiTa"]
})


# lowercase
df["Nom"] = df["Nom"].str.lower() #tout en miniscule
print(df)

# suppression espaces
df["Nom"] = df["Nom"].str.strip()
print(df)


# Formatage colonne:
df.columns = df.columns.str.upper()
print(df)

# nom client -> nom_client
df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
