import pytest
from fastapi.testclient import TestClient
from api.main import app
from api.model import load_model, predict, predict_class, encode_categories
import pandas as pd

client = TestClient(app)

def test_dummy():
    assert 1 + 1 == 2


# Test de la route principale
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Credit Scoring API is up and running"}

# # Test du endpoint de prédiction avec des données valides
# def test_predict_valid():
#     sample_data = {"NAME_CONTRACT_TYPE":0,"FLAG_OWN_CAR":1,"FLAG_OWN_REALTY":1,"CNT_CHILDREN":1,"AMT_INCOME_TOTAL":234000.0,"AMT_CREDIT":1080000.0,"AMT_ANNUITY":34969.5,"AMT_GOODS_PRICE":1080000.0,"REGION_POPULATION_RELATIVE":0.003541,"DAYS_BIRTH":10664,"DAYS_EMPLOYED":-1452.0,"DAYS_REGISTRATION":-339.0,"DAYS_ID_PUBLISH":-3348,"OWN_CAR_AGE":7.0,"FLAG_MOBIL":1,"FLAG_EMP_PHONE":1,"FLAG_WORK_PHONE":0,"FLAG_CONT_MOBILE":1,"FLAG_PHONE":0,"FLAG_EMAIL":0,"CNT_FAM_MEMBERS":3.0,"REGION_RATING_CLIENT":1,"REGION_RATING_CLIENT_W_CITY":1,"HOUR_APPR_PROCESS_START":13,"REG_REGION_NOT_LIVE_REGION":0,"REG_REGION_NOT_WORK_REGION":0,"LIVE_REGION_NOT_WORK_REGION":0,"REG_CITY_NOT_LIVE_CITY":0,"REG_CITY_NOT_WORK_CITY":0,"LIVE_CITY_NOT_WORK_CITY":0,"EXT_SOURCE_1":0.5401316641,"EXT_SOURCE_2":0.5929868573,"EXT_SOURCE_3":0.4347332488,"APARTMENTS_AVG":0.0959,"BASEMENTAREA_AVG":0.0529,"YEARS_BEGINEXPLUATATION_AVG":0.9851,"YEARS_BUILD_AVG":0.796,"COMMONAREA_AVG":0.0605,"ELEVATORS_AVG":0.08,"ENTRANCES_AVG":0.0345,"FLOORSMAX_AVG":0.2917,"FLOORSMIN_AVG":0.3333,"LANDAREA_AVG":0.013,"LIVINGAPARTMENTS_AVG":0.0773,"LIVINGAREA_AVG":0.0549,"NONLIVINGAPARTMENTS_AVG":0.0039,"NONLIVINGAREA_AVG":0.0098,"APARTMENTS_MODE":0.0924,"BASEMENTAREA_MODE":0.0538,"YEARS_BEGINEXPLUATATION_MODE":0.9851,"YEARS_BUILD_MODE":0.804,"COMMONAREA_MODE":0.0497,"ELEVATORS_MODE":0.0806,"ENTRANCES_MODE":0.0345,"FLOORSMAX_MODE":0.2917,"FLOORSMIN_MODE":0.3333,"LANDAREA_MODE":0.0128,"LIVINGAPARTMENTS_MODE":0.079,"LIVINGAREA_MODE":0.0554,"NONLIVINGAPARTMENTS_MODE":0.0,"NONLIVINGAREA_MODE":0.0,"APARTMENTS_MEDI":0.0968,"BASEMENTAREA_MEDI":0.0529,"YEARS_BEGINEXPLUATATION_MEDI":0.9851,"YEARS_BUILD_MEDI":0.7987,"COMMONAREA_MEDI":0.0608,"ELEVATORS_MEDI":0.08,"ENTRANCES_MEDI":0.0345,"FLOORSMAX_MEDI":0.2917,"FLOORSMIN_MEDI":0.3333,"LANDAREA_MEDI":0.0132,"LIVINGAPARTMENTS_MEDI":0.0787,"LIVINGAREA_MEDI":0.0558,"NONLIVINGAPARTMENTS_MEDI":0.0039,"NONLIVINGAREA_MEDI":0.01,"TOTALAREA_MODE":0.0714,"OBS_30_CNT_SOCIAL_CIRCLE":2.0,"DEF_30_CNT_SOCIAL_CIRCLE":0.0,"OBS_60_CNT_SOCIAL_CIRCLE":2.0,"DEF_60_CNT_SOCIAL_CIRCLE":0.0,"DAYS_LAST_PHONE_CHANGE":-262.0,"FLAG_DOCUMENT_2":0,"FLAG_DOCUMENT_3":1,"FLAG_DOCUMENT_4":0,"FLAG_DOCUMENT_5":0,"FLAG_DOCUMENT_6":0,"FLAG_DOCUMENT_7":0,"FLAG_DOCUMENT_8":0,"FLAG_DOCUMENT_9":0,"FLAG_DOCUMENT_10":0,"FLAG_DOCUMENT_11":0,"FLAG_DOCUMENT_12":0,"FLAG_DOCUMENT_13":0,"FLAG_DOCUMENT_14":0,"FLAG_DOCUMENT_15":0,"FLAG_DOCUMENT_16":0,"FLAG_DOCUMENT_17":0,"FLAG_DOCUMENT_18":0,"FLAG_DOCUMENT_19":0,"FLAG_DOCUMENT_20":0,"FLAG_DOCUMENT_21":0,"AMT_REQ_CREDIT_BUREAU_HOUR":0.0,"AMT_REQ_CREDIT_BUREAU_DAY":0.0,"AMT_REQ_CREDIT_BUREAU_WEEK":0.0,"AMT_REQ_CREDIT_BUREAU_MON":0.0,"AMT_REQ_CREDIT_BUREAU_QRT":0.0,"AMT_REQ_CREDIT_BUREAU_YEAR":3.0,"CODE_GENDER_F":1,"CODE_GENDER_M":0,"NAME_TYPE_SUITE_Children":0,"NAME_TYPE_SUITE_Family":0,"NAME_TYPE_SUITE_Group of people":0,"NAME_TYPE_SUITE_Other_A":0,"NAME_TYPE_SUITE_Other_B":0,"NAME_TYPE_SUITE_Spouse, partner":0,"NAME_TYPE_SUITE_Unaccompanied":1,"NAME_INCOME_TYPE_Businessman":0,"NAME_INCOME_TYPE_Commercial associate":0,"NAME_INCOME_TYPE_Pensioner":0,"NAME_INCOME_TYPE_State servant":0,"NAME_INCOME_TYPE_Student":0,"NAME_INCOME_TYPE_Unemployed":0,"NAME_INCOME_TYPE_Working":1,"NAME_EDUCATION_TYPE_Academic degree":0,"NAME_EDUCATION_TYPE_Higher education":0,"NAME_EDUCATION_TYPE_Incomplete higher":0,"NAME_EDUCATION_TYPE_Lower secondary":0,"NAME_EDUCATION_TYPE_Secondary \/ secondary special":1,"NAME_FAMILY_STATUS_Civil marriage":0,"NAME_FAMILY_STATUS_Married":1,"NAME_FAMILY_STATUS_Separated":0,"NAME_FAMILY_STATUS_Single \/ not married":0,"NAME_FAMILY_STATUS_Widow":0,"NAME_HOUSING_TYPE_Co-op apartment":0,"NAME_HOUSING_TYPE_House \/ apartment":1,"NAME_HOUSING_TYPE_Municipal apartment":0,"NAME_HOUSING_TYPE_Office apartment":0,"NAME_HOUSING_TYPE_Rented apartment":0,"NAME_HOUSING_TYPE_With parents":0,"OCCUPATION_TYPE_Accountants":0,"OCCUPATION_TYPE_Cleaning staff":0,"OCCUPATION_TYPE_Cooking staff":0,"OCCUPATION_TYPE_Core staff":0,"OCCUPATION_TYPE_Drivers":0,"OCCUPATION_TYPE_HR staff":0,"OCCUPATION_TYPE_High skill tech staff":0,"OCCUPATION_TYPE_IT staff":0,"OCCUPATION_TYPE_Laborers":0,"OCCUPATION_TYPE_Low-skill Laborers":0,"OCCUPATION_TYPE_Managers":0,"OCCUPATION_TYPE_Medicine staff":0,"OCCUPATION_TYPE_Private service staff":0,"OCCUPATION_TYPE_Realty agents":0,"OCCUPATION_TYPE_Sales staff":0,"OCCUPATION_TYPE_Secretaries":0,"OCCUPATION_TYPE_Security staff":0,"OCCUPATION_TYPE_Waiters\/barmen staff":0,"WEEKDAY_APPR_PROCESS_START_FRIDAY":0,"WEEKDAY_APPR_PROCESS_START_MONDAY":0,"WEEKDAY_APPR_PROCESS_START_SATURDAY":1,"WEEKDAY_APPR_PROCESS_START_SUNDAY":0,"WEEKDAY_APPR_PROCESS_START_THURSDAY":0,"WEEKDAY_APPR_PROCESS_START_TUESDAY":0,"WEEKDAY_APPR_PROCESS_START_WEDNESDAY":0,"ORGANIZATION_TYPE_Advertising":0,"ORGANIZATION_TYPE_Agriculture":0,"ORGANIZATION_TYPE_Bank":0,"ORGANIZATION_TYPE_Business Entity Type 1":0,"ORGANIZATION_TYPE_Business Entity Type 2":0,"ORGANIZATION_TYPE_Business Entity Type 3":1,"ORGANIZATION_TYPE_Cleaning":0,"ORGANIZATION_TYPE_Construction":0,"ORGANIZATION_TYPE_Culture":0,"ORGANIZATION_TYPE_Electricity":0,"ORGANIZATION_TYPE_Emergency":0,"ORGANIZATION_TYPE_Government":0,"ORGANIZATION_TYPE_Hotel":0,"ORGANIZATION_TYPE_Housing":0,"ORGANIZATION_TYPE_Industry: type 1":0,"ORGANIZATION_TYPE_Industry: type 10":0,"ORGANIZATION_TYPE_Industry: type 11":0,"ORGANIZATION_TYPE_Industry: type 12":0,"ORGANIZATION_TYPE_Industry: type 13":0,"ORGANIZATION_TYPE_Industry: type 2":0,"ORGANIZATION_TYPE_Industry: type 3":0,"ORGANIZATION_TYPE_Industry: type 4":0,"ORGANIZATION_TYPE_Industry: type 5":0,"ORGANIZATION_TYPE_Industry: type 6":0,"ORGANIZATION_TYPE_Industry: type 7":0,"ORGANIZATION_TYPE_Industry: type 8":0,"ORGANIZATION_TYPE_Industry: type 9":0,"ORGANIZATION_TYPE_Insurance":0,"ORGANIZATION_TYPE_Kindergarten":0,"ORGANIZATION_TYPE_Legal Services":0,"ORGANIZATION_TYPE_Medicine":0,"ORGANIZATION_TYPE_Military":0,"ORGANIZATION_TYPE_Mobile":0,"ORGANIZATION_TYPE_Other":0,"ORGANIZATION_TYPE_Police":0,"ORGANIZATION_TYPE_Postal":0,"ORGANIZATION_TYPE_Realtor":0,"ORGANIZATION_TYPE_Religion":0,"ORGANIZATION_TYPE_Restaurant":0,"ORGANIZATION_TYPE_School":0,"ORGANIZATION_TYPE_Security":0,"ORGANIZATION_TYPE_Security Ministries":0,"ORGANIZATION_TYPE_Self-employed":0,"ORGANIZATION_TYPE_Services":0,"ORGANIZATION_TYPE_Telecom":0,"ORGANIZATION_TYPE_Trade: type 1":0,"ORGANIZATION_TYPE_Trade: type 2":0,"ORGANIZATION_TYPE_Trade: type 3":0,"ORGANIZATION_TYPE_Trade: type 4":0,"ORGANIZATION_TYPE_Trade: type 5":0,"ORGANIZATION_TYPE_Trade: type 6":0,"ORGANIZATION_TYPE_Trade: type 7":0,"ORGANIZATION_TYPE_Transport: type 1":0,"ORGANIZATION_TYPE_Transport: type 2":0,"ORGANIZATION_TYPE_Transport: type 3":0,"ORGANIZATION_TYPE_Transport: type 4":0,"ORGANIZATION_TYPE_University":0,"ORGANIZATION_TYPE_XNA":0,"FONDKAPREMONT_MODE_not specified":0,"FONDKAPREMONT_MODE_org spec account":0,"FONDKAPREMONT_MODE_reg oper account":1,"FONDKAPREMONT_MODE_reg oper spec account":0,"HOUSETYPE_MODE_block of flats":1,"HOUSETYPE_MODE_specific housing":0,"HOUSETYPE_MODE_terraced house":0,"WALLSMATERIAL_MODE_Block":1,"WALLSMATERIAL_MODE_Mixed":0,"WALLSMATERIAL_MODE_Monolithic":0,"WALLSMATERIAL_MODE_Others":0,"WALLSMATERIAL_MODE_Panel":0,"WALLSMATERIAL_MODE_Stone, brick":0,"WALLSMATERIAL_MODE_Wooden":0,"EMERGENCYSTATE_MODE_No":1,"EMERGENCYSTATE_MODE_Yes":0,"DAYS_EMPLOYED_ANOM":0,"CREDIT_INCOME_PERCENT":4.6153846154,"ANNUITY_INCOME_PERCENT":0.1494423077,"CREDIT_TERM":0.0323791667,"DAYS_EMPLOYED_PERCENT":-0.1361590398}
#     response = client.post("/predict/", json=sample_data)
#     assert response.status_code == 200
#     json_response = response.json()
#     assert "Classe prédite pour ces données" in json_response
#     assert "Prédiction de la TARGET 0" in json_response
#     assert "Prédiction de la TARGET 1" in json_response

# Test du endpoint de prédiction avec des données incorrectes
def test_predict_invalid():
    response = client.post("/predict/", json={"wrong_feature": "invalid"})
    assert response.status_code == 500

# Test de chargement du modèle
def test_load_model():
    model = load_model()
    assert model is not None

# # Test d'encodage des catégories
# def test_encode_categories():
#     sample_data = {"feature1": 1.0, "feature2": 0.5, "feature3": "category1"}
#     encoded_data = encode_categories(sample_data)
#     assert isinstance(encoded_data, pd.DataFrame)

# # Test de prédiction de probabilité
# def test_predict():
#     model = load_model()
#     sample_data = {"feature1": 1.0, "feature2": 0.5, "feature3": "category1"}
#     prediction = predict(model, sample_data)
#     assert prediction is not None

# # Test de prédiction de classe
# def test_predict_class():
#     model = load_model()
#     sample_data = {"feature1": 1.0, "feature2": 0.5, "feature3": "category1"}
#     class_prediction = predict_class(model, sample_data)
#     assert class_prediction is not None
