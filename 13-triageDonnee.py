# Tri des données: handaminana ligne ao anaty DataFrame arakarakin'ny valeur ao anaty colonne iray
# sort_values(): handaminana DataFrame arakaraky ny valeur ao amin'ny colonne iray
import pandas as pd
df = pd.read_csv("personne.csv")


# tri ordre croissant:
df_sorted = df.sort_values(by = "Age")
# by: mamaritra ny colonne hanaovana tri

# tri ordre decroissant:
df.sort_values(by = "Age", ascending = False)
# ascending= False: manaraka ordre decroissant

# sort_index(): organiser le DataFrame suivant les index
df2= pd.DataFrame({
    "Nom": ["Rakoto", "Rabe", "Lita"],
    "Age": [20, 19, 26]
}, index= [2, 0, 1])

df_sort= df.sort_index()
print(df_sort)


# teo aloha: 2, 0, 1
# aorian'ny sort_index(): 0, 1, 2