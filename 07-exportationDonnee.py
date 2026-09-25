# Exportation de donnée:
# Mitahiry donnée ao anaty DataFrame ho las fichier any ivelany
# 
# to_csv(): exportation DataFrame -> csv
import pandas as pd

df = pd.DataFrame({
    "Nom": ["rakoto", "Rabe", "Randria"],
    "Age": [20, 32, 24]
})

df.to_csv("etudiant.csv", index = False)
# index = False: tsy tehirizina anaty fichier ny index

# to_excel: DataFrame -> Excel
df.to_excel("etudiant.xlsx", index = False)


# to_json: DataFrame->JSON
df.to_json("etudiant.json", orient = "records", indent = 4)
# orient = "records": mamadika ny ligne tsirairay ho objet json
# indent = 4:
#       tsy misy indent: 
{{}, {}, {}} 
#       misy indent:
{
    {

    },
    {

    }
}