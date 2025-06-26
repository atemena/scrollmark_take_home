import os
import pandas as pd
import logging
import tempfile
from src.ingest import load_comments_csv

def test_load_comments_csv_valid(tmp_path):
    # Use the provided example.csv (all valid)
    df = load_comments_csv("data/example.csv")
    assert len(df) == 4
    assert set(df.columns) == {"timestamp", "media_id", "media_caption", "comment_text"}

def test_load_comments_csv_malformed(tmp_path, caplog):
    # Create a temp CSV with one malformed row
    csv_content = (
        "timestamp,media_id,media_caption,comment_text\n"
        "2024-06-01T12:00:00Z,1,Caption,Comment\n"
        "2024-06-01T12:05:00Z,1,Caption,\n"  # Malformed: missing comment_text
        "2024-06-01T13:00:00Z,2,Caption,Comment\n"
    )
    temp_file = tmp_path / "malformed.csv"
    temp_file.write_text(csv_content)
    with caplog.at_level(logging.WARNING):
        df = load_comments_csv(str(temp_file))
        assert len(df) == 2  # One row skipped
        assert "Skipped 1 malformed rows" in caplog.text
