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
    at.number_input("AMT_INCOME_TOTAL").set_value(50000.0).run()
    assert at.session_state.form_values["AMT_INCOME_TOTAL"] == 50000.0

@patch("requests.post")
def test_api_call(mock_post):
    """Test l'envoi d'une requête API et la gestion de la réponse."""
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"prediction": "Approved"}
    
    at = AppTest.from_file(APP_PATH)
    at.run()
    at.button("Prédire").click().run()
    
    mock_post.assert_called_once()
    assert "Prédiction réussie" in at.html
    assert "Approved" in at.html
