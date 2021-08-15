import psycopg2
connection = psycopg2.connect("host=192.168.24.97 port=9403 dbname=sampledb user=sayamada password=pssword")
print(connection.get_backend_pid())
