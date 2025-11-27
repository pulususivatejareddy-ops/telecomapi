import streamlit as st
import pandas as pd
import requests

# Streamlit UI for Customer Churn Prediction
st.title("Telecom Customer Churn Prediction App")
st.write("This tool predicts customer churn risk based on their details. Enter the required information below.")

# Collect user input based on dataset columns
CustomerID = st.number_input("Customer ID", min_value=10000000, max_value=99999999)
SeniorCitizen = st.selectbox("Senior citizen", ["Yes", "No"])
Partner = st.selectbox("Does the customer have a partner?", ["Yes", "No"])
Dependents = st.selectbox("Does the customer have dependents?", ["Yes", "No"])
PhoneService = st.selectbox("Does the customer have phone service?", ["Yes", "No"])
InternetService = st.selectbox("Type of Internet Service", ["DSL", "Fiber optic", "No"])
Contract = st.selectbox("Type of Contract", ["Month-to-month", "One year", "Two year"])
PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
tenure = st.number_input("Tenure (Months with the company)", min_value=0, value=12)
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0, value=600.0)

# Convert categorical inputs to match model training
customer_data = {
    'SeniorCitizen': 1 if SeniorCitizen == "Yes" else 0,
    'Partner':Partner,
    'Dependents': Dependents,
    'tenure': tenure,
    'PhoneService': PhoneService,
    'InternetService': InternetService,
    'Contract': Contract,
    'PaymentMethod': PaymentMethod,
    'MonthlyCharges': MonthlyCharges,
    'TotalCharges': TotalCharges
}


if st.button("Predict", type='primary'):
    response = requests.post("https://pulususivatejareddy123-telecomapi.hf.space/v1/customer", json=customer_data)    # enter user name and space name before running the cell
    if response.status_code == 200:
        result = response.json()
        churn_prediction = result["Prediction"]  # Extract only the value
        st.write(f"Based on the information provided, the customer with ID {CustomerID} is likely to {churn_prediction}.")
    else:
        st.error("Error in API request")

# Batch Prediction
st.subheader("Batch Prediction")

file = st.file_uploader("Upload CSV file", type=["csv"])
if file is not None:
    if st.button("Predict for Batch", type='primary'):
        response = requests.post("https://pulususivatejareddy123-telecomapi.hf.space/v1/customerbatch", files={"file": file})    # enter user name and space name before running the cell
        if response.status_code == 200:
            result = response.json()
            st.header("Batch Prediction Results")
            st.write(result)
        else:
            st.error("Error in API request")
