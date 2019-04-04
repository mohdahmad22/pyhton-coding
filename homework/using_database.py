# import database file as a module
from example_database import Database

db = Database()

db.create_table()

db.add('Chai', 8)
db.add('Biscuit', 10)
db.add('Eggs', 14)
db.add('Burger', 100)
db.add('Brush', 98)

data = db.view()
print(data)