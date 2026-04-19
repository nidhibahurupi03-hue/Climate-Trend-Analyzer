from src.data_loader import load_data
from src.preprocessing import clean_data
from src.eda import perform_eda
from src.trend_analysis import analyze_trends
from src.anomaly_detection import detect_anomalies
from src.visualization import plot_all, plot_forecast
from src.forecasting import forecast_temperature

def main():
    # Load & clean data
    df = load_data("data/climate_data.csv")
    df = clean_data(df)

    # EDA
    perform_eda(df)

    # Trend analysis
    analyze_trends(df)

    # Anomaly detection
    df = detect_anomalies(df)

    # Forecasting
    forecast_df = forecast_temperature(df)

    # Visualization
    plot_all(df)
    plot_forecast(forecast_df)

if __name__ == "__main__":
    main()