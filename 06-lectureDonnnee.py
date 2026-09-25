# Lecture de donnée:
# Mamaky donnée avy amina source ivelany havadika Dataframe 
# TYPE: csv, xlsx, sql, json
 
# read_csv(): hamakiana fichier csv havadika dataframe
import pandas as pd
df = pd.read_csv("clients.csv")
print(df.head()) #affichage 5 premières lignes

df = pd.read("clients.csv", sep = ",", encoding = "utf-8")
# sep = séparateur
# encoding = format texte


# read_excel(): hamakiana fichier Excel (.xlsx)
# installation openpyxl: pip install openpyxl
# Importation: Excel -> read_excel() -> DataFrame
# Exportation: DataFrame -> df.to_excel() 
df = pd.read_excel("ventes.xlsx")
print(df.head())

# DataFrame to Excel:
df.to_excel("resultat.xlsx", index = False)
#index = False: tsy misy index
# index = True: misy index

# read_json(): mamaky fichier json ho lasa DataFrame
df = pd.read_json("data.json")
print(df.head())

# Base de donnée SQL
import sqlite3

conn = sqlite3.connect("database.db")
df = pd.read_sql("SELECT * FROM client", conn)
print (df.head())



