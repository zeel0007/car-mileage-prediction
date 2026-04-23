import streamlit as st
import pickle
import os

model = pickle.load(open("final_model.pkl", "rb"))

d1 = {
    "Comprehensive": 0,
    "Third Party insurance": 1,
    "Zero Dep": 2,
    "Not Available": 3,
    "Third Party": 1
}
d2 = {"Petrol": 0, "Diesel": 1, "CNG": 2}
d3 = {"Manual": 0, "Automatic": 1}
d4 = {
    "First Owner": 1,
    "Second Owner": 2,
    "Third Owner": 3,
    "Fourth Owner": 4,
    "Fifth Owner": 5
}

st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")
st.title("🚗 Car Price Prediction App")

insurance_validity = st.selectbox("Insurance Validity", list(d1.keys()))
fuel_type = st.radio("Fuel Type", list(d2.keys()))
ownership = st.selectbox("Ownership", list(d4.keys()))
transmission = st.radio("Transmission Type", list(d3.keys()))
kms_driven = st.slider("KMs Driven", 0, 300000, 50000, 1000)

if st.button("Predict Price"):
    test = [[
        d1[insurance_validity],
        d2[fuel_type],
        int(kms_driven),
        d4[ownership],
        d3[transmission]
    ]]

    prediction = model.predict(test)[0]
    #st.write("Input sent to model:", test)
    st.success(f"Predicted Price: ₹ {prediction}")