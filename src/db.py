import sqlite3

def init_db(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS Media (
            media_id TEXT PRIMARY KEY,
            media_caption TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS Comment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            media_id TEXT,
            timestamp TEXT,
            comment_text TEXT,
            FOREIGN KEY(media_id) REFERENCES Media(media_id)
        )
    """)
    conn.commit()
    conn.close()

def insert_data(db_path, df):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # Insert media
    media = df[["media_id", "media_caption"]].drop_duplicates().values.tolist()
    c.executemany("INSERT OR IGNORE INTO Media (media_id, media_caption) VALUES (?, ?)", media)
    # Insert comments
    comments = df[["media_id", "timestamp", "comment_text"]].values.tolist()
    c.executemany("INSERT INTO Comment (media_id, timestamp, comment_text) VALUES (?, ?, ?)", comments)
    conn.commit()
    conn.close()
