import psycopg2
connection = psycopg2.connect("host=ec2-23-23-128-222.compute-1.amazonaws.com port=5432 dbname=dbmcuoiouunpmj user=qpjacaujnkxyil password=57acd55734d09130ac9abf498de632f05969bd0e0b799f90490728e2e40abcc4")
cur = connection.cursor()
cur.execute("select version()")
for row in cur:
  print(row)
