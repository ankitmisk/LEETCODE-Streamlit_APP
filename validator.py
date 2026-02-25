import pandas as pd

def normalize_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize DataFrame for fair comparison:
    - lowercase column names
    - sort columns
    - sort rows
    - reset index
    """
    if df is None or df.empty:
        return df

    df_copy = df.copy()

    # Normalize column names (case-insensitive)
    df_copy.columns = [str(col).lower() for col in df_copy.columns]

    # Sort columns alphabetically
    df_copy = df_copy.reindex(sorted(df_copy.columns), axis=1)

    # Convert all values to string for safe comparison
    df_copy = df_copy.astype(str)

    # Sort rows by all columns
    df_copy = df_copy.sort_values(by=list(df_copy.columns))

    return df_copy.reset_index(drop=True)


def validate(user_df: pd.DataFrame, expected_df: pd.DataFrame) -> bool:
    try:
        user_norm = normalize_df(user_df)
        expected_norm = normalize_df(expected_df)
        return user_norm.equals(expected_norm)
    except Exception:
        return False
