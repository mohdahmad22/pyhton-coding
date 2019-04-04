# create a class DATABASE2
# and add a table students
# store the following details
# name, age, class, gender
# then create methods for
# adding, removing, view and searching
# student by name
# YAY
import sqlite3

class Database2:
    
    table = 'students'

    def __init__(self, name = "mydb.sqlite3"):
        self.con = sqlite3.connect(name)
        print('Connected')

    def run(self, query):
        try:
            self.con.execute(query)
            self.con.commit() # saves
            return True
        except Exception as e:
            print(query)
            print(e)
            return False

    def create_table(self):
        query = f"""
            CREATE TABLE {self.table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                class TEXT,
                gender TEXT
            )
        """

        return self.run(query)

    def add(self, name, age, class_, gender):
        query = f"""
            INSERT INTO {self.table} VALUES(
                null, '{name}', {age},'{class_}', '{gender}'
            )
        """
        return self.run(query)

    def delete(self, name):
        query = f"""
            DELETE FROM {self.table} WHERE name = '{name}'
        """

        return self.run(query)

    def search(self,name):
            query = f"SELECT * FROM {self.table} where name='{name}'"
            try:
                result = self.con.execute(query)
                return result.fetchall()
            except Exception as e:
                print('Error')
                print(e)
    def view(self):
            query = f"SELECT  * FROM {self.table} "
            try:
                result = self.con.execute(query)
                return result.fetchall()
            except Exception as e:
                print('Error')
                print(e)