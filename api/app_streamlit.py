import streamlit as st
import requests
import json
import os

# Définition de l'URL de l'API FastAPI déployée sur Render
API_URL = "https://mdn-antoine-projet7-implementez-un.onrender.com/predict/"

st.title("🔍 Interface de Prédiction - Crédit Scoring")

st.write("Entrez les informations du client pour obtenir une prédiction.")


# Récupérer le chemin absolu
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "fonctional_request.json")

# Chargement des données avec gestion d'erreur
try:
    with open(json_path, "r") as f:
        example_data = json.load(f)
except FileNotFoundError:
    st.error(f"❌ Fichier JSON introuvable à : {json_path}")
    st.stop()


# Générer dynamiquement les champs du formulaire
user_input = {}
for key, value in example_data.items():
    if isinstance(value, int):
        user_input[key] = st.number_input(key, value=value, step=1)
    elif isinstance(value, float):
        user_input[key] = st.number_input(key, value=value, step=0.0001)
    elif isinstance(value, str):
        user_input[key] = st.text_input(key, value=value)
    elif isinstance(value, bool):
        user_input[key] = st.checkbox(key, value=value)

# Bouton pour soumettre les données à l’API
if st.button("🔍 Prédire"):
    response = requests.post(API_URL, json=user_input)

    if response.status_code == 200:
        st.success("✅ Prédiction réussie !")
        st.json(response.json())
    else:
        st.error("❌ Erreur lors de la prédiction.")
        st.write(response.text)
