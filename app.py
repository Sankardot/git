import streamlit as st
import pickle
import numpy as np

# Load model
with open("house_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏠 House Price Prediction App")

# User Inputs
area = st.number_input("Enter Area (sq ft)")
bedrooms = st.number_input("Enter Bedrooms")
age = st.number_input("Enter Age of House")

if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, age]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Price: {prediction[0]:.2f} Lakhs")