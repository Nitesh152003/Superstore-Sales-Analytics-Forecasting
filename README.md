# 📊 Superstore Sales Analytics & Forecasting

## Project Overview
This project analyzes historical retail sales data to uncover business insights
and forecasts sales for the next 7 days using time-series analysis.

## Objectives
- Perform exploratory data analysis (EDA) to understand sales trends
- Identify key business insights from historical data
- Build a time-series model to predict short-term sales
- Deploy the solution as an interactive Streamlit application

## Dataset
- Global Superstore sales dataset (4 years of data)
- Contains order, customer, shipping, and sales information
- Time-series data aggregated at a daily level

## Approach
1. Data cleaning and preprocessing
2. Exploratory Data Analysis (EDA)
3. Daily sales aggregation and time-series preparation
4. Sales forecasting using ARIMA
5. Deployment using Streamlit

## Key Insights
- Sales show noticeable fluctuations and seasonal patterns over time
- The Consumer segment contributes the highest share of total sales
- Standard Class shipping mode dominates order volume
- Forecasted sales provide actionable insights for short-term planning

## Forecasting
- Daily sales data used for time-series modeling
- ARIMA model applied to predict the next 7 days of sales
- Model evaluated using RMSE on recent data

## Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Statsmodels (ARIMA)
- Streamlit

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
