import streamlit as st
# widget: composant ahafahan'ny utilisateur mifandray amin'ny application
# 

# st.button(): composant hamoronana boutton() ao amin'ny application
# syntaxe: st.button(label)
 
st.title("Exemple boutton")
if st.button("Afficher message"):
    st.success("Bienvenue dans l'analyse des données")

# st.checkbox():
st.subheader("Exemple checkbox")
accepte = st.checkbox("J'accepte les conditions")
if accepte:
    st.success("Merci pour votre confirmation")
else:
    st.warning("Veuillez accepter les conditions")

# st.radio()
st.subheader("Choix de langue")

langue = st.radio(
    ["Français", "Anglais", "Malagasy"]
)

st.write("Vous avez choisi ", langue)

# st.selectbox(): liste deroulante
st.subheader("choix d'un pays")
pays = st.selectbox("Sélectionner votre pays", ["Madagogo", "Canada", "France", "Angleterre"])
st.write("Pays séléctinné: ", pays)

# st.multiselect()
st.subheader("Compétences ")
competences= st.multiselect(
    "Séléctionner vos compétences", [
        "Python",
        "Pandas",
        "Matplotlib",
        "Streamlit"
    ]
)
st.write("Compétences choisie: ")
st.write(competences)