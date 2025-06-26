import sqlite3
from src.db import init_db, insert_data
from src.ingest import load_comments_csv

def test_db_insert_and_counts(tmp_path):
    db_path = tmp_path / "test.sqlite"
    init_db(str(db_path))
    df = load_comments_csv("data/example.csv")
    insert_data(str(db_path), df)
    conn = sqlite3.connect(str(db_path))
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM Media")
    media_count = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM Comment")
    comment_count = c.fetchone()[0]
    conn.close()
    assert media_count == 2  # 2 unique media_id
    assert comment_count == 4  # 4 comments in example.csv
