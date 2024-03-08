import mysql.connector
from mysql.connector import Error
from tables import *

class Database:
    def __init__(self, host, user, password, database=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
        except Error as e:
            print(e)

    def create_table(self, table_sql):
        try:
            self.cursor.execute(table_sql)
            print(f"{table_sql}: created")
        except Error as e:
            print(e)

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            if self.cursor.with_rows:
                return self.cursor.fetchall()
        except Error as e:
            print(e)

    def commit(self):
        self.connection.commit()
    
    def close(self):
        self.connection.close()


if __name__ == "__main__":
    db_info = {
        'host': 'localhost',
        'user': 'root',
        'password': 'pass',
        'database': 'School_Managment_System'
        }
    db = Database(**db_info)

    for table in tables.values():
        db.create_table(table)