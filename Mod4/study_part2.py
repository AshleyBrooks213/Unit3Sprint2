import sqlite3


# Instantiate a New SQLite DB
# simply sqlite3.connect() to Whatever you 
# want your new DB to be called.

# Create New DB or connect -> Same Thing
conn = sqlite3.connect("study_part2.sqlite3")
print('SQLITE DB Connection Successful')


#Instantiate Cursor
curs = conn.cursor()
print('Cursor Instantiated')


# Create Table Query
CREATE_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS study_part_2 (
        student VARCHAR(50),
        studied TEXT,
        grade INT, 
        age INT,
        sex VARCHAR(10)
    );
"""


# Execute Create Table Query
curs.execute(CREATE_TABLE_QUERY)
# Commit new table on the connection
conn.commit()
print("Table Successfully Created!")


# Get Data 
student_data = (('Lion-O', 'True', 85, 24, 'Male'),
                ('Cheetara', 'True', 95, 22, 'Female'),
                ('Mumm-Ra', 'False', 65, 153, 'Male'),
                ('Snarf', 'False', 70, 15, 'Male'),
                ('Panthro', 'True', 80, 30, 'Male'))


# Insert data
INSERT_ROWS_INTO_STUDENTS = """
INSERT INTO study_part_2(student, studied, grade, age, sex)
VALUES (?, ?, ?, ?, ?);
"""


for row in student_data:
    curs.execute(INSERT_ROWS_INTO_STUDENTS, row)


conn.commit()

print("Rows Inserted Successfully")



# 