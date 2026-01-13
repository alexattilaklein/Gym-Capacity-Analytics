import pandas as pd
import matplotlib as mpl

def clean_data():

    df = pd.read_csv("data.csv")

    # Extract mindate, maxdate
    df["exact_date"] = df["date"].str[:10]
    mindate = df["exact_date"].min()
    maxdate = df["exact_date"].max()
    df['exact_date'] = pd.to_datetime(df['exact_date'])

    # Datatype conversions
    df['date'] = pd.to_datetime(df['date'], utc=True)
    df['is_weekend'] = df['is_weekend'].astype(bool)
    df['is_holiday'] = df['is_holiday'].astype(bool)
    df['is_start_of_semester'] = df['is_start_of_semester'].astype(bool)
    df['is_during_semester'] = df['is_during_semester'].astype(bool)

    # New columns
    df["year"] = df["date"].dt.year
    df["minute"] = df["date"].dt.round('10min')
    df["minute"] = df["minute"].dt.minute
    df["day"] = df["date"].dt.day
    df["day_of_week"] = df['date'].dt.day_name() # Original values were wrong + replace with Day name
    df['is_weekend'] = df["day_of_week"].isin(['Saturday', 'Sunday']) # Original values were wrong

    # Drop unnecessary / redundant columns
    df.drop(columns=["date","timestamp","temperature"], inplace=True)

    return df,mindate,maxdate
