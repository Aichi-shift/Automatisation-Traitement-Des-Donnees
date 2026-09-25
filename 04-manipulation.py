import pandas as pd

# Affichage première ligne:
# pd.head()
df = pd.DataFrame({
        "Nom" : ["Rakoto", "Rabe", "Randria", "Jezana", "Rasoa", "Lita"],
        "Age" : [20, 16, 50, 85, 20, 25]
    })  

print(df.head()) #Afficher les 5 premieres lignes
print(df.head(3)) #Affciher les 3 premières lignes


#Affichage dernière lligne:
#pd.tail()
print(df.tail())#afficher les 5 dernières lignes
print(df.tail(2)) #afficher les 2 dernières lignes

#informations generales
#info: mampiseho ny informations générales momba ny DataFrame 
#nombres de lignes
# nombres de colonnes
# anaran'ny colonne
# type de donnée
# nombre de valeur non nulle par colonne
# taille de mémoire ampiasain'ny dataframe 
print(df.info())

# Statistique descriptive:
# describe():
# count: isan'ny valeur
# mean: moyenne
# min: valeur minimale
# 25%: premiere quartile
# 50%: deuxieme quartile ou median
# 75%: troisieme quartile
# max: valeur maximale

df.describe()  

#selectionner une colonne
print(df["Nom"]) #colonne iray
print(df["Age"].mean()) #valeur moyenne age

# selectionner plusieurs colonne
print(df[["Nom","Age"]]) 

# Suppression colonne:
df.drop("Nom", axis= 1, inplace= True)
# axis = 0: manambara fa mamafa ligne
# axis = 1: mamambara fa mamafa colonne 
# inplace = True: modifer-na mivantana ilay dataframe
# inplace = false: mamorona DataFrame vaovao 

#filtre donnée:
df2 = pd.read_csv("personne.csv")
print(df2(df2["Age">30]))

print(df2)

# Plusieurs  avec AND (&)
print(df[(df["Age"] > 30) & (df["Ville"] == "Mahajanga")])

# Plusieurs condition avec OR (|)
print(df[(df["Age"]>20) | (df["Ville"] == "Toliara")])

# Nom, Age, Ville
# Rakoto, 25, Tana
# Rabe, 30, Toliara
# lita, 43, Toamasina
# Randria, 50, Mahajanga