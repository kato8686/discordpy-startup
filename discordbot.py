import MySQLdb

# 接続する
con = MySQLdb.connect(
user='root',
passwd='root',
host='localhost',
db='mysql')

# 接続を閉じる
con.close
