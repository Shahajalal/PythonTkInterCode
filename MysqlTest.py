import MySQLdb
db=MySQLdb.connect("localhost","root","s1hahajalal","school")
c=db.cursor()
sql="select * from student"
c.execute(sql)
rows=c.fetchall()
print(rows)