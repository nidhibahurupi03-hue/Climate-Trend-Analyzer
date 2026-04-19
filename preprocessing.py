import pandas as pd   # ✅ हे add कर

def clean_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df.fillna(method='ffill', inplace=True)
    return df