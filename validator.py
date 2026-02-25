import pandas as pd

def normalize_df(df):
    return df.sort_index(axis=1).sort_values(by=df.columns.tolist()).reset_index(drop=True)

def validate(user_df, expected_df):
    try:
        return normalize_df(user_df).equals(normalize_df(expected_df))
    except:
        return False
