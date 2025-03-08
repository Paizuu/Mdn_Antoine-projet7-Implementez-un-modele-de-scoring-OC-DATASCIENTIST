# Imports
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
import pandas as pd
from api.model import load_model, predict, predict_class
# from api.schemas import ClientData  
from typing import Dict, Any
from fastapi import Body

app = FastAPI(
    title="Credit Scoring API",
    description="API de prédiction du score client utilisant le modèle RandomForest optimisé.",
    version="1.0.0"
)

# Charger le modèle lors du démarrage de l'API
model = load_model()

@app.post("/predict/")
async def get_prediction(data: Any = Body(...)):
    # data = await request.json()

    print("Données reçues : ", data)
    # Faire la prédiction
    try:
        prediction = predict(model, data)
        class_predite = predict_class(model, data)
        return {
            "Classe prédite pour ces données": int(class_predite[0]),
            "Prédiction de la TARGET 0": float(prediction[0, 0]),
            "Prédiction de la TARGET 1": float(prediction[0, 1])
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Point d'entrée racine pour tester l'API
@app.get("/")
def read_root():
    return {"message": "Credit Scoring API is up and running"}
