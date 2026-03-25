import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path("data.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        login_id TEXT,
        name TEXT,
        role TEXT,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        doc_type TEXT,
        content TEXT,
        file_path TEXT,
        created_at TEXT
    )
    """)

    conn.commit()

    cur.execute("SELECT COUNT(*) FROM users")
    if cur.fetchone()[0] == 0:
        cur.executemany("""
        INSERT INTO users VALUES (NULL,?,?,?,?)
        """, [
            ("admin001","관리자","admin","0000"),
            ("김소영101","김소영","mentee","0000"),
            ("이준호201","이준호","mentor","0000"),
        ])
        conn.commit()

    conn.close()

def authenticate(login_id, password, role):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM users WHERE login_id=? AND password=? AND role=?
    """,(login_id,password,role))
    user = cur.fetchone()
    conn.close()
    return user