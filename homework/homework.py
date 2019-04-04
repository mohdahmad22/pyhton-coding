from Databasehome import Database2
db=Database2()
#db.create_table()
#db.add('vikas','20','bca','male')
data=db.view()
#db.delete('ahmad')
data=db.search('vikas')
print(data)