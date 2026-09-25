# GroupBy: regroupement donnée manana valeur mitovy anaty colonne iray 
import pandas as pd

df = pd.DataFrame({
    "Nom": ["Randria", "Rasoa", "Lita", "Rabe"],
    "Ville": ["Tana", "Tana", "Anosy", "Tana"],
    "Salaire": [2000, 3000, 6000, 20000]
})

group = df.groupby("Ville")
# group.size() : effectif à chaque ville
print(group.size())

# total des valeurs dans une colonne
print(group["Salaire"].sum())


