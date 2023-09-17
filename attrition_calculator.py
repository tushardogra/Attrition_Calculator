import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

model = joblib.load('linear_regression_model.pkl')

st.title("Attrition Rate Calculator")

label_encoder_hometown = LabelEncoder()
label_encoder_cb = LabelEncoder()
label_encoder_unit = LabelEncoder()
label_encoder_decision_skill = LabelEncoder()

compensation_mapping = {
    "type0": 0,
    "type1": 1,
    "type2": 2,
    "type3": 3,
    "type4": 4
}

hometown_mapping = {
    "Franklin": 0,
    "Springfield": 1,
    "Clinton": 2,
    "Lebanon": 3,
    "Washington": 4,
    "Frankfort": 5,
    "Hudson": 6,
    "Archer": 7,
    "Springville": 8,
    "Fairmount": 9
}

unit_mapping = {
    "R&D": 0,
    "IT": 1,
    "HR": 2,
    "Sales": 3,
    "Finance": 4,
}

decision_skill_mapping = {
    "Analytical": 0,
    "Conceptual": 1,
    "Behavioral": 2,
    "Directive": 3,
}

gender = st.radio("Gender:", ["Male", "Female"])
age = st.number_input("Age:")
relationship_status = st.selectbox("Relationship Status:", ["Single", "Married"])
hometown = st.selectbox("Hometown:", list(hometown_mapping.keys()))
unit = st.selectbox("Unit:", list(unit_mapping.keys()))
decision_skill_possess = st.selectbox("Decision Skill Possess:", list(decision_skill_mapping.keys()))
time_of_service = st.number_input("Time of Service:")
time_since_promotion = st.number_input("Time Since Promotion:")
growth_rate = st.number_input("Growth Rate:")
travel_rate = st.number_input("Travel Rate:")
post_level = st.number_input("Post Level:")
pay_scale = st.number_input("Pay Scale:")
compensation_and_benefits = st.selectbox("Compensation and Benefits:", list(compensation_mapping.keys()))
work_life_balance = st.number_input("Work-Life Balance:")

input_data = {
    'Gender': [1 if gender == 'Male' else 0],
    'Age': [age],
    'Relationship_Status': [1 if relationship_status == "Married" else 0],
    'Hometown': [hometown_mapping[hometown]],
    'Unit': [unit_mapping[unit]],
    'Decision_skill_possess': [decision_skill_mapping[decision_skill_possess]],
    'Time_of_service': [time_of_service],
    'Time_since_promotion': [time_since_promotion],
    'growth_rate': [growth_rate],
    'Travel_Rate': [travel_rate],
    'Post_Level': [post_level],
    'Pay_Scale': [pay_scale],
    'Compensation_and_Benefits': [compensation_mapping[compensation_and_benefits]],
    'Work_Life_balance': [work_life_balance]
}

input_df = pd.DataFrame(input_data)

if st.button("Calculate Attrition Rate"):
    try:
        prediction = model.predict(input_df)

        st.success(f"Predicted Attrition Rate: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
