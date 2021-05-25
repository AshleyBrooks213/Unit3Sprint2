import sqlite3
print("----- START OF ETL -----")

# Initiate a New SQLite DB

# To Create an Empty SQLite DB:
# Simply sqlite3.connect() to Whatever you
# want your new DB to be called.

# sqlite3.connect('Type your New DataBase name here.db)

db_path = 'study_part1.sqlite3'


# Establish Connection
#sl_conn = sqlite3.connect("study_part1.sqlite3")
sl_conn = sqlite3.connect(db_path)
print("SQLite Connection Established")
# Instantiate Cursor
sl_curs = sl_conn.cursor()
print("Cursor Instantiated")


CREATE_TABLE_STUDENTS = """
    CREATE TABLE IF NOT EXISTS students (
        student VARCHAR(50),
        studied VARCHAR(50),
        grade INT,
        age INT,
        sex VARCHAR(40)
    );
"""


# Execute CREATE TABLE Query
sl_curs.execute(CREATE_TABLE_STUDENTS)

# Commit New Table on the Connection
sl_conn.commit()
print("Table Successfull Created")


# Get Data 
student_data = (('Lion-O', 'True', 85, 24, 'Male'),
                ('Cheetara', 'True', 95, 22, 'Female'),
                ('Mumm-Ra', 'False', 65, 153, 'Male'),
                ('Snarf', 'False', 70, 15, 'Male'),
                ('Panthro', 'True', 80, 30, 'Male'))


# ? is the placeholder value for SQLite
INSERT_ROWS_INTO_STUDENTS = """
INSERT INTO students(student, studied, grade, age, sex)
VALUES(?, ?, ?, ?, ?);
"""

# In the Execute method, you can pass values as a second argument
# AFTER passing a Query String that Contains Placeholder Values
# which for SQLite are '?'.
# ----> For PostGreSQL the placeholder value works the same way but it
#       is '%s'. <---Just FYI
for row in student_data:
    sl_curs.execute(INSERT_ROWS_INTO_STUDENTS, row)


# Commit Inserted Rows on the Connection
sl_conn.commit()
print("Rows Successfully Inserted")

#---Check on the Success of the Insertion---


# Get 5 Rows from New Table, Students
GET_ALL_FROM_NEW_TABLE = """
SELECT * FROM students LIMIT 5;
"""


# Execute Query
response = sl_curs.execute(GET_ALL_FROM_NEW_TABLE).fetchall()
# In the responses you might see that before each string there
# is a u (u'string1', u'string2')<-- Like so
# Apparently this just stands for Unicode and should not be an issue.

#Print Response
print("--- SELECT * RESPONSE ---")
print(response)
print("--- RESPONSE END ---")


# Close Up Shop -> Close Cursor and Connection
sl_curs.close()
print("Cursor Closed")
sl_conn.close()
print("Connection Closed")
print("----- END OF ETL -----")





