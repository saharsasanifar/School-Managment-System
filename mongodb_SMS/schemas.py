schemas = {"Students_schema" : """{
            "$jsonSchema":{
                "bsonType": "object",
                "required": ["stu_id", "name", "age"],
                "properties":{
                    "stu_id" : {
                        "bsonType": "string", 
                        "description": "must be string"
                    },
                     "name" : {
                        "bsonType": "string", 
                        "description": "must be string"
                    },
                     "age" : {
                        "bsonType": "double", 
                        "description": "must be double"
                    }

                }
            }
        }""",

            "Teachers_schema" : """{
            "$jsonSchema":{
                "bsonType": "object",
                "required": ["tch_id", "name", "age"],
                "properties":{
                    "tch_id" : {
                        "bsonType": "string", 
                        "description": "must be string"
                    },
                     "name" : {
                        "bsonType": "string", 
                        "description": "must be string"
                    },
                     "age" : {
                        "bsonType": "double", 
                        "description": "must be double"
                    }

                }
            }
        }""",

            "Classes_schema" : """{
            "$jsonSchema":{
                "bsonType": "object",
                "required": ["class_id", "seats", "college"],
                "properties":{
                    "class_id" : {
                        "bsonType": "string", 
                        "description": "must be string"
                    },
                     "seats" : {
                        "bsonType": "int", 
                        "description": "number of seats"
                    },
                     "college" : {
                         "bsonType": "string", 
                         "description": "must be string"
                     }

                }
            }
        }""",

            "Courses_schema" : """{
            "$jsonSchema":{
                "bsonType": "object",
                "required": ["course_id", "name", "teacher_id", "class_id"],
                "properties":{
                    "course_id" : {
                        "bsonType": "string", 
                        "description": "must be string"
                    },
                     "name" : {
                        "bsonType": "string", 
                        "description": "must be string"
                    },
                     "teacher_id" : {
                        "bsonType": "int", 
                        "description": "the teachers id"
                    },

                     "class_id" : {
                         "bsonType": "int",
                         "description": "the class id"
                     }

                }
            }
        }"""}