#PANDAS:
#Data preparation: analyse des données, nettoyage, transformation
#Aalyse des données: statistique, KPI

#installation: pip insstall pandas

# DataFrame: structure de donnée mitovy amin'ny tableau excel, misy ligne sy colonne
# Mitahiry donnée amin'ny format structuré (row +colums)
import pandas as pd

df = pd.DataFrame ({

    "Nom": ["Rakoto", "Rabe"],
    "Age" : [25,26],
    "Ville" : ["Tana", "Toamasina"]
})

print(df)