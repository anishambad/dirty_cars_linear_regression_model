import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Load scaler + model
# -----------------------------
with open("linear_model.pkl", "rb") as f:
    scaler, model = pickle.load(f)

st.title("Car Resale Value Predictor")

# -----------------------------
# User Inputs
# -----------------------------
year = st.number_input("Year of Manufacture", min_value=1990, max_value=2026, value=2015)
mileage = st.number_input("Mileage (km)", min_value=0, max_value=300000, value=50000)
owner_count = st.number_input("Number of Owners", min_value=1, max_value=5, value=1)

fuel_type = st.selectbox("Fuel Type", ["petrol", "gas", "electric", "unknown"])
car_model = st.selectbox("Car Model", ["honda", "toyota", "bmw"])  # baseline is BMW
transmission = st.selectbox("Transmission", ["manual", "automatic", "unknown"])  # baseline is automatic

# -----------------------------
# Build Input Row (exact order from training)
# -----------------------------
input_data = pd.DataFrame([[
    year,
    mileage,
    owner_count,
    1 if transmission=="manual" else 0,
    1 if transmission=="unknown" else 0,
    1 if car_model=="honda" else 0,
    1 if car_model=="toyota" else 0,
    1 if fuel_type=="electric" else 0,
    1 if fuel_type=="gas" else 0,
    1 if fuel_type=="petrol" else 0,
    1 if fuel_type=="unknown" else 0
]], columns=[
    'year','mileage','owner_count',
    'transmission_manual','transmission_unknown',
    'car_model_honda','car_model_toyota',
    'fuel_type_electric','fuel_type_gas','fuel_type_petrol','fuel_type_unknown'
])

# -----------------------------
# Scale numeric features
# -----------------------------
num_cols = ['year','mileage','owner_count']
input_data[num_cols] = scaler.transform(input_data[num_cols])

st.write("Input Data (scaled):", input_data)

# -----------------------------
# Prediction
# -----------------------------
prediction = model.predict(input_data)[0]
st.subheader(f"Predicted Resale Value: ₹{prediction:,.2f}")
