#Dataframe: structure de donnée bidimensionnelle

# Creation à partir dictionnaire
import pandas as pd

etudiants = {
    "Nom" : ["rakoto", "Rabe", "Lita"],
    "Age" : [15, 62, 24],
    "Ville" : ["tana", "Toliara", "Toamasina"]
}

df = pd.DataFrame(etudiants)

#Création DataFrame à partir liste:
data = [
    ["Rakoto", 20, "tamatave"],
    ["Rabe", 30, "Tana"],
    ["Lita", 19, "Toliara"]
]

df = pd.DataFrame(
    data,
    colums = ["Nom", "age", "Ville"]
)

#création dataframe à partir fichier csv
df = pd.read_csv("etudiant.csv")
print(df)

#read_csv(): mamaky contenu anaty fichier csv, mamadika azy ho lasa dataframe
   