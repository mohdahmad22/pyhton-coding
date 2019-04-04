import sqlite3
con=sqlite3.connect('student.dbs')
print('connected')
#query='CREATE TABLE students(name TEXT,class TEXT)'
#con.execute(query)
#con.commit()
#query2="INSERT INTO students values('ahmad','bca33')"
#con.execute(query2)
#con.commit()
query="delete from students where name='ahmad'"
con.execute(query)

query3="select * from students"
data=con.execute(query3)
print(data.fetchall())
con.commit()
