import streamlit as st
import joblib
import numpy as np

model = joblib.load("phishing_model.pkl")

st.title("Phishing Website Detector")

url_length = st.number_input("URL Length")
dots = st.number_input("Number of Dots")
https = st.number_input("HTTPS (1 or 0)")

if st.button("Predict"):
    features = np.array([[url_length, dots, https]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠ Phishing Website")
    else:
        st.success("✅ Legitimate Website")