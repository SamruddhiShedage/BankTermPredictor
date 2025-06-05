import streamlit as st
import pandas as pd
import joblib
import xgboost as xgb

# Load the trained model
model = joblib.load("xgboost_bank_model.pkl")

st.set_page_config(page_title="Bank Marketing Predictor", layout="wide")

# Sidebar layout
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1170/1170576.png", width=80)
    st.title("📋 Input Features")
    st.markdown("Fill out the form to get a prediction.")

# Load sample data
sample_df = pd.read_csv("./bank-additional-full.csv", sep=';')
categorical_cols = sample_df.select_dtypes(include='object').columns.tolist()

# Input form
st.markdown("## 🎯 Term Deposit Subscription Prediction")
user_input = {}
for col in sample_df.columns:
    if col == 'y':
        continue
    elif col in categorical_cols:
        options = sample_df[col].astype('category').cat.categories.tolist()
        user_input[col] = st.sidebar.selectbox(f"{col.capitalize()}", options)
    else:
        user_input[col] = st.sidebar.number_input(f"{col.capitalize()}", value=float(sample_df[col].mean()))

if st.sidebar.button("🔍 Predict"):
    input_df = pd.DataFrame([user_input])

    # Ensure all expected columns are present
    missing_cols = set(sample_df.drop('y', axis=1).columns) - set(input_df.columns)
    for col in missing_cols:
        if col in categorical_cols:
            input_df[col] = sample_df[col].mode()[0]
        else:
            input_df[col] = sample_df[col].mean()

    input_df = input_df[sample_df.drop('y', axis=1).columns]

    # Convert only if column exists in input_df
    for col in categorical_cols:
        if col in input_df.columns:
            input_df[col] = input_df[col].astype('category')

    prediction = model.predict(input_df)[0]
    prediction_proba = model.predict_proba(input_df)[0][1]

    st.markdown("---")
    st.markdown("### 🧠 Prediction Result")
    if prediction == 1:
        st.success(f"✅ The customer is **likely to subscribe**.\n\n**Confidence:** {prediction_proba:.2%}")
    else:
        st.warning(f"⚠️ The customer is **unlikely to subscribe**.\n\n**Confidence:** {1 - prediction_proba:.2%}")