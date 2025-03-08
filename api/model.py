from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import mlflow
import mlflow.sklearn  
import os
import re

# Charger le modèle MLflow
def load_model():
    model_uri = "mlruns/592004699819887619/037c7248072b462db1b3b5ef509ced6e/artifacts/model"
    model = mlflow.sklearn.load_model(model_uri)
    return model

def encode_categories(data):
    # Charger les données de train pour avoir les mêmes colonnes
    train_data = pd.read_csv("train_data.csv")

    # # Vérification des colonnes disponibles
    # missing_cols = (set(train_data.columns)) - set(data.keys())
    # col_not_in = (set(data.keys())) - set(train_data.columns)

    # print(f"Train Columns: {train_data.columns}")
    # print(f"Data DF Columns: {data.keys()}")

    # if missing_cols:
    #     print(f"⚠️ Colonnes manquantes dans les données reçues par l'API : {missing_cols}")
    #     for col in missing_cols:
    #         data[col] = 0  # Ajouter les colonnes manquantes avec des valeurs par défaut (0)
    
    # if col_not_in:
    #     print(f"⚠️ Colonnes en trop qu'on kick : {col_not_in}")
    #     for col in col_not_in:
    #         del data[col] #Delete les colonnes non presente dans le train data

    data_df = pd.DataFrame([data])

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
