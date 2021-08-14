import MySQLdb

# 接続する
con = MySQLdb.connect(
user='qpjacaujnkxyil',
passwd='57acd55734d09130ac9abf498de632f05969bd0e0b799f90490728e2e40abcc4',
host='ec2-23-23-128-222.compute-1.amazonaws.com',
db='dbmcuoiouunpmj')

# 接続を閉じる
con.close
