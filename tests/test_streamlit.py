import pytest
from streamlit.testing.v1 import AppTest
import json
import os
import requests
from unittest.mock import patch

# Définir le chemin du fichier Streamlit
APP_PATH = "api/app_streamlit.py"

def test_app_loads():
    """Test que l'application Streamlit se charge sans erreur."""
    at = AppTest.from_file(APP_PATH)
    at.run()
    assert at

def test_initial_values():
    """Test que les valeurs initiales sont bien chargées dans session_state."""
    at = AppTest.from_file(APP_PATH)
    at.run()
    assert "form_values" in at.session_state
    assert isinstance(at.session_state.form_values, dict)


def test_user_input():
    """Test la modification d'une valeur et sa mise à jour dans session_state."""
    at = AppTest.from_file(APP_PATH)
    at.run()
    at.number_input(key="AMT_INCOME_TOTAL").set_value(50000.0).run()
    assert at.session_state.form_values["AMT_INCOME_TOTAL"] == 50000.0

@patch("requests.post")
def test_api_call(mock_post):
    """Test l'envoi d'une requête API et la gestion de la réponse."""
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "Classe prédite pour ces données": 1,
        "Prédiction de la TARGET 0": 0.35,
        "Prédiction de la TARGET 1": 0.65
    }
    
    at = AppTest.from_file(APP_PATH)
    at.run()
    at.button(key="predict_button").click().run()
    
    mock_post.assert_called_once()
    
    # Vérification améliorée du message de succes
    success_messages = [str(msg) for msg in at.get("st.success")]
    assert any("Prédiction réussie" in msg for msg in success_messages), f"Message de succès non trouvé. Messages: {success_messages}"
    
    # Vérification de l'affichage JSON
    json_displayed = json.dumps(at.get("st.json"))
    assert "Classe prédite pour ces données" in json_displayed, f"JSON non trouvé: {json_displayed}"

