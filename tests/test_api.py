import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_dummy():
    assert 1 + 1 == 2

# Test si l'API démarre bien
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Credit Scoring API is up and running"}

# # Test avec des données valides
# def test_prediction_valid():
#     sample_data = {
#         "feature1": 1.5,
#         "feature2": 3.2,
#         "feature3": "A",
#         "feature4": 0
#     }
    
#     response = client.post("/predict/", json=sample_data)
    
#     assert response.status_code == 200
#     json_response = response.json()
    
#     assert "Classe prédite pour ces données" in json_response
#     assert "Prédiction de la TARGET 0" in json_response
#     assert "Prédiction de la TARGET 1" in json_response
#     assert isinstance(json_response["Prédiction de la TARGET 0"], float)
#     assert isinstance(json_response["Prédiction de la TARGET 1"], float)

# Test avec des données invalides (ex: champ manquant)
def test_prediction_invalid():
    sample_data = {
        "feature1": 1.5,
        "feature3": "A"  # Manque feature2 et feature4
    }
    
    response = client.post("/predict/", json=sample_data)
    
    assert response.status_code == 500  # L'API doit retourner une erreur

# Test avec un format de données incorrect (ex: une liste au lieu d'un dict)
def test_prediction_invalid_format():
    sample_data = [
        {"feature1": 1.5, "feature2": 3.2, "feature3": "A", "feature4": 0}
    ]
    
    response = client.post("/predict/", json=sample_data)
    
    assert response.status_code == 500  # L'API doit gérer ce cas proprement

