from db_con import *


class Class:
    def __init__(self, database):
        self.database = database

    def __str__(self):
        return f"Class ID: {self.id} in College: {self.college} --> number of seats: {self.seats_num},
          smart: {self.is_smart}, accessible: {self.accesible}"
    
    def add_class(self, college, seats_num=None, is_smart=None):
        self.college = college
        self.seats_num = seats_num
        self.is_smart = is_smart
        self.accesible = True
        query = "INSERT INTO classes (college, seats_num, is_smart) VALUES (%s, %s, %s)"
        params = (self.college, self.seats_num, self.is_smart)
        self.database.execute_query(query, params)
        self.database.commit()

    def update_class(self, id, college=None, seats_num=None, is_smart=None):
        college = college or self.college
        seats_num = seats_num or self.seats_num
        is_smart = is_smart or self.is_smart
        query = "UPDATE classes SET college = %s, seats_num = %s, is_smart = %s WHERE id = %s"
        params = (college, seats_num, is_smart, id)
        self.database.execute_query(query, params)
        self.database.commit()

    def delete_class(self, id):
        query = "UPDATE classes SET accessible = 0 WHERE id = %s"
        params = (id,)
        self.database.execute_query(query, params)
        self.database.commit()
