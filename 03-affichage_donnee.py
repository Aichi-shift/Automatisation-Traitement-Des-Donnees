import streamlit as st
import pandas as pd

# st.dataframe()
clients = pd.DataFrame({
    "Nom": ["Rakoto", "Rabe", "Lita", "Randria"],
    "Age": [20, 30, 50, 12],
    "Ville": ["tana", "diego", "fianarantsoa", "anosy"]
})
st.title("Liste des clients")
st.dataframe(clients)


# st.table(): fonction hanehoana tableau statique
produits = pd.DataFrame({
    "Produits": ["PC", "Clavier", "Souris"],
    "Prix": [10000, 50000, 6000],
    "Quantite": [12, 50, 60]
})
st.title("Catalogue")
st.table(produits)


# Message et alerte
import streamlit as st

# st.success(): notification (succés)
st.subheader("Success")
st.success("Connexion réussie")

# st.info(): 
st.subheader("Info")
st.info("Veuillez vous connecter")

# st.warning()
st.subheader("warning")
st.info("Aucun fichier n'a encore importer")

# st.error()
st.subheader("Error")
st.error("Veuillez saisir votre mot de passe")
