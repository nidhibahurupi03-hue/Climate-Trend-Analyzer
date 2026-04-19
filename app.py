import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.data_loader import load_data
from src.preprocessing import clean_data
from src.anomaly_detection import detect_anomalies

st.title("🌍 Climate Trend Analyzer Dashboard")

# Load data
df = load_data("data/climate_data.csv")
df = clean_data(df)
df = detect_anomalies(df)

# Show dataset
st.subheader("📊 Dataset Preview")
st.write(df.head())

# ----------------------------
# Temperature Trend
# ----------------------------
st.subheader("🌡️ Temperature Trend")

fig1, ax1 = plt.subplots()
ax1.plot(df['date'], df['temperature'])
ax1.set_title("Temperature Trend")
st.pyplot(fig1)

# ----------------------------
# Rainfall Trend
# ----------------------------
st.subheader("🌧️ Rainfall Trend")

fig2, ax2 = plt.subplots()
ax2.plot(df['date'], df['rainfall'])
ax2.set_title("Rainfall Trend")
st.pyplot(fig2)

# ----------------------------
# Anomaly Detection
# ----------------------------
st.subheader("🚨 Anomaly Detection")

fig3, ax3 = plt.subplots()
ax3.plot(df['date'], df['temperature'], label="Normal")

anomalies = df[df['anomaly'] == True]
ax3.scatter(anomalies['date'], anomalies['temperature'], label="Anomaly")

ax3.legend()
st.pyplot(fig3)

# ----------------------------
# Show anomalies table
# ----------------------------
st.subheader("⚠️ Anomaly Records")
st.write(anomalies)