import sqlite3

def setup_db():
    conn = sqlite3.connect("bikerental.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (name TEXT PRIMARY KEY)")
    conn.commit()
    conn.close()

def add_user(name):
    conn = sqlite3.connect("bikerental.db")
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect("bikerental.db")
    cur = conn.cursor()
    cur.execute("SELECT name FROM users")
    rows = cur.fetchall()
    conn.close()
    return [r[0] for r in rows]

def delete_user(name):
    conn = sqlite3.connect("bikerental.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE name=?", (name,))
    conn.commit()
    conn.close()
