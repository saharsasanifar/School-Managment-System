from person import *

class Courses(Base):
    last_id = 1234
    def add_courses(self, name, credit, prerequisit):
        super().add_member(name)
        self.credit = credit
        self. prerequisit = prerequisit
        self.id_ = "C" + str(Courses.last_id)
        Courses.last_id += 1
        query = "INSERT INTO courses (name, credit, prerequisit. id_) VALUES (%s, %s, %s, %s)"
        params = (self.name, self.credit, self.prerequisit, self.id_)
        self.database.execute_query(query, params)
        self.database.commit()

    def update_courses(self, name=None, credit=None, prerequisit=None):
        super().update_member(name)
        credit = credit or self.credit
        prerequisit = prerequisit or self.prerequisit
        query = "UPDATE courses SET name = %s, credit = %s, prerequisit = %s"
        params = (name, f_name, age, college, entrance_year)
        self.database.execute_query(query, params)
        self.database.commit()
