def perform_eda(df):
    print(df.describe())
    print(df.isnull().sum())