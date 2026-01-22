import pandas as pd



def create_risk_level(df):
    df['risk_level'] = pd.cut(df['range_km'],
                        bins=[0, 20, 100, 300, 1000],
                        labels=['low','medium','high','extreme']) 
    
    return df

def fill_manufacturer(df):
    df['manufacturer'] = df['manufacturer'].fillna("Unknown")
    return df