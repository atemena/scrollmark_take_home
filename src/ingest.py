import pandas as pd
import logging

def load_comments_csv(path):
    required_columns = {"timestamp", "media_id", "media_caption", "comment_text"}
    df = pd.read_csv(path)
    missing_cols = required_columns - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")
    # Drop rows with any missing required fields
    before = len(df)
    df_clean = df.dropna(subset=required_columns)
    skipped = before - len(df_clean)
    if skipped > 0:
        logging.warning(f"Skipped {skipped} malformed rows from {path}")
    return df_clean.reset_index(drop=True)
