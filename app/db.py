import pandas as pd
from models import Weapon


# df = pd.DataFrame(df)

file = "weapons_list.csv"

def muha(file: Weapon):
    df = pd.read_csv(file)
    df = pd.DataFrame(df)
    return df



df = muha(file)

def create_risk_level():
    df['risk_level'] = pd.cut(df['range_km'],
                        bins=[0, 20, 100, 300, 1000],
                        labels=['low','medium','high','extreme']) 


def fill_manufacturer():
    df['manufacturer'] = df['manufacturer'].fillna("Unknown")
