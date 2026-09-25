import pandas as pd

# creation de nouvelle colonne
df = pd.read_csv("personne.csv")
df["Ville"] = ["tana", "Toamasina", "Mahajanga"]

# calcul entre colonne:
df["Total"] = df["Prix"] * df["Quantite"]

