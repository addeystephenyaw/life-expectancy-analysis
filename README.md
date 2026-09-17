# life-expectancy-analysis
data cleaning, hypothesis testing, and regression modeling on WHO Life Expectancy data

# Life Expectancy Analysis

A data science project analyzing the WHO Life Expectancy dataset through data cleaning, statistical analysis, hypothesis testing, feature selection and regression modelling. The main objective was to investigate factors associated with life expectancy and build a model capable estimating life expectancy from selected health, education and economic indicators. 
An interactive Streamlit application was later developed to demonstrate the trained model and allow users to generate life-expectancy predictions.

## Dataset
Source: [Life Expectancy (WHO)(https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who) by KUMARRAJARSHI on Kaggle.
The dataset contains health, demographic, education, and economic indicators for different countries.

## What This Project Does
- Cleans and handles missing data, including a hidden data quality issue (implausible 0.0 values in HDI-linked columns) discovered mid-analysis.
- Tests whether development status (Developed vs Developing) has a statistically significant relationship with life expectancy (t-test)
- Identifies the strongest predictors of life expectancy using correlation analysis
- Builds a linear regression model to predict life expectancy from health, education and economic factors.
- Provides an interactive Streamlit application for making predictions.

## Key Findings
- Development status has a statistically significant effect on life expectancy (p < 0.001)
- Schooling, Incoome composition of resources, and Adult Mortality are the strongest predictors
- The regression model explains ~83% of the variation in life expectancy (R^2 = 0.83, RMSE = 3.8 years)
- Correcting a hidden data quality issue improved the model's performance measurably (R^2 rose from 0.80 to 0.83)

## Interactive Prediction App
The project includes a Streamlit web application that allows users to enter values for selected factors and receive an estimated life expectancy.

### Input Factors
The application uses the following factors:
- Schooling (years)
- Income Composition of Resources
- Adult Mortality (per 1000)
- HIV/AIDS (deaths per 1000)
- BMI
- GDP
- Diphtheria Immunization
- Thinnness 5-9 years (%)
- Under-five Deaths (per 1000)

## Project Files
- 'Life Expectancy Analysis.ipynb' - Data cleaning, exploration, statistical analysis and model development
- 'Life Expectancy Data.csv' - Dataset used for the analysis
- 'life_expectancy_model.pkl' - saved trained prediction model
- 'app.py' - Streamlit application for interactive predictions.
- 'requirements.txt' - Python packages required to run the project.

## Tools Used
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, SciPy, Streamlit, Joblib

## Note
This project is primarily an academic data science project demonstrating the complete process from raw data to data analysis, statistical modelling, and an interactive prediction application.
The Streamlit application is intended for educational and demonstration purposes. Its predictions should not be considered a reliable tool for real-world medical or demographic decision making.
