from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import mlflow
import mlflow.sklearn  
import os
import re

# Charger le modèle MLflow
def load_model():
    model_uri = "mlruns/592004699819887619/31a98f93ed8d4201bf1e05164b15b503/artifacts/model"
    model = mlflow.sklearn.load_model(model_uri)
    return model

def encode_categories(data):
    # Charger les données d'entraînement pour s'assurer d'avoir les mêmes colonnes
    train_data = pd.read_csv("train_data.csv")

    # Vérification des colonnes disponibles
    missing_cols = (set(train_data.columns)) - set(data.keys())
    col_not_in = (set(data.keys())) - set(train_data.columns)

    print(f"Train Columns: {train_data.columns}")
    print(f"Data DF Columns: {data.keys()}")

    if missing_cols:
        print(f"⚠️ Colonnes manquantes dans les données reçues par l'API : {missing_cols}")
        for col in missing_cols:
            data[col] = 0  # Ajouter les colonnes manquantes avec des valeurs par défaut (0)
    
    if col_not_in:
        print(f"⚠️ Colonnes en trop qu'on kick : {col_not_in}")
        for col in col_not_in:
            del data[col] #Delete les colonnes non presente dans le train data

    data_df = pd.DataFrame([data])

    data_df = data_df[train_data.columns]

    return data_df

def predict(model, data):
    # Convertir les données reçues en DataFrame
    

    # Vérification des données reçues
    # print("\n=== Données reçues par l'API ===")
    # print(data_df.head())
    # print("Colonnes du DataFrame :", list(data_df.columns))

    # Encoder les colonnes catégorielles

    print("pre categori")
    data_df = encode_categories(data)

    print("post categoi")
    
    

    # Vérification après encodage
    # print("\n=== Données après encodage ===")
    # print(data_encoded.head())

    print("pre bs")


    print("pre predict")

    print("data_df",data_df.columns.tolist() )

    # Prédiction avec le modèle
    prediction = model.predict_proba(data_df)[:, 1]

    print("post predict")

    return prediction[0]

# Charger le modèle au démarrage
model = load_model()
