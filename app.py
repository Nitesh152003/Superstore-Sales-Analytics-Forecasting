import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import numpy as np

st.set_page_config(page_title="Superstore Sales Forecast", layout="wide")

st.title("📊 Superstore Sales Analytics & Forecasting")
st.write("Analyze historical sales data and forecast sales for the next 7 days.")

# Load data
df = pd.read_csv("data/train.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df = df.drop_duplicates()
df = df.sort_values('Order Date')

# Daily aggregation
daily_sales = df.groupby('Order Date')['Sales'].sum().reset_index()
daily_sales = daily_sales.set_index('Order Date')
daily_sales = daily_sales.asfreq('D')
daily_sales['Sales'] = daily_sales['Sales'].fillna(0)

st.subheader("📈 Daily Sales Trend")
fig, ax = plt.subplots(figsize=(10,4))
ax.plot(daily_sales.index, daily_sales['Sales'])
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
st.pyplot(fig)

# Forecast section
st.subheader("🔮 Sales Forecast (Next 7 Days)")

train = daily_sales[:-7]

model = ARIMA(train['Sales'], order=(5,1,0))
model_fit = model.fit()

forecast = model_fit.forecast(steps=7)

future_dates = pd.date_range(
    start=train.index[-1] + pd.Timedelta(days=1),
    periods=7,
    freq='D'
)

forecast_df = pd.DataFrame({
    'Date': future_dates,
    'Predicted Sales': forecast.values
})

st.dataframe(forecast_df)

# Plot forecast
fig2, ax2 = plt.subplots(figsize=(10,4))
ax2.plot(train.index, train['Sales'], label="Historical Sales")
ax2.plot(forecast_df['Date'], forecast_df['Predicted Sales'], marker='o', label="Forecast")
ax2.legend()
st.pyplot(fig2)

st.success("Forecast generated successfully!")
