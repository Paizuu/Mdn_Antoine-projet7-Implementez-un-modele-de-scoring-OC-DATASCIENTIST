import streamlit as st
import requests
import json
import os

# Définition de l'URL de l'API FastAPI déployée sur Render
API_URL = "https://mdn-antoine-projet7-implementez-un.onrender.com/predict/"

st.title("🔍 Interface de Prédiction - Crédit Scoring")

st.write("Entrez les informations du client pour obtenir une prédiction.")


# Charger le fichier JSON (remplace par le bon chemin)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "fonctional_request.json")
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Liste des champs disponibles
field_names = list(data.keys())  # Extrait les noms des champs du JSON


# Récupérer le chemin absolu
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# json_path = os.path.join(BASE_DIR, "fonctional_request.json")

# # Chargement des données avec gestion d'erreur
# try:
#     with open(json_path, "r") as f:
#         example_data = json.load(f)
# except FileNotFoundError:
#     st.error(f"❌ Fichier JSON introuvable à : {json_path}")
#     st.stop()


# # Générer dynamiquement les champs du formulaire
# user_input = {}
# for key, value in example_data.items():
#     if isinstance(value, int):
#         user_input[key] = st.number_input(key, value=value, step=1)
#     elif isinstance(value, float):
#         user_input[key] = st.number_input(key, value=value, step=0.0001)
#     elif isinstance(value, str):
#         user_input[key] = st.text_input(key, value=value)
#     elif isinstance(value, bool):
#         user_input[key] = st.checkbox(key, value=value)

# # Bouton pour soumettre les données à l’API
# if st.button("🔍 Prédire"):
#     response = requests.post(API_URL, json=user_input)

#     if response.status_code == 200:
#         st.success("✅ Prédiction réussie !")
#         st.json(response.json())
#     else:
#         st.error("❌ Erreur lors de la prédiction.")
#         st.write(response.text)




import streamlit as st
import pandas as pd

# Charger les données initiales (exemple basé sur ton fichier JSON)
data = {"NAME_CONTRACT_TYPE":0,"FLAG_OWN_CAR":1,"FLAG_OWN_REALTY":1,"CNT_CHILDREN":0,"AMT_INCOME_TOTAL":225000.0,"AMT_CREDIT":101880.0,"AMT_ANNUITY":11101.5,"AMT_GOODS_PRICE":90000.0,"REGION_POPULATION_RELATIVE":0.019101,"DAYS_BIRTH":11788,"DAYS_EMPLOYED":-3489.0,"DAYS_REGISTRATION":-4378.0,"DAYS_ID_PUBLISH":-4450,"OWN_CAR_AGE":4.0,"FLAG_MOBIL":1,"FLAG_EMP_PHONE":1,"FLAG_WORK_PHONE":0,"FLAG_CONT_MOBILE":1,"FLAG_PHONE":0,"FLAG_EMAIL":0,"CNT_FAM_MEMBERS":2.0,"REGION_RATING_CLIENT":2,"REGION_RATING_CLIENT_W_CITY":2,"HOUR_APPR_PROCESS_START":11,"REG_REGION_NOT_LIVE_REGION":0,"REG_REGION_NOT_WORK_REGION":0,"LIVE_REGION_NOT_WORK_REGION":0,"REG_CITY_NOT_LIVE_CITY":0,"REG_CITY_NOT_WORK_CITY":0,"LIVE_CITY_NOT_WORK_CITY":0,"EXT_SOURCE_1":0.2124594938,"EXT_SOURCE_2":0.7238774842,"EXT_SOURCE_3":0.7557400502,"APARTMENTS_AVG":0.0598,"BASEMENTAREA_AVG":0.0632,"YEARS_BEGINEXPLUATATION_AVG":0.9811,"YEARS_BUILD_AVG":0.7416,"COMMONAREA_AVG":0.0087,"ELEVATORS_AVG":0.0,"ENTRANCES_AVG":0.1379,"FLOORSMAX_AVG":0.1667,"FLOORSMIN_AVG":0.2083,"LANDAREA_AVG":0.0204,"LIVINGAPARTMENTS_AVG":0.0479,"LIVINGAREA_AVG":0.0498,"NONLIVINGAPARTMENTS_AVG":0.0039,"NONLIVINGAREA_AVG":0.0093,"APARTMENTS_MODE":0.0609,"BASEMENTAREA_MODE":0.0656,"YEARS_BEGINEXPLUATATION_MODE":0.9811,"YEARS_BUILD_MODE":0.7517,"COMMONAREA_MODE":0.0088,"ELEVATORS_MODE":0.0,"ENTRANCES_MODE":0.1379,"FLOORSMAX_MODE":0.1667,"FLOORSMIN_MODE":0.2083,"LANDAREA_MODE":0.0209,"LIVINGAPARTMENTS_MODE":0.0523,"LIVINGAREA_MODE":0.0519,"NONLIVINGAPARTMENTS_MODE":0.0039,"NONLIVINGAREA_MODE":0.0099,"APARTMENTS_MEDI":0.0604,"BASEMENTAREA_MEDI":0.0632,"YEARS_BEGINEXPLUATATION_MEDI":0.9811,"YEARS_BUILD_MEDI":0.7451,"COMMONAREA_MEDI":0.0087,"ELEVATORS_MEDI":0.0,"ENTRANCES_MEDI":0.1379,"FLOORSMAX_MEDI":0.1667,"FLOORSMIN_MEDI":0.2083,"LANDAREA_MEDI":0.0208,"LIVINGAPARTMENTS_MEDI":0.0487,"LIVINGAREA_MEDI":0.0507,"NONLIVINGAPARTMENTS_MEDI":0.0039,"NONLIVINGAREA_MEDI":0.0095,"TOTALAREA_MODE":0.0459,"OBS_30_CNT_SOCIAL_CIRCLE":2.0,"DEF_30_CNT_SOCIAL_CIRCLE":0.0,"OBS_60_CNT_SOCIAL_CIRCLE":2.0,"DEF_60_CNT_SOCIAL_CIRCLE":0.0,"DAYS_LAST_PHONE_CHANGE":-2441.0,"FLAG_DOCUMENT_2":0,"FLAG_DOCUMENT_3":1,"FLAG_DOCUMENT_4":0,"FLAG_DOCUMENT_5":0,"FLAG_DOCUMENT_6":0,"FLAG_DOCUMENT_7":0,"FLAG_DOCUMENT_8":0,"FLAG_DOCUMENT_9":0,"FLAG_DOCUMENT_10":0,"FLAG_DOCUMENT_11":0,"FLAG_DOCUMENT_12":0,"FLAG_DOCUMENT_13":0,"FLAG_DOCUMENT_14":0,"FLAG_DOCUMENT_15":0,"FLAG_DOCUMENT_16":0,"FLAG_DOCUMENT_17":0,"FLAG_DOCUMENT_18":0,"FLAG_DOCUMENT_19":0,"FLAG_DOCUMENT_20":0,"FLAG_DOCUMENT_21":0,"AMT_REQ_CREDIT_BUREAU_HOUR":0.0,"AMT_REQ_CREDIT_BUREAU_DAY":0.0,"AMT_REQ_CREDIT_BUREAU_WEEK":0.0,"AMT_REQ_CREDIT_BUREAU_MON":0.0,"AMT_REQ_CREDIT_BUREAU_QRT":1.0,"AMT_REQ_CREDIT_BUREAU_YEAR":0.0,"CODE_GENDER_F":0,"CODE_GENDER_M":1,"NAME_TYPE_SUITE_Children":0,"NAME_TYPE_SUITE_Family":0,"NAME_TYPE_SUITE_Group of people":0,"NAME_TYPE_SUITE_Other_A":0,"NAME_TYPE_SUITE_Other_B":0,"NAME_TYPE_SUITE_Spouse, partner":0,"NAME_TYPE_SUITE_Unaccompanied":1,"NAME_INCOME_TYPE_Businessman":0,"NAME_INCOME_TYPE_Commercial associate":0,"NAME_INCOME_TYPE_Pensioner":0,"NAME_INCOME_TYPE_State servant":1,"NAME_INCOME_TYPE_Student":0,"NAME_INCOME_TYPE_Unemployed":0,"NAME_INCOME_TYPE_Working":0,"NAME_EDUCATION_TYPE_Academic degree":0,"NAME_EDUCATION_TYPE_Higher education":0,"NAME_EDUCATION_TYPE_Incomplete higher":1,"NAME_EDUCATION_TYPE_Lower secondary":0,"NAME_EDUCATION_TYPE_Secondary_special":0,"NAME_FAMILY_STATUS_Civil marriage":0,"NAME_FAMILY_STATUS_Married":1,"NAME_FAMILY_STATUS_Separated":0,"NAME_FAMILY_STATUS_Single_not_married":0,"NAME_FAMILY_STATUS_Widow":0,"NAME_HOUSING_TYPE_Co-op apartment":0,"NAME_HOUSING_TYPE_House_apartment":1,"NAME_HOUSING_TYPE_Municipal apartment":0,"NAME_HOUSING_TYPE_Office apartment":0,"NAME_HOUSING_TYPE_Rented apartment":0,"NAME_HOUSING_TYPE_With parents":0,"OCCUPATION_TYPE_Accountants":0,"OCCUPATION_TYPE_Cleaning staff":0,"OCCUPATION_TYPE_Cooking staff":0,"OCCUPATION_TYPE_Core staff":0,"OCCUPATION_TYPE_Drivers":0,"OCCUPATION_TYPE_HR staff":0,"OCCUPATION_TYPE_High skill tech staff":0,"OCCUPATION_TYPE_IT staff":0,"OCCUPATION_TYPE_Laborers":1,"OCCUPATION_TYPE_Low-skill Laborers":0,"OCCUPATION_TYPE_Managers":0,"OCCUPATION_TYPE_Medicine staff":0,"OCCUPATION_TYPE_Private service staff":0,"OCCUPATION_TYPE_Realty agents":0,"OCCUPATION_TYPE_Sales staff":0,"OCCUPATION_TYPE_Secretaries":0,"OCCUPATION_TYPE_Security staff":0,"OCCUPATION_TYPE_Waiters_barmen_staff":0,"WEEKDAY_APPR_PROCESS_START_FRIDAY":0,"WEEKDAY_APPR_PROCESS_START_MONDAY":1,"WEEKDAY_APPR_PROCESS_START_SATURDAY":0,"WEEKDAY_APPR_PROCESS_START_SUNDAY":0,"WEEKDAY_APPR_PROCESS_START_THURSDAY":0,"WEEKDAY_APPR_PROCESS_START_TUESDAY":0,"WEEKDAY_APPR_PROCESS_START_WEDNESDAY":0,"ORGANIZATION_TYPE_Advertising":0,"ORGANIZATION_TYPE_Agriculture":0,"ORGANIZATION_TYPE_Bank":0,"ORGANIZATION_TYPE_Business Entity Type 1":0,"ORGANIZATION_TYPE_Business Entity Type 2":0,"ORGANIZATION_TYPE_Business Entity Type 3":0,"ORGANIZATION_TYPE_Cleaning":0,"ORGANIZATION_TYPE_Construction":0,"ORGANIZATION_TYPE_Culture":0,"ORGANIZATION_TYPE_Electricity":0,"ORGANIZATION_TYPE_Emergency":0,"ORGANIZATION_TYPE_Government":0,"ORGANIZATION_TYPE_Hotel":0,"ORGANIZATION_TYPE_Housing":0,"ORGANIZATION_TYPE_Industry: type 1":0,"ORGANIZATION_TYPE_Industry: type 10":0,"ORGANIZATION_TYPE_Industry: type 11":0,"ORGANIZATION_TYPE_Industry: type 12":0,"ORGANIZATION_TYPE_Industry: type 13":0,"ORGANIZATION_TYPE_Industry: type 2":0,"ORGANIZATION_TYPE_Industry: type 3":0,"ORGANIZATION_TYPE_Industry: type 4":0,"ORGANIZATION_TYPE_Industry: type 5":0,"ORGANIZATION_TYPE_Industry: type 6":0,"ORGANIZATION_TYPE_Industry: type 7":0,"ORGANIZATION_TYPE_Industry: type 8":0,"ORGANIZATION_TYPE_Industry: type 9":0,"ORGANIZATION_TYPE_Insurance":0,"ORGANIZATION_TYPE_Kindergarten":0,"ORGANIZATION_TYPE_Legal Services":0,"ORGANIZATION_TYPE_Medicine":0,"ORGANIZATION_TYPE_Military":1,"ORGANIZATION_TYPE_Mobile":0,"ORGANIZATION_TYPE_Other":0,"ORGANIZATION_TYPE_Police":0,"ORGANIZATION_TYPE_Postal":0,"ORGANIZATION_TYPE_Realtor":0,"ORGANIZATION_TYPE_Religion":0,"ORGANIZATION_TYPE_Restaurant":0,"ORGANIZATION_TYPE_School":0,"ORGANIZATION_TYPE_Security":0,"ORGANIZATION_TYPE_Security Ministries":0,"ORGANIZATION_TYPE_Self-employed":0,"ORGANIZATION_TYPE_Services":0,"ORGANIZATION_TYPE_Telecom":0,"ORGANIZATION_TYPE_Trade: type 1":0,"ORGANIZATION_TYPE_Trade: type 2":0,"ORGANIZATION_TYPE_Trade: type 3":0,"ORGANIZATION_TYPE_Trade: type 4":0,"ORGANIZATION_TYPE_Trade: type 5":0,"ORGANIZATION_TYPE_Trade: type 6":0,"ORGANIZATION_TYPE_Trade: type 7":0,"ORGANIZATION_TYPE_Transport: type 1":0,"ORGANIZATION_TYPE_Transport: type 2":0,"ORGANIZATION_TYPE_Transport: type 3":0,"ORGANIZATION_TYPE_Transport: type 4":0,"ORGANIZATION_TYPE_University":0,"ORGANIZATION_TYPE_XNA":0,"FONDKAPREMONT_MODE_not specified":0,"FONDKAPREMONT_MODE_org spec account":0,"FONDKAPREMONT_MODE_reg oper account":1,"FONDKAPREMONT_MODE_reg oper spec account":0,"HOUSETYPE_MODE_block of flats":1,"HOUSETYPE_MODE_specific housing":0,"HOUSETYPE_MODE_terraced house":0,"WALLSMATERIAL_MODE_Block":0,"WALLSMATERIAL_MODE_Mixed":0,"WALLSMATERIAL_MODE_Monolithic":0,"WALLSMATERIAL_MODE_Others":0,"WALLSMATERIAL_MODE_Panel":1,"WALLSMATERIAL_MODE_Stone_brick":0,"WALLSMATERIAL_MODE_Wooden":0,"EMERGENCYSTATE_MODE_No":1,"EMERGENCYSTATE_MODE_Yes":0,"DAYS_EMPLOYED_ANOM":0,"CREDIT_INCOME_PERCENT":0.4528,"ANNUITY_INCOME_PERCENT":0.04934,"CREDIT_TERM":0.1089664311,"DAYS_EMPLOYED_PERCENT":-0.2959789617}

df = pd.DataFrame([data])

# Définition des groupes dynamiques
GROUPE_SELECTIONNABLE = {
    "CODE_GENDER": ["CODE_GENDER_F","CODE_GENDER_M"],
    "NAME_TYPE_SUITE": ["NAME_TYPE_SUITE_Children","NAME_TYPE_SUITE_Family","NAME_TYPE_SUITE_Group of people","NAME_TYPE_SUITE_Other_A","NAME_TYPE_SUITE_Other_B","NAME_TYPE_SUITE_Spouse, partner","NAME_TYPE_SUITE_Unaccompanied"],
    "NAME_INCOME_TYPE": ["NAME_INCOME_TYPE_Businessman","NAME_INCOME_TYPE_Commercial associate","NAME_INCOME_TYPE_Pensioner","NAME_INCOME_TYPE_State servant","NAME_INCOME_TYPE_Student","NAME_INCOME_TYPE_Unemployed","NAME_INCOME_TYPE_Working"],
    "NAME_EDUCATION_TYPE": ["NAME_EDUCATION_TYPE_Academic degree","NAME_EDUCATION_TYPE_Higher education","NAME_EDUCATION_TYPE_Incomplete higher","NAME_EDUCATION_TYPE_Lower secondary","NAME_EDUCATION_TYPE_Secondary_special"],
    "NAME_FAMILY_STATUS": ["NAME_FAMILY_STATUS_Civil marriage","NAME_FAMILY_STATUS_Married","NAME_FAMILY_STATUS_Separated","NAME_FAMILY_STATUS_Single_not_married","NAME_FAMILY_STATUS_Widow"],
    "NAME_HOUSING_TYPE": ["NAME_HOUSING_TYPE_Co-op apartment","NAME_HOUSING_TYPE_House_apartment","NAME_HOUSING_TYPE_Municipal apartment","NAME_HOUSING_TYPE_Office apartment","NAME_HOUSING_TYPE_Rented apartment","NAME_HOUSING_TYPE_With parents"],
    "OCCUPATION_TYPE": ["OCCUPATION_TYPE_Accountants","OCCUPATION_TYPE_Cleaning staff","OCCUPATION_TYPE_Cooking staff","OCCUPATION_TYPE_Core staff","OCCUPATION_TYPE_Drivers","OCCUPATION_TYPE_HR staff","OCCUPATION_TYPE_High skill tech staff","OCCUPATION_TYPE_IT staff","OCCUPATION_TYPE_Laborers","OCCUPATION_TYPE_Low-skill Laborers","OCCUPATION_TYPE_Managers","OCCUPATION_TYPE_Medicine staff","OCCUPATION_TYPE_Private service staff","OCCUPATION_TYPE_Realty agents","OCCUPATION_TYPE_Sales staff","OCCUPATION_TYPE_Secretaries","OCCUPATION_TYPE_Security staff","OCCUPATION_TYPE_Waiters_barmen_staff"],
    "WEEKDAY_APPR_PROCESS_START": ["WEEKDAY_APPR_PROCESS_START_FRIDAY","WEEKDAY_APPR_PROCESS_START_MONDAY","WEEKDAY_APPR_PROCESS_START_SATURDAY","WEEKDAY_APPR_PROCESS_START_SUNDAY","WEEKDAY_APPR_PROCESS_START_THURSDAY","WEEKDAY_APPR_PROCESS_START_TUESDAY","WEEKDAY_APPR_PROCESS_START_WEDNESDAY"],
    "ORGANIZATION_TYPE": ["ORGANIZATION_TYPE_Advertising","ORGANIZATION_TYPE_Agriculture","ORGANIZATION_TYPE_Bank","ORGANIZATION_TYPE_Business Entity Type 1","ORGANIZATION_TYPE_Business Entity Type 2","ORGANIZATION_TYPE_Business Entity Type 3","ORGANIZATION_TYPE_Cleaning","ORGANIZATION_TYPE_Construction","ORGANIZATION_TYPE_Culture","ORGANIZATION_TYPE_Electricity","ORGANIZATION_TYPE_Emergency","ORGANIZATION_TYPE_Government","ORGANIZATION_TYPE_Hotel","ORGANIZATION_TYPE_Housing","ORGANIZATION_TYPE_Industry: type 1","ORGANIZATION_TYPE_Industry: type 10","ORGANIZATION_TYPE_Industry: type 11","ORGANIZATION_TYPE_Industry: type 12","ORGANIZATION_TYPE_Industry: type 13","ORGANIZATION_TYPE_Industry: type 2","ORGANIZATION_TYPE_Industry: type 3","ORGANIZATION_TYPE_Industry: type 4","ORGANIZATION_TYPE_Industry: type 5","ORGANIZATION_TYPE_Industry: type 6","ORGANIZATION_TYPE_Industry: type 7","ORGANIZATION_TYPE_Industry: type 8","ORGANIZATION_TYPE_Industry: type 9","ORGANIZATION_TYPE_Insurance","ORGANIZATION_TYPE_Kindergarten","ORGANIZATION_TYPE_Legal Services","ORGANIZATION_TYPE_Medicine","ORGANIZATION_TYPE_Military","ORGANIZATION_TYPE_Mobile","ORGANIZATION_TYPE_Other","ORGANIZATION_TYPE_Police","ORGANIZATION_TYPE_Postal","ORGANIZATION_TYPE_Realtor","ORGANIZATION_TYPE_Religion","ORGANIZATION_TYPE_Restaurant","ORGANIZATION_TYPE_School","ORGANIZATION_TYPE_Security","ORGANIZATION_TYPE_Security Ministries","ORGANIZATION_TYPE_Self-employed","ORGANIZATION_TYPE_Services","ORGANIZATION_TYPE_Telecom","ORGANIZATION_TYPE_Trade: type 1","ORGANIZATION_TYPE_Trade: type 2","ORGANIZATION_TYPE_Trade: type 3","ORGANIZATION_TYPE_Trade: type 4","ORGANIZATION_TYPE_Trade: type 5","ORGANIZATION_TYPE_Trade: type 6","ORGANIZATION_TYPE_Trade: type 7","ORGANIZATION_TYPE_Transport: type 1","ORGANIZATION_TYPE_Transport: type 2","ORGANIZATION_TYPE_Transport: type 3","ORGANIZATION_TYPE_Transport: type 4","ORGANIZATION_TYPE_University","ORGANIZATION_TYPE_XNA"],
    "FONDKAPREMONT_MODE": ["FONDKAPREMONT_MODE_not specified","FONDKAPREMONT_MODE_org spec account","FONDKAPREMONT_MODE_reg oper account","FONDKAPREMONT_MODE_reg oper spec account"],
    "HOUSETYPE_MODE": ["HOUSETYPE_MODE_block of flats","HOUSETYPE_MODE_specific housing","HOUSETYPE_MODE_terraced house"],
    "WALLSMATERIAL_MODE": ["WALLSMATERIAL_MODE_Block","WALLSMATERIAL_MODE_Mixed","WALLSMATERIAL_MODE_Monolithic","WALLSMATERIAL_MODE_Others","WALLSMATERIAL_MODE_Panel","WALLSMATERIAL_MODE_Stone_brick","WALLSMATERIAL_MODE_Wooden"],
    "EMERGENCYSTATE_MODE": ["EMERGENCYSTATE_MODE_No","EMERGENCYSTATE_MODE_Yes"],
}

# Définition des champs calculés
def calcul_champs(data):
    data["CREDIT_INCOME_PERCENT"] = data["AMT_CREDIT"] / data["AMT_INCOME_TOTAL"]
    data["ANNUITY_INCOME_PERCENT"] = data["AMT_ANNUITY"] / data["AMT_INCOME_TOTAL"]
    data["CREDIT_TERM"] = data["AMT_ANNUITY"] / data["AMT_CREDIT"]
    data["DAYS_EMPLOYED_PERCENT"] = data["DAYS_EMPLOYED"] / data["DAYS_BIRTH"]
    return data

# Interface Streamlit
st.title("Interface de saisie dynamique")

# Stockage des valeurs dynamiques
if "form_values" not in st.session_state:
    st.session_state.form_values = data

data = st.session_state.form_values

def update_groups(selected_field, group):
    """Met à jour les autres champs du groupe à 0 si un champ est activé."""
    for field in group:
        if field != selected_field:
            st.session_state.form_values[field] = 0

def on_change(field, group):
    if st.session_state.form_values[field] == 1:
        update_groups(field, group)

# Affichage des groupes
for group_name, fields in GROUPE_SELECTIONNABLE.items():
    st.subheader(group_name)
    for field in fields:
        st.session_state.form_values[field] = st.radio(
            f"{field}",
            [0, 1],
            index=int(data[field]),
            key=field,
            on_change=on_change,
            args=(field, fields),
        )

# Affichage des champs classiques
st.subheader("Autres informations")
for field in data.keys():
    if field not in sum(GROUPE_SELECTIONNABLE.values(), []):
        if field in ["CREDIT_INCOME_PERCENT", "ANNUITY_INCOME_PERCENT"]:
            st.write(f"{field}: {data[field]:.4f}")  # Affichage sans modification possible
        else:
            st.session_state.form_values[field] = st.number_input(
                field, value=data[field]
            )

# Recalcul des champs calculés
st.session_state.form_values = calcul_champs(st.session_state.form_values)

st.write("### Données finales")
st.write(st.session_state.form_values)
