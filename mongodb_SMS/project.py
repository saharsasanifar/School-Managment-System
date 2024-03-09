from pymongo import MongoClient
import configparser
from pymongo.errors import DuplicateKeyError, CollectionInvalid
from schemas import *

class MongoDBConnection:
    @staticmethod
    def load_config(file_name="config.ini"):
        config = configparser.ConfigParser()
        config.read(file_name)
        return config
    
    def __init__(self, file_name="config.ini"):
        config = MongoDBConnection.load_config(file_name)
        mongo_host = config['mongodb']['host']
        mongo_port = int(config['mongodb']['port'])
        db_name = config['mongodb']['db_name']
        self.collection_names = [config['mongodb'][i] for i in config['mongodb']['col_name'].split(",")]
        self.client = MongoClient(mongo_host, mongo_port)
        self.db = self.client[db_name]
        self.setup_collection()

    def setup_collection(self):
        for collection_name in self.collection_names:
            for n, s in schemas.items():
                if n == f"{collection_name}_schema":
                    valid = s
            try:
                self.db.create_collection(collection_name, validator=valid)
                print(f"Collection {collection_name} created!")

            except:
                collection = self.db[self.collection_name]
        collection.create_index("id_", unique=True)
        



class Student:
    def __init__(self, id_, name, age, **info):
        self.id_ = id_
        self.name = name
        self.age = age
        self.info = info

    def change_to_dict(self):
        student = {
            "stu_id": self.id_,
            "name": self.name,
            "age": self.age
            **self.info
        }
        return student



class Teacher:
    def __init__(self, id_, name, age, **info):
        self.id_ = id_
        self.name = name
        self.age = age
        self.info = info

    def change_to_dict(self):
        teacher = {
            "id_": self.id_,
            "name": self.name,
            "age": self.age
            **self.info
        }
        return teacher
    
class Classroom:
    def __init__(self, id_, seats, college, **info):
        self.id_ = id_
        self.seats = seats
        self.college = college
        self.info = info

    def change_to_dict(self):
        classroom = {
            "class_id": self.id_,
            "seats": self.seats,
            "college": self.college
            **self.info
        }
        return classroom
    

    
class Course:
    def __init__(self, id_, name, teacher_id, class_id, **info):
        self.id_ = id_
        self.name = name
        self.teacher_id = teacher_id
        self.class_id = class_id
        self.info = info

    def change_to_dict(self):
        course = {
            "course_id": self.id_,
            "name": self.name,
            "teacher_id": self.teacher_id,
            "class_id": self.class_id
            **self.info
        }
        return course
    



class School:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_student(self, student):
        student = student.change_to_dict()
        print(student)
        try:
            self.db_connection.db[self.db_connection.Students].insert_one(student)
            print("Added!")
        except Exception as e:
            print(e)

    def remove_student(self, stu_id):
        result = self.db_connection.db[self.db_connection.Students].delete_one({"id_": stu_id})
        if result.deleted_count:
            print("Removed!")
        else:
            print("Not Found!")

    def search_student(self, stu_id):
        data = self.db_connection.db[self.db_connection.Students].find_one({"id_": stu_id})
        print(data)

    def show_all_students(self):
        data = self.db_connection.db[self.db_connection.Students].find()
        data = list(data)

    def add_teacher(self, teacher):
        teacher = teacher.change_to_dict()
        self.db_connection.db[self.db_connection.Teachers].insert_one(teacher)
        print("Added!")

    def remove_teacher(self, teacher_id):
        result = self.db_connection.db[self.db_connection.Teachers].delete_one({"id_": teacher_id})
        if result.deleted_count:
            print("Removed!")
        else:
            print("Not Found!")

    def add_classroom(self, classroom):
        classroom = classroom.change_to_dict()
        self.db_connection.db[self.db_connection.Classes].insert_one(classroom)
        print("Added!")

    def add_course(self, course):
        course = course.change_to_dict()
        self.db_connection.db[self.db_connection.Courses].insert_one(course)
        print("Added!")

    def remove_course(self, course_id):
        result = self.db_connection.db[self.db_connection.Courses].delete_one({"course_id": course_id})
        if result.deleted_count:
            print("Removed!")
        else:
            print("Not Found!")