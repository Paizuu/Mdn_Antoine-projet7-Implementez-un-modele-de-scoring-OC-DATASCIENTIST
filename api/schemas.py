# from pydantic import BaseModel
# from typing import Optional

# class ClientData(BaseModel):
#     # Colonnes numériques principales
#     REG_REGION_NOT_LIVE_REGION: int
#     NAME_CONTRACT_TYPE: int
#     FLAG_OWN_CAR: int
#     FLAG_OWN_REALTY: int
#     CNT_CHILDREN: int
#     AMT_INCOME_TOTAL: float
#     AMT_CREDIT: float
#     AMT_ANNUITY: float
#     AMT_GOODS_PRICE: float
#     REGION_POPULATION_RELATIVE: float
#     DAYS_BIRTH: int
#     DAYS_EMPLOYED: float
#     DAYS_REGISTRATION: float
#     DAYS_ID_PUBLISH: int
#     OWN_CAR_AGE: Optional[float] = None
#     FLAG_MOBIL: int
#     FLAG_EMP_PHONE: int
#     FLAG_WORK_PHONE: int
#     FLAG_CONT_MOBILE: int
#     FLAG_PHONE: int
#     FLAG_EMAIL: int
#     CNT_FAM_MEMBERS: float
#     REGION_RATING_CLIENT: int
#     REGION_RATING_CLIENT_W_CITY: int
#     HOUR_APPR_PROCESS_START: int
#     #REG_REGION_NOT_LIVE_REGION: int
#     REG_REGION_NOT_WORK_REGION: int
#     LIVE_REGION_NOT_WORK_REGION: int
#     REG_CITY_NOT_LIVE_CITY: int
#     REG_CITY_NOT_WORK_CITY: int
#     LIVE_CITY_NOT_WORK_CITY: int
#     EXT_SOURCE_1: Optional[float] = None
#     EXT_SOURCE_2: Optional[float] = None
#     EXT_SOURCE_3: Optional[float] = None

#     # Colonnes OneHotEncodées
#     CODE_GENDER_F: int
#     CODE_GENDER_M: int
#     NAME_TYPE_SUITE_Children: int
#     NAME_TYPE_SUITE_Family: int
#     NAME_TYPE_SUITE_Group_of_people: int
#     NAME_TYPE_SUITE_Other_A: int
#     NAME_TYPE_SUITE_Other_B: int
#     NAME_TYPE_SUITE_Spouse_partner: int
#     NAME_TYPE_SUITE_Unaccompanied: int
#     NAME_INCOME_TYPE_Businessman: int
#     NAME_INCOME_TYPE_Commercial_associate: int
#     NAME_INCOME_TYPE_Pensioner: int
#     NAME_INCOME_TYPE_State_servant: int
#     NAME_INCOME_TYPE_Student: int
#     NAME_INCOME_TYPE_Unemployed: int
#     NAME_INCOME_TYPE_Working: int
#     NAME_EDUCATION_TYPE_Academic_degree: int
#     NAME_EDUCATION_TYPE_Higher_education: int
#     NAME_EDUCATION_TYPE_Incomplete_higher: int
#     NAME_EDUCATION_TYPE_Lower_secondary: int
#     NAME_EDUCATION_TYPE_Secondary_special: int
#     NAME_FAMILY_STATUS_Civil_marriage: int
#     NAME_FAMILY_STATUS_Married: int
#     NAME_FAMILY_STATUS_Separated: int
#     NAME_FAMILY_STATUS_Single: int
#     NAME_FAMILY_STATUS_Widow: int
#     NAME_HOUSING_TYPE_Co_op_apartment: int
#     NAME_HOUSING_TYPE_House_apartment: int
#     NAME_HOUSING_TYPE_Municipal_apartment: int
#     NAME_HOUSING_TYPE_Office_apartment: int
#     NAME_HOUSING_TYPE_Rented_apartment: int
#     NAME_HOUSING_TYPE_With_parents: int
#     OCCUPATION_TYPE_Accountants: int
#     OCCUPATION_TYPE_Cleaning_staff: int
#     OCCUPATION_TYPE_Cooking_staff: int
#     OCCUPATION_TYPE_Core_staff: int
#     OCCUPATION_TYPE_Drivers: int
#     OCCUPATION_TYPE_HR_staff: int
#     OCCUPATION_TYPE_High_skill_tech_staff: int
#     OCCUPATION_TYPE_IT_staff: int
#     OCCUPATION_TYPE_Laborers: int
#     OCCUPATION_TYPE_Low_skill_Laborers: int
#     OCCUPATION_TYPE_Managers: int
#     OCCUPATION_TYPE_Medicine_staff: int
#     OCCUPATION_TYPE_Private_service_staff: int
#     OCCUPATION_TYPE_Realty_agents: int
#     OCCUPATION_TYPE_Sales_staff: int
#     OCCUPATION_TYPE_Secretaries: int
#     OCCUPATION_TYPE_Security_staff: int
#     OCCUPATION_TYPE_Waiters_barmen_staff: int

#     # Variables métier crées
#     CREDIT_INCOME_PERCENT: float
#     ANNUITY_INCOME_PERCENT: float
#     CREDIT_TERM: float
#     DAYS_EMPLOYED_PERCENT: float
