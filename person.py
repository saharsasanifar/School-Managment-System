from db_con import *

class Base :
    def __init__(self, database):
        self.database = database
 
    def add_member(self, name):
        self.name = name
        query = "INSERT INTO students (name) VALUES (%s)"
        params = (self.name,)
        self.database.execute_query(query, params)
        self.database.commit()

    def delete_member(self):
        query = "DELETE FROM students WHERE id = %s"
        params = (self.id,)
        self.database.execute_query(query, params)
        self.database.commit()

    def update_member(self, name=None, f_name=None, age=None, college=None, entrance_year=None):
        name = name or self.name
        query = "UPDATE students SET name = %s"
        params = (name,)
        self.database.execute_query(query, params)
        self.database.commit()

    