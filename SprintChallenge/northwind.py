"""-----Part 2 of Sprint Challenge-----"""

import sqlite3


"""Create connection with northwind_small.sqlite3"""
conn = sqlite3.connect("northwind_small.sqlite3")


"""Instantiate Cursor"""
curs = conn.cursor()


"""
What are the 10 most expensive items
(per unit price) in the database?
"""
expensive_items = """
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""


"""Execute expensive_items Query"""
query1 = curs.execute(expensive_items).fetchall()
print(query1)


"""
What is the average age of an employee
at the time of their hiring?
(Hint: a lot of arithmetic works with dates)
"""
avg_hire_age = """
SELECT AVG(HireDate - BirthDate)
FROM Employee;
"""


"""Execute avg_hire_age Query"""
query2 = curs.execute(avg_hire_age).fetchall()
print(query2)


"""
Stretch Goal!
How does the average age of employee at hire
vary by city?
"""
avg_age_by_city = """
SELECT City, AVG(HireDate - BirthDate)
FROM Employee
GROUP BY City;
"""


"""Execute avg_age_by_city Query"""
query3 = curs.execute(avg_age_by_city).fetchall()
print(query3)


"""-----PART 3 of Sprint Challenge-----"""


"""
What are the ten most expensive items
(per unit price) in the database AND their suppliers?
"""
ten_most_expensive = """
SELECT DISTINCT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product
INNER JOIN Supplier
ON Product.SupplierId = Supplier.Id
ORDER BY Product.UnitPrice DESC
LIMIT 10;
"""


"""Execute ten_most_expensive Query"""
part3_query1 = curs.execute(ten_most_expensive).fetchall()
print(part3_query1)


"""
What is the largest category
(by number of unique products in it)?
"""
largest_category = """
SELECT Category.CategoryName, COUNT(DISTINCT Product.ProductName)
FROM Category
INNER JOIN Product
ON Category.Id = Product.CategoryId
GROUP BY Category.CategoryName
ORDER BY COUNT(Product.ProductName) DESC
LIMIT 1;
"""


most_territories = """
SELECT Employee.FirstName, Employee.LastName
FROM Employee
INNER JOIN EmployeeTerritory
ON Employee.Id = EmployeeTerritory.EmployeeId
INNER JOIN Territory
ON EmployeeTerritory.TerritoryId = Territory.Id
GROUP BY Employee.FirstName
ORDER BY COUNT(Territory.Id) DESC
LIMIT 1;
"""


"""Execute largest_category Query"""
part3_query2 = curs.execute(largest_category).fetchall()
print(part3_query2)


"""-------Part 4 - Questions and Answers"""
"""
Answer the following questions, baseline ~3-5
sentences each, as if they were interview screening
questions (a form you fill when applying for a job):
​
- In the Northwind database, what is the type of
relationship between the `Employee` and `Territory` tables?
- What is a situation where a document store (like MongoDB)
is appropriate, and what is a situation where it is not appropriate?
- What is "NewSQL", and what is it trying to achieve?

"""

answer1 = "The relationship between the 'Employee' and 'Territory' tables \
            shows that each employee is responsible for a certain \
            territory or territories. \
            There is a column in Territory that has a short description \
            that you can read to see the details of each territory."


print(answer1)


answer2 = "A document store like MongoDB would be appropriate if \
            you were dealing with Big Data and needed the benefits \
            of horizontal scaling so it is not all done on one computer. \
            MongoDB is an object-oriented NOSQL database. So, it handles data \
            that is located in separate documents instead of in tables\
            like data stored in SQL databases."


print(answer2)


answer3 = "NewSQL is a way of using a relational database that has \
            characteristics of a SQL and a NOSQL database. \
            NewSQL tries to achieve the scalability of a \
            non-relational database and the guaranteed ACID \
            properties of a relational database."


print(answer3)
