from db_con import *


class Student:
    def __init__(self, database):
        self.database = database

    def add_student(self, name, f_name, age, college, entrance_year):
        self.name = name
        self.f_name = f_name
        self.age = age
        self.college = college
        self.entrance_year = entrance_year
        query = "INSERT INTO students (name, f_name, age, college, entrance_year) VALUES (%s, %s, %s, %s, %s)"
        params = (self.name, self.f_name, self.age, self.college, self.entrance_year)
        self.database.execute_query(query, params)
        self.database.commit()

    def update_student(self, id, name=None, f_name=None, age=None, college=None, entrance_year=None):
        name = name or self.name
        f_name = f_name or self.f_name
        age = age or self.age
        college = college or self.college
        entrance_year = entrance_year or self.entrance_year
        query = "UPDATE students SET name = %s, f_name = %s, age = %s, college = %s, entrance_year = %s WHERE id = %s"
        params = (name, f_name, age, college, entrance_year, id)
        self.database.execute_query(query, params)
        self.database.commit()

    def delete_student(self, id):
        query = "DELETE FROM students WHERE id = %s"
        params = (id,)
        self.database.execute_query(query, params)
        self.database.commit()

    def add_course(self, course_id):
        query = "UPDATE students SET course_id = %s WHERE id = %s"
        params = (course_id, id)
        self.database.execute_query(query, params)
        self.database.commit()