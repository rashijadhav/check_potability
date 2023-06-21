import streamlit as st
import pandas as pd
import joblib
model = joblib.load("model_water.pkl")
def predict_potability(inputs):
    return model.predict(inputs)
def main():
    st.title("Water Potability Predictor")
    st.write("Enter the water parameters to predict its potability.")

    # Create input fields for the user
    ph = st.number_input("pH")
    hardness = st.number_input("Hardness")
    solids = st.number_input("Solids")
    chloramines = st.number_input("Chloramines")
    sulfate = st.number_input("Sulfate")
    conductivity = st.number_input("Conductivity")
    organic_carbon = st.number_input("Organic Carbon")
    trihalomethanes = st.number_input("Trihalomethanes")
    turbidity = st.number_input("Turbidity")

    # Create a DataFrame from the user inputs
    user_data = pd.DataFrame({
        'ph': [ph],
        'Hardness': [hardness],
        'Solids': [solids],
        'Chloramines': [chloramines],
        'Sulfate': [sulfate],
        'Conductivity': [conductivity],
        'Organic_carbon': [organic_carbon],
        'Trihalomethanes': [trihalomethanes],
        'Turbidity': [turbidity]
    })

    # Make a prediction using the user inputs
    if st.button("Predict"):
        prediction = predict_potability(user_data)
        result = "Potable" if prediction[0] == 1 else "Not Potable"
        st.success(f"The water is predicted to be {result}.")

if __name__ == '__main__':
    main()
