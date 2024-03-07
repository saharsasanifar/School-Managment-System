tables = {
    'students' : """
                CREAT TABLE IF NOT EXIST students(
                id INT AUTO_INCREMENT,
                name VARCHAR(50) NOT NULL,
                f_name VARCHAR(50) NOT NULL,
                age INT,
                college VARCHAR(225),
                entrance_year INT,
                course_id INT,
                PRIMARY KEY (id),
                FOREIGN KEY (course_id) REFERENCES courses (id)
                )
""",

    'teachers' : """
                CREAT TABLE IF NOT EXIST teachers(
                id INT AUTO_INCREMENT,
                name VARCHAR(50) NOT NULL,
                f_name VARCHAR(50) NOT NULL,
                age INT,
                college VARCHAR(225),
                ranking VARCHAR(225) NOT NULL,
                course_id INT,
                PRIMARY KEY (id),
                FOREIGN KEY (course_id) REFERENCES courses (id)
                )
""",

    'courses' : """
                CREAT TABLE IF NOT EXIST courses(
                id INT AUTO_INCREMENT,
                course_title VARCHAR(225) NOT NULL,
                class_id INT,
                teacher_id INT,
                PRIMARY KEY (id),
                FOREIGN KEY (class_id) REFERENCES classes (id),
                FOREIGN KEY (teacher_id) REFERENCES teachers (id)
                )
""",
    
    'classes' : """
                CREATE TABLE IF NOT EXIST classes(
                id INT AUTO_INCREMENT,
                college VARCHAR(225) NOT NULL,
                seats_num INT,
                is_smart BOOL,
                PRIMARY KEY (id)
                )
"""
}