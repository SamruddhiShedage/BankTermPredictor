import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("xgboost_bank_model.pkl")

st.title("💼 Bank Term Deposit Subscription Predictor")
st.markdown("Predict whether a customer will subscribe to a term deposit based on their information.")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)
job = st.selectbox("Job", ["admin.", "blue-collar", "entrepreneur", "housemaid", "management", 
                           "retired", "self-employed", "services", "student", "technician", "unemployed", "unknown"])
marital = st.selectbox("Marital Status", ["married", "single", "divorced", "unknown"])
education = st.selectbox("Education", ["basic.4y", "basic.6y", "basic.9y", "high.school", 
                                       "illiterate", "professional.course", "university.degree", "unknown"])
default = st.selectbox("Has Credit in Default?", ["yes", "no"])
housing = st.selectbox("Has Housing Loan?", ["yes", "no"])
loan = st.selectbox("Has Personal Loan?", ["yes", "no"])
contact = st.selectbox("Contact Communication Type", ["cellular", "telephone"])
month = st.selectbox("Last Contact Month", ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])
day_of_week = st.selectbox("Day of Week", ["mon", "tue", "wed", "thu", "fri"])
duration = st.number_input("Last Contact Duration (seconds)", min_value=0, max_value=5000, value=100)
campaign = st.number_input("Number of Contacts in Campaign", min_value=1, max_value=50, value=1)
pdays = st.number_input("Days Since Last Contact", min_value=-1, max_value=999, value=999)
previous = st.number_input("Number of Previous Contacts", min_value=0, max_value=100, value=0)
poutcome = st.selectbox("Previous Outcome", ["failure", "nonexistent", "success"])
emp_var_rate = st.number_input("Employment Variation Rate", value=1.1)
cons_price_idx = st.number_input("Consumer Price Index", value=93.994)
cons_conf_idx = st.number_input("Consumer Confidence Index", value=-36.4)
euribor3m = st.number_input("Euribor 3 Month Rate", value=4.86)
nr_employed = st.number_input("Number of Employees", value=5191.0)

# Assemble into DataFrame
user_input = {
    'age': age,
    'job': job,
    'marital': marital,
    'education': education,
    'default': default,
    'housing': housing,
    'loan': loan,
    'contact': contact,
    'month': month,
    'day_of_week': day_of_week,
    'duration': duration,
    'campaign': campaign,
    'pdays': pdays,
    'previous': previous,
    'poutcome': poutcome,
    'emp.var.rate': emp_var_rate,
    'cons.price.idx': cons_price_idx,
    'cons.conf.idx': cons_conf_idx,
    'euribor3m': euribor3m,
    'nr.employed': nr_employed
}

input_df = pd.DataFrame([user_input])

# Convert object columns to categorical (required for XGBoost with enable_categorical=True)
for col in input_df.columns:
    if input_df[col].dtype == 'object':
        input_df[col] = input_df[col].astype('category')

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.success("🎉 The customer is **likely to subscribe** to the term deposit!")
        st.markdown("✅ Based on the provided data, the model predicts a **positive outcome**. Consider following up with the customer for final confirmation.")
    else:
        st.error("🚫 The customer is **unlikely to subscribe** to the term deposit.")
        st.markdown("❌ The model suggests a **low probability of subscription**. Consider reviewing the customer's profile or targeting a different offer.")


