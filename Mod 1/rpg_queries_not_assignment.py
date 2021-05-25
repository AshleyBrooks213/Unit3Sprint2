"""Practice using SQL and doing the assignment the right way"""


import sqlite3


"""Step1: Connect to Database"""
conn = sqlite3.connect("rpg_db.sqlite3")

"""Step2: Make a cursor"""
curs = conn.cursor()

"""Step 3: Write our Query"""
example_of_query = """
SELECT * FROM charactercreator_character;
"""

"""Step 4: Execute Query"""
curs.execute(example_of_query)

"""Step5: Grab results from cursor"""
results = curs.execute(example_of_query)

"""Step6: Fetchall"""
results = results.fetchall()


"""Or you can write a function that will do all of this"""
#For Connecting to our database
def connect_to_db(db_name="rpg_db.sqlite3"):
    conn = sqlite3.connect(db_name)
    return conn

#For executing READ queries
def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


"""Question 1: How many total Characters are there?"""
"""302 Distinct character id's"""
#Counts the rows of the character_id column in charactercreator_character
#and removes duplicates (DISTINCT)
Q1_Query = """
SELECT COUNT(DISTINCT character_id) 
FROM charactercreator_character
"""
results1 = curs.execute(Q1_Query)

answer1 = results1.fetchall()


"""Question 2: How many of each specific subclass?"""
"""Fighter: 68"""
fighter = """
SELECT
COUNT(DISTINCT charactercreator_character.character_id)
FROM charactercreator_character
INNER JOIN charactercreator_fighter
ON charactercreator_character.character_id = 
charactercreator_fighter.character_ptr_id
;
"""
fighter_class = curs.execute(fighter)
fighter_class_answer = fighter_class.fetchall()

"""Cleric"""
cleric = """
SELECT
COUNT(DISTINCT charactercreator_character.character_id)
FROM charactercreator_character
INNER JOIN charactercreator_cleric
ON charactercreator_character.character_id = 
charactercreator_cleric.character_ptr_id
;
"""
cleric_class = curs.execute(cleric)
cleric_class_answer = cleric_class.fetchall()


if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()

    fighter_class_using_function_ex = execute_query(curs, fighter)
    print("Number of Characters in Fighter class:", fighter_class_using_function_ex)

    cleric_class_using_function_ex = execute_query(curs, cleric)
    print("Number of Characters in Cleric class:", cleric_class_using_function_ex)