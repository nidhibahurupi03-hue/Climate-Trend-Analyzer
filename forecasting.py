import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def forecast_temperature(df):
    df = df.copy()

    # Convert date to numeric
    df['date_ordinal'] = pd.to_datetime(df['date']).map(pd.Timestamp.toordinal)

    X = df[['date_ordinal']]
    y = df['temperature']

    model = LinearRegression()
    model.fit(X, y)

    # Future dates
    future_dates = pd.date_range(start=df['date'].max(), periods=30)
    future_ord = future_dates.map(pd.Timestamp.toordinal).values.reshape(-1,1)

    predictions = model.predict(future_ord)

    forecast_df = pd.DataFrame({
        'date': future_dates,
        'predicted_temp': predictions
    })

    return forecast_df