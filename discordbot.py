import os
import psycopg2

def get_connection():
    dsn = os.environ['DATABASE_URL']
    return psycopg2.connect(dsn)

conn = get_connection()
cur = conn.cursor()
cur.execute('SELECT * FROM users')
cur.close()
conn.close()
