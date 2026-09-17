# life-expectancy-analysis
data cleaning, hypothesis testing, and regression modeling on WHO Life Expectancy data

# Life Expectancy Analysis

A data science project analyzing the WHO Life Expectancy dataset - covering data cleaning, hypothesis testing, feature selection and regression modelling.

## Dataset
Source: [Life Expectancy (WHO)(https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who) by KUMARRAJARSHI on Kaggle

## What This Project Does
- Cleans and handles missing data, including a hidden data quality issue (implausible 0.0 values in HDI-linked columns) discovered mid-analysis.
- Tests whether development status (Developed vs Developing) has a statistically significant relationship with life expectancy (t-test)
- Identifies the strongest predictors of life expectancy using correlation analysis
- Builds a linear regression model to predict life expectancy from health, education and economic factors.

## Key Findings
- Development status has a statistically significant effect on life expectancy (p < 0.001)
- Schooling, Incoome composition of resources, and Adult Mortality are the strongest predictors
- The regression model explains ~83% of the variation in life expectancy (R^2 = 0.83, RMSE = 3.8 years)
- Correcting a hidden data quality issue improved the model's performance measurably (R^2 rose from 0.80 to 0.83)

## Tools Used
Python, pandas, numpy, scikit-learn, matplotlib, seaborn, scipy

## Note
This project focuses on demonstrating a complete analysis from raw data to a working model - not on producing a tool meant for real world prediction.
