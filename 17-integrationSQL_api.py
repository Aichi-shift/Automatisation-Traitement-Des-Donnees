import pandas as pd
import sqlite3

# read_sql()
# read_sql_query(): maka donnée anaty SQL ho lasa DataFrame
conn = sqlite3.connect("database.db")
df = pd.read_sql_query("SELECT * FROM clients", conn)
print(df)

# Ecriture vers SQL
# to_sql(): hitehirizana data ao anaty DataFrame mankany amin'ny basse de donnée sql
df.to_sql(
    "client",
    conn,
    if_exists = "replace",
    index = False
)
# if_exists: paramètre mamaritra izay atao raha efa misy ilay table
# fail: mamoaka erreur raha efa misy ilay table
# replace: mamafa table vaovao dia mamorona vaovao
# append: manampy donnée vaovao anaty table efa misy
# 
# Ingestion API
# fakana donnée avy amin'ny internet (API REST)
# 
url = "https://api.exemples.com/ventes"

import requests
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)