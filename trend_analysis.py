import pandas as pd

def analyze_trends(df):
    df['year'] = df['date'].dt.year
    yearly_avg = df.groupby('year')['temperature'].mean()
    print(yearly_avg)