"""Sprint Challenge for Unit 3 - Sprint 2 - SQL Queries"""

import sqlite3


"""Create connection to new database"""
conn = sqlite3.connect("demo_data.sqlite3")
print("Connection Successful")

"""Instantiate cursor"""
curs = conn.cursor()
print("Cursor Successful")


"""Create Table Statement"""
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS demo (
    s VARCHAR(5),
    x INT,
    y INT
);
"""


"""Execute Create Table Statement"""
curs.execute(CREATE_TABLE_QUERY)


"""Commit new table on the connection"""
conn.commit()
print("Table Successfully Created!!!")


"""Get Data - Should always be a list of tuples"""
data = (('g', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7))


"""Insert data into table"""
INSERT_ROWS_INTO_DEMO = """
INSERT INTO demo(s, x, y)
VALUES (?, ?, ?);
"""


for row in data:
    curs.execute(INSERT_ROWS_INTO_DEMO, row)


"""Commit inserted data on the connection"""
conn.commit()
print("Data Successfully Inserted!")


"""PART 1 SQL QUERIES"""
"""How many rows are there? - It should be 3!"""
row_count = """
SELECT COUNT(*)
FROM demo;
"""


"""Execute First Query"""
response = curs.execute(row_count).fetchall()
print(response)


"""How many rows are there where both x and y are at least 5?"""
xy_at_least_5 = """
SELECT COUNT(*)
FROM demo
WHERE x > 4 AND y > 4;
"""


"""Execute Second Query"""
response2 = curs.execute(xy_at_least_5).fetchall()
print(response2)

"""How many unique values of y are there?"""
unique_y = """
SELECT COUNT(DISTINCT(y))
FROM demo;
"""


"""Execute Third Query"""
response3 = curs.execute(unique_y).fetchall()
print(response3)


"""Close cursor"""
curs.close()
