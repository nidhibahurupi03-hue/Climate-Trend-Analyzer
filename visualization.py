import matplotlib.pyplot as plt
import os

def plot_all(df):
    os.makedirs("outputs/plots", exist_ok=True)

    # 🌡️ Temperature
    plt.figure()
    plt.plot(df['date'], df['temperature'])
    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.savefig("outputs/plots/temp_trend.png")
    plt.close()

    # 🌧️ Rainfall
    plt.figure()
    plt.plot(df['date'], df['rainfall'])
    plt.title("Rainfall Trend")
    plt.xlabel("Date")
    plt.ylabel("Rainfall")
    plt.savefig("outputs/plots/rainfall_trend.png")
    plt.close()

    # 💧 Humidity
    plt.figure()
    plt.plot(df['date'], df['humidity'])
    plt.title("Humidity Trend")
    plt.xlabel("Date")
    plt.ylabel("Humidity")
    plt.savefig("outputs/plots/humidity_trend.png")
    plt.close()

    # 🚨 Anomaly Plot
    plt.figure()
    plt.plot(df['date'], df['temperature'], label="Normal")

    anomalies = df[df['anomaly'] == True]
    plt.scatter(anomalies['date'], anomalies['temperature'], label="Anomaly")

    plt.legend()
    plt.title("Temperature Anomaly Detection")
    plt.xlabel("Date")
    plt.ylabel("Temperature")

    plt.savefig("outputs/plots/anomaly_plot.png")
    plt.close()


def plot_forecast(forecast_df):
    os.makedirs("outputs/plots", exist_ok=True)

    plt.figure()
    plt.plot(forecast_df['date'], forecast_df['predicted_temp'])
    plt.title("Temperature Forecast (Next 30 Days)")
    plt.xlabel("Date")
    plt.ylabel("Predicted Temperature")

    plt.savefig("outputs/plots/forecast.png")
    plt.close()

    print("✅ All plots saved successfully!")