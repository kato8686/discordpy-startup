import os
import psycopg2

def get_connection():
    dsn = os.environ['DATABASE_URL']
    return psycopg2.connect(dsn)
conn = get_connection()
cur = conn.cursor()
cur.execute('CREATE TABLE test (id int);\
            INSERT INTO test VALUES (1);\
            SELECT * FROM test;')
print(cur)
cur.close()
conn.close()
