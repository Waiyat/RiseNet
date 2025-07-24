import sqlite3

def init_db():
    conn = sqlite3.connect("wallet.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tg_id TEXT UNIQUE,
        name TEXT,
        phone TEXT,
        balance REAL DEFAULT 0.0
    )''')
    conn.commit()
    conn.close()

def register_user(tg_id, name, phone=""):
    conn = sqlite3.connect("wallet.db")
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (tg_id, name, phone) VALUES (?, ?, ?)", (tg_id, name, phone))
    conn.commit()
    conn.close()

def update_balance(tg_id, amount):
    conn = sqlite3.connect("wallet.db")
    c = conn.cursor()
    c.execute("UPDATE users SET balance = balance + ? WHERE tg_id = ?", (amount, tg_id))
    conn.commit()
    conn.close()

def get_balance(tg_id):
    conn = sqlite3.connect("wallet.db")
    c = conn.cursor()
    c.execute("SELECT balance FROM users WHERE tg_id = ?", (tg_id,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else 0.0
