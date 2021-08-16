import os
import psycopg2

def get_connection():
    dsn = os.environ['DATABASE_URL']
    return psycopg2.connect(dsn)
conn = get_connection()
cur = conn.cursor()
cur.execute('CREATE TABLE test (id int);')
cur.close()
conn.close()
