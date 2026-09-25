#Series: structure de donnée unidimensionnelle hitahirizana donnée 
#Valeur miaraka amin'ny index
#0  Rakoto
#1  Rabe
#2  Lita

#Creation des series:
import pandas as pd

noms = pd.Series(["rakoto", "rabe", "lita"])
print(noms)

#Séries avec index personnalisé
notes = pd.Series(
    [12, 15, 18],
    index = ["rakoto", "rabe", "randria"]
)

print(notes)
# rakoto      12
# rabe        15
# randria     18

print (notes["rabe"]) #15

