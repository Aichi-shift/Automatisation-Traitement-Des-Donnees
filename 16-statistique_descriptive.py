# statistique descriptives:
# mean(): 
# df["salaire"].mean()

# min()
# df["salaire"].min()

# max()
# df["salaire"].max()




# mode(): hitadiavana valeur miverimberina anaty colonne iray
import pandas as pd
df = pd.DataFrame({
    "Age": [20, 22, 30, 20]
})
print(df["Age"].mode()) #20

# describe(): manome résumé automatique
# moyenne, minimum, quartile (25%, 50%, 75%)
print(df.describe())

# idxmax(): mamerina ny index misy ny valeur lehibe indrindra

# idxmin(): mamerina ny index misy ny valeur kely indrindra

print(df["Age"].idxmax()) #2
print(df["Age"].idxmin()) #0