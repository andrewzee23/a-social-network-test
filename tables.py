import sqlite3
from sqlite3 import Error


conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('delete from posts')

print('rows cleared')

conn.commit()

conn.close()

print('connection closed')