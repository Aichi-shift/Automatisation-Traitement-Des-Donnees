# indexation et selection:
# ahafahana misafidy donnée ao anaty DataFrame
# .loc[]: séléction par labels
# hisafidianana donnée amin'ny alalan'ny labels
# syntaxe:
# df.loc[lignes, colonnes]
# lignes: anaran'ny index
# colonnes: anaran'ny colonne

import pandas as pd

df = pd.DataFrame({
    "Nom" : ["rakoto", "rabe", "Lita", "randria"],
    "Age": [25,36,42,52],
    "Ville" : ["Tana", "Toamasina", "toliara", "Fianarantsoa"]
})

# rabe
# print(df.loc[1, "Nom"])
print(df.loc[1])

# selection plusieurs lignes et colonnes
print(df.loc[[0, 2], ["Nom", "Age"]])


# selection par postion:
# .iloc[]:  
# hakana données amin'ny alalan'ny position numérique
# syntaxe:
# df.iloc[ligne, colonne]

print("\n", df.iloc[0:3, 0:2])
# 0:3 : ligne position 0   -> ligne position 3
# 0:2 : colonne position 0 -> colonne position 2




