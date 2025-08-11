import sqlite3

class Databaserooms():
    def __init__(self):
        pass

    def connection_db(self):
        self.conn = sqlite3.connect("db.db")
        self.cur = self.conn.cursor()
        print("successfully connected to database")

        def createtable(self):
            query = "CREATE TABLE IF NOT EXISTS ROOMS(id INTEGER PRIMARY KEY AUTOINCREMENT)"
            self.cur.execute(query)

            query = "ALERT TABLE rooms ADD COLUMN name TEXT"
            self.cur.execute(query)

            query = "ALERT TABLE rooms ADD COLUMN floor INTEGER"
            self.cur.execute(query)

            query = "ALERT TABLE rooms ADD COLUMN room_number INTEGER"
            self.cur.execute(query)

            self.conn.commit()
            print("table created successfully")
