import sqlite3
DB_NAME = 'logs.db'
def init_db():
    conn = sqlite3.connect(DB_NAME)
    with open("setup_db.sql") as f:
        conn.executescript(f.read())
    conn.close()

def log_query(query, category, level):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO queries (query, category, response) VALUES (?, ?, ?)", (query, category, level))
    conn.commit()
    conn.close()