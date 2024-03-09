from person import *

class Teacher(person):
    
    last_numberid = T1234
    def add_student(self, name, f_name, courses, college, id_):
        super().add_member(name)
        self.f_name = f_name
        self.college = college
        self.courses = courses 
        self.id_ = "T" + str(Teacher.last_numberid)
        Teacher.last_numberid += 1
        query = "INSERT INTO students (name, f_name, college, courses, id_) VALUES (%s, %s, %s, %s, %s)"
        params = (self.name, self.f_name, self.college, self.courses, self.id_)
        self.database.execute_query(query, params)
        self.database.commit()

    def update_teacher(self, name=None, f_name=None, college=None, courses=None):
        super().update_member(name)
        f_name = f_name or self.f_name
        college = college or self.college
        courses = courses or self.courses
        query = "UPDATE students SET name = %s, f_name = %s, college = %s, courses = %s"
        params = (name, f_name, age, college, courses)
        self.database.execute_query(query, params)
        self.database.commit()