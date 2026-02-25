import re

def is_safe_query(query):
    forbidden = [
        "delete", "drop", "update", "alter",
        "insert", "truncate", "create", "replace"
    ]
    q = query.lower()
    return not any(re.search(rf"\b{word}\b", q) for word in forbidden)

def normalize(df):
    return df.sort_index(axis=1).reset_index(drop=True)

def validate(user_df, expected_df):
    try:
        return normalize(user_df).equals(normalize(expected_df))
    except:
        return False
