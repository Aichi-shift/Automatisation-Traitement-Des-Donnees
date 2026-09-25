# Gestion des doublons:
# doublons: lignes miverimberina anaty DataFrame

# duplicated(): hamantarana doublons
# True: raha misy doublon
# False: raha tsy misy doublon
# 
import pandas as pd

df = pd.read_csv("personne.csv")
df.duplicated() #True / False

# Nombre de doublon:
print(df.duplicate().sum())

# drop_duplicates(): suppression lignes misy doublons
print(df.drop_duplicates()) #mamafafa doublons amin'ny colonne rehetra

print(df.drop_duplicates(subset = ["Nom"], inplace = True))

