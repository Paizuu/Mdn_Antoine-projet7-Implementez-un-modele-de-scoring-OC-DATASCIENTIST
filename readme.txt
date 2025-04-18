# NOTES INTRODUCTIVES

Ce document a pour objectif de présenter le contexte du projet ainsi que le découpage des dossiers.


# CONTEXTE

La société "Prêt à dépenser" souhaite mettre en place un système automatisé de scoring.  
L'objectif est d’évaluer la capacité des clients à rembourser ou non leur crédit, et d’améliorer l’efficacité du processus de décision.


# MISSIONS

- Développer un modèle de scoring capable de prédire le risque de défaut des clients.  
- Analyser les features qui contribuent le plus au modèle, de manière générale (feature importance globale) et au niveau d’un client (feature importance locale).  
- Mettre en production le modèle de scoring avec une interface à l’aide d’une API.  
- Le tout en mettant en œuvre une approche globale MLOps de bout en bout pour le tracking des expérimentations.


# NETTOYAGE DU DOSSIER DE RENDU

Le dossier de rendu a été nettoyé pour limiter son volume. Les dossiers suivants ont été supprimés :

- Dossier des données sources  
- Dossier de l’environnement virtuel  
- Une partie des runs/modélisations sauvegardées via mlflow


# DECOUPAGE DES DOSSIERS

Dossier 'api' : comprend les principaux fichiers de l'API  
- model.py qui permet de charger le modèle  
- main.py qui structure l’API avec FASTAPI  
- app_streamlit.py qui crée l’interface de remplissage de données client sur une 2e API  
- fonctional_requests.json qui comprend une ligne de données client sous format json  

Dossier 'tests' : comprend les fichiers de tests  
- test_api.py teste les fonctions de l’API FASTAPI (main.py)  
- test_streamlit.py teste les fonctions de l’interface Streamlit (app_streamlit.py)  

Dossier 'mlruns' : comprend l’enregistrement en local du tracking mlflow

Fichier requirements.txt liste les packages utilisés dans l'environnement virtuel

# LIENS GITHUB

REPO GITHUB DU PROJET : 
https://github.com/Paizuu/Mdn_Antoine-projet7-Implementez-un-modele-de-scoring-OC-DATASCIENTIST

HISTORIQUE DES COMMITS DU PROJET:
https://github.com/Paizuu/Mdn_Antoine-projet7-Implementez-un-modele-de-scoring-OC-DATASCIENTIST/commits/main/

DEPLOIEMENT DES API VIA GITHUB ACTIONS :
https://github.com/Paizuu/Mdn_Antoine-projet7-Implementez-un-modele-de-scoring-OC-DATASCIENTIST/actions
