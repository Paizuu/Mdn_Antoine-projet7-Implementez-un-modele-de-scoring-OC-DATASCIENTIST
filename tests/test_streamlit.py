# TEST de l'interface streamlit

import pytest
from streamlit.testing.v1 import AppTest
import json
import os
import requests

# Définir le chemin du fichier Streamlit
APP_PATH = "api/app_streamlit.py"

# Test que l'application Streamlit se charge sans erreur
def test_app_loads():
    at = AppTest.from_file(APP_PATH)
    at.run()
    assert at

# Test que les valeurs initiales sont bien chargées
def test_initial_values():
    at = AppTest.from_file(APP_PATH)
    at.run()
    assert "form_values" in at.session_state
    assert isinstance(at.session_state.form_values, dict)

# Test la modification d'une valeur
def test_user_input():
    at = AppTest.from_file(APP_PATH)
    at.run()
    at.number_input(key="AMT_INCOME_TOTAL").set_value(50000.0).run()
    assert at.session_state.form_values["AMT_INCOME_TOTAL"] == 50000.0

