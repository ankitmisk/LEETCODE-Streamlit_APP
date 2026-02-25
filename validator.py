import re
import pandas as pd

# --------------------------------
# SECURITY: ALLOW ONLY SELECT
# --------------------------------
def is_safe_query(query: str) -> bool:
    forbidden = [
        "delete", "drop", "update", "alter",
        "insert", "truncate", "create", "replace"
    ]

    query_lower = query.lower()
    return not any(
        re.search(rf"\b{word}\b", query_lower) for word in forbidden
    )

# --------------------------------
# RESULT VALIDATION (CASE-INSENSITIVE)
# --------------------------------
def normalize_df(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        return df

    df = df.copy()

    # Normalize column names
    df.columns = [str(col).lower() for col in df.columns]

    # Sort columns
    df = df.reindex(sorted(df.columns), axis=1)

    # Convert values to string for safe comparison
    df = df.astype(str)

    # Sort rows
    df = df.sort_values(by=list(df.columns))

    return df.reset_index(drop=True)


def validate(user_df: pd.DataFrame, expected_df: pd.DataFrame) -> bool:
    try:
        user_norm = normalize_df(user_df)
        expected_norm = normalize_df(expected_df)
        return user_norm.equals(expected_norm)
    except Exception:
        return False
