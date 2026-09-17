import streamlit as st
import joblib
import numpy as np

# Loading the trained model
model = joblib.load('life_expectancy_model.pkl')

st.title("Life Expectancy Predictor")
st.write("Enter the values below to get a predicted life expectancy.")

# Input the fields matching the 9 features used to train the model in the same order used during training.
schooling = st.slider("Schooling (years)", 0.0, 20.0, 10.0)
income_comp = st.slider("Income Composition of Resources", 0.0, 1.0, 0.5)
adult_mortality = st.slider("Adult Mortality (per 1000)", 0.0, 700.0, 150.0)
hiv_aids = st.slider("HIV/AIDS (deaths per 1000)", 0.0, 50.0, 0.5)
bmi = st.slider("BMI", 0.0, 80.0, 40.0)
gdp = st.number_input("GDP", 0.0, 150000.0, 5000.0)
diphtheria = st.slider("Diphtheria Immunization (%)", 0.0, 100.0, 80.0)
thinness = st.slider("Thinness 5-9 years (%)", 0.0, 30.0, 5.0)
under_five_deaths = st.slider("Under-five Deaths (per 1000)", 0.0, 300.0, 20.0)

if st.button("Predict Life Expectancy"):
    input_data = np.array([[
    	schooling, 
    	income_comp, 	
    	adult_mortality, 
    	hiv_aids, 	
    	bmi, 
    	gdp, 
    	diphtheria, 
    	thinness, 
    	under_five_deaths
    ]])
    
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Life Expectancy: {prediction[0]:.1f} years")



