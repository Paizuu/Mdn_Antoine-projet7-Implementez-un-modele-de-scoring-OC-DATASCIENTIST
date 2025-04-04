from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import mlflow
import mlflow.sklearn  
import os
import re

# Charger le modèle MLflow
def load_model():
    model_uri = "mlruns/592004699819887619/0f136d13601d4180b6c9e002c5b6ed94/artifacts/model"
    model = mlflow.sklearn.load_model(model_uri)
    return model

def encode_categories(data):
    # Charger les données de train pour avoir les mêmes colonnes
    train_data = pd.read_csv("train_data.csv")
    # Passer les données en Dataframe
    data_df = pd.DataFrame([data])
    # Order sur l'ordre d'origine
    data_df = data_df[train_data.columns]

    return data_df

def predict(model, data):

    data_df = encode_categories(data)

    prediction = model.predict_proba(data_df)

    print("post predict")

    return prediction

def predict_class(model, data):

    data_df_class = encode_categories(data)

    class_predite = model.predict(data_df_class)

    print("post predict class")

    return class_predite

# Charger le modèle au démarrage
model = load_model()
