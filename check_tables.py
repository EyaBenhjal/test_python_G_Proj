# check_tables.py
import sqlite3

# chemin vers ta base SQLite
conn = sqlite3.connect("test.db")  
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables dans la base :", tables)

conn.close()
