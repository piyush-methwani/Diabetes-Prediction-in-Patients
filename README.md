# Diabetes-Prediction-in-Patients
This project is a machine learning-based web application that predicts whether a person is likely to have diabetes based on medical parameters. It uses a trained Decision Tree Classifier and is deployed with Streamlit for easy user interaction.

Features:
 Predicts diabetes based on:
 1. Number of Pregnancies
 2. Glucose Level
 3. Blood Pressure
 4. Skin Thickness
 5. Insulin Level
 6. BMI
 7. Diabetes Pedigree Function
 8. Age

Built using:

1. Python
2. Pandas, NumPy, Scikit-learn
3. Streamlit for the front-end
4. Simple and intuitive interface
5. Lightweight and easy to deploy

Diabetes-Prediction

┣ diabetes.csv----------------------------------# Dataset

┣ Prediction of Diabetes.ipynb------------------# Model training and exploration

┣ model_pipeline.pkl----------------------------# Saved ML model

┣ app.py----------------------------------------# Streamlit web app

┗ README.md-------------------------------------# Project overview

Dataset

The dataset used is the Pima Indians Diabetes Database. It includes several medical predictor variables and one target variable (Outcome), indicating whether the patient has diabetes.

Model
1.  Algorithm: Decision Tree Classifier

2. Trained using Scikit-learn

3. Saved with pickle for reuse in the web app

How to Run
1. Clone the repository:

git clone https://github.com/your-username/diabetes-prediction.git
cd diabetes-prediction

2. Install required packages:

pip install -r requirements.txt

3. Run the Streamlit app:

streamlit run app.py

Author:

Developed by Piyush Methwani

Feel free to connect on LinkedIn 
