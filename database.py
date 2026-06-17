import sqlite3

DB_NAME = "api_metrics.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS api_metrics(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        api_name TEXT,
        url TEXT,
        response_time REAL,
        status_code INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS apis(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        api_name TEXT NOT NULL,
        api_url TEXT NOT NULL UNIQUE
    )
    """)
    
    conn.commit()
    conn.close()

def insert_metric(api_name,url,response_time,status_code):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO api_metrics
    (api_name,url,response_time,status_code)
    VALUES (?,?,?,?)
    """,(api_name,url,response_time,status_code))

    conn.commit()
    conn.close()

def add_api(api_name, api_url):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO apis(api_name, api_url)
    VALUES(?,?)
    """,(api_name, api_url))

    conn.commit()
    conn.close()

def get_all_apis():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM apis")

    data = cursor.fetchall()

    conn.close()

    return data

def delete_api(api_id):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM apis WHERE id=?",
        (api_id,)
    )

    conn.commit()
    conn.close()