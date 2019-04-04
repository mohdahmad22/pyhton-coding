import sqlite3

class Database:
    
    table = 'expenses'

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
                item TEXT,
                price DOUBLE
            )
        """

        return self.run(query)

    def add(self, item, price):
        query = f"""
            INSERT INTO {self.table} VALUES(
                null, '{item}', {price}
            )
        """
        return self.run(query)

    def delete(self, id):
        query = f"""
            DELETE FROM {self.table} WHERE id = {id}
        """

        return self.run(query)

    def view(self):
            query = f"SELECT * FROM {self.table}"
            try:
                result = self.con.execute(query)
                return result.fetchall()
            except Exception as e:
                print('Error')
                print(e)