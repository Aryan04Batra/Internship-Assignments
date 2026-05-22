import sqlite3
conn = sqlite3.connect("college.db")
sql = """
CREATE TABLE IF NOT EXISTS Student(
    id INTEGER PRIMARY KEY,
    name TEXT,
    branch TEXT
)
"""
conn.execute(sql)
sql = """
CREATE TABLE IF NOT EXISTS Teacher(
    id INTEGER PRIMARY KEY,
    name TEXT,
    subject TEXT
)
"""
conn.execute(sql)
sql = """
CREATE TABLE IF NOT EXISTS Course(
    id INTEGER PRIMARY KEY,
    course_name TEXT,
    duration TEXT
)
"""
conn.execute(sql)
conn.commit()

#Inserting Data

sql = """
INSERT INTO Student VALUES
(1,'Aryan','CSE'),
(2,'Rahul','IT'),
(3,'Aman','ECE')
"""
conn.execute(sql)
sql = """
INSERT INTO Teacher VALUES
(1,'Sharma','Python'),
(2,'Verma','DBMS')
"""
conn.execute(sql)
sql = """
INSERT INTO Course VALUES
(1,'Python','3 Months'),
(2,'DBMS','4 Months')
"""
conn.execute(sql)
conn.commit()

#Select Operations
print("\nStudent Table Data")
sql = "SELECT * FROM Student"
for row in conn.execute(sql):
    print(row)
print("\nStudents from CSE Branch")
sql = "SELECT * FROM Student WHERE branch='CSE'"
for row in conn.execute(sql):
    print(row)

#Update Data

sql = """
UPDATE Student
SET branch='AI'
WHERE id=2
"""
conn.execute(sql)
conn.commit()

sql = "SELECT * FROM Student"
for row in conn.execute(sql):
    print(row)

#Delete Data

sql = """
DELETE FROM Student
WHERE id=3
"""
conn.execute(sql)
conn.commit()
print("\nData Deleted Successfully")
print("\nFinal Student Table")
sql = "SELECT * FROM Student"
for row in conn.execute(sql):
    print(row)
conn.close()
