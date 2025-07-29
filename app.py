import numpy as np
import pickle
import streamlit as st

# Load the trained Decision Tree model
pickle_in = open("model_pipeline.pkl", "rb")
classifier = pickle.load(pickle_in)

# Prediction function
def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    # Convert inputs to float
    inputs = np.array([[float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                        float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]])
    prediction = classifier.predict(inputs)
    return prediction

# Main GUI
def main():
    st.markdown("""
       
    """, unsafe_allow_html=True)

    html_temp = """
   
    <h1> Diabetes Prediction in Patient  </h1>
    <h7>by Piyush Methwani </h7>

    <br>
    <br>
  
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Input fields
    Pregnancies = st.text_input("Pregnancies")
    Glucose = st.text_input("Glucose")
    BloodPressure = st.text_input("BloodPressure")
    SkinThickness = st.text_input("SkinThickness")
    Insulin = st.text_input("Insulin")
    BMI = st.text_input("BMI")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
    Age = st.text_input("Age")

    result = ""
    if st.button("Predict diabetes"):
        try:
            result = predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)

            if result == 0:
                st.success('Person may NOT be suffering from Diabetes')
            elif result == 1:
                st.success(' Person may be suffering from Diabetes')
            else:
                st.warning("Unexpected result from the model.")
        except ValueError:
            st.error("Please enter valid numeric inputs.")

if __name__ == '__main__':
    main()
