from db_con import *
import re 
import pandas as pd
#reminder =======> write email for it
class Student:

    id_ = 1234
    def add_student_with_csv(self,url):
        self.url = url
        self.df = pd.read_csv(url)
        self.name = df["name"]
        self.f_name = df["f_name"]
        self.age = df["age"]
        self.college = df["college"]
        self.entrance_year = df["entrance_year"]

    def add_student(self, name, f_name, age, college, entrance_year,email):
        super().add_member(name)
        self.f_name = f_name
        self.age = age
        self.college = college
        self.entrance_year = entrance_year
        self.id_ = "S" + str(Student.id_)
        Student.id_ += 1
        self.email = email
        query = "INSERT INTO students (name, f_name, age, college, entrance_year, id_, email) VALUES (%s, %s, %s, %s, %s, %s,%s)"
        params = (self.name, self.f_name, self.age, self.college, self.entrance_year, self.id_, email)
        self.database.execute_query(query, params)
        self.database.commit()

    def update_student(self, name=None, f_name=None, age=None, college=None, entrance_year=None, email=None):
        super().update_member(name)
        f_name = f_name or self.f_name
        age = age or self.age
        college = college or self.college
        entrance_year = entrance_year or self.entrance_year
        email = email or self.email
        query = "UPDATE students SET name = %s, f_name = %s, age = %s, college = %s, entrance_year = %s"
        params = (name, f_name, age, college, entrance_year)
        self.database.execute_query(query, params)
        self.database.commit()


    def add_course(self, course_id):
        query = "UPDATE students SET course_id = %s WHERE id = %s"
        params = (course_id, self.id)
        self.database.execute_query(query, params)
        self.database.commit()
        
    def search_student_by_id(self, id_):
        query = "SELECT * FROM students WHERE id = %s"
        params = (id_,)
        self.database.execute_query(query, params)
        self.database.commit()

    def search_student_by_name(self, name):
        query = "SELECT * FROM students WHERE name = %s"
        params = (name,)
        self.database.execute_query(query, params)
        self.database.commit()

    def search_by_course(self, course_id):
        query = "SELECT * FROM students WHERE course_id = %s"
        params = (course_id,)
        self.database.execute_query(query, params)
        self.database.commit()

    def search_student_by_id(self, id):
        query = "SELECT * FROM students WHERE id = %s"
        params = (id,)
        self.database.execute_query(query, params)
        self.database.commit()

    def search_student_by_name(self, name):
        query = "SELECT * FROM students WHERE name = %s"
        params = (name,)
        self.database.execute_query(query, params)
        self.database.commit()

    def search_by_course(self, course_id):
        query = "SELECT * FROM students WHERE course_id = %s"
        params = (course_id,)
        self.database.execute_query(query, params)
        self.database.commit()