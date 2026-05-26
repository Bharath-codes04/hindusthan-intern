import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("random_forest_model.pkl", "rb"))

st.title("Titanic Survival Prediction")

st.write("Ensemble Learning using Random Forest")

pclass = st.selectbox("Passenger Class", [1, 2, 3])

sex = st.selectbox("Gender", ["Male", "Female"])

age = st.slider("Age", 1, 80, 25)

fare = st.number_input("Fare", 0.0, 500.0, 50.0)

if sex == "Male":
    sex = 1
else:
    sex = 0

if st.button("Predict"):

    input_data = np.array([[pclass, sex, age, fare]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Passenger Survived")
    else:
        st.error("Passenger Did Not Survive")