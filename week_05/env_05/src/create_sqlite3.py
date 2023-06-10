import sqlite3
conn = sqlite3.connect('huhu.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS foods (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL NOT NULL)')
conn.commit()
conn.close()