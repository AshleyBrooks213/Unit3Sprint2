"""Basic SQlite - DS21-Unit3-Sprint2-MOD1 Assignment"""
import sqlite3


"""Step 1: Connect to Database"""
conn = sqlite3.connect("rpg_db.sqlite3")

"""Step 2: Make a cursor"""
curs = conn.cursor()

"""Step 3: Write our query"""
GET_CHARACTERS = """
SELECT * FROM charactercreator_character;
"""

"""Step 4: Execute query"""
curs.execute(GET_CHARACTERS)

"""Step 5: Grab the results from the cursor"""
results = curs.execute(GET_CHARACTERS)

"""Step 6: Fetchall"""
results = results.fetchall()


"""For Connecting to our database"""
def connect_to_db(db_name="rpg_db.sqlite3"):
    conn = sqlite3.connect(db_name)
    return conn

"""For executing READ queries"""
def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


"""For finding length of database"""
def len_characters(characters):
    return len(characters)


"""WITHOUT ANY FUNCTIONS"""
"""Question 1: How many total Characters are there?"""
"""302 Distinct character id's"""
Q1_Query = """
SELECT COUNT(DISTINCT character_id) 
FROM charactercreator_character
"""
results1 = curs.execute(Q1_Query)

answer1 = results1.fetchall()



"""Question 2: How many of each specific subclass?"""
"""Cleric: 75"""
curs2 = conn.cursor()
cleric = """
SELECT * FROM charactercreator_cleric;
"""
cleric_class = curs2.execute(cleric)
cleric_class = cleric_class.fetchall()
len(cleric_class)

"""Fighter: 68"""
#curs3 = conn.cursor() <- I don't need to create
##a separate cursor for each one
fighter = """
SELECT
COUNT(DISTINCT charactercreator_character.character_id)
FROM charactercreator_character
INNER JOIN charactercreator_fighter
ON charactercreator_character.character_id = 
charactercreator_fighter.character_ptr_id
"""
fighter_class = curs2.execute(fighter)
fighter_class_answer = fighter_class.fetchall()


"""Mage: 108"""
curs4 = conn.cursor()
mage = """
SELECT * FROM charactercreator_mage;
"""
mage_class = curs4.execute(mage)
mage_class = mage_class.fetchall()
len(mage_class)

"""Necromancer: 11"""
curs5 = conn.cursor()
necromancer = """
SELECT * FROM charactercreator_necromancer;
"""
necromancer_class = curs5.execute(necromancer)
necromancer_class = necromancer_class.fetchall()
len(necromancer_class)

"""Thief: 51"""
curs6 = conn.cursor()
thief = """
SELECT * FROM charactercreator_thief;
"""
thief_class = curs6.execute(thief)
thief_class = thief_class.fethcall()
len(thief_class)


"""Question 3: How many total items?"""
"""Items: 174"""
curs7 = conn.cursor()
item = """
SELECT * FROM armory_item;
"""
armory_item = curs7.execute(item)
armory_item = armory_item.fetchall()
len(armory_item)


"""Question 4: How many of the items are weapons? How many are not"""
"""Items that are weapons: 37"""
"""Items that are not weapons: 137"""
curs8 = conn.cursor()
weapons = """
SELECT * FROM armory_weapon;
"""
armory_weapon = curs8.execute(weapons)
armory_weapon = armory_weapon.fetchall()
len(armory_weapon)
not_weapons = len(armory_item) - len(armory_weapon)


"""Questions 5: How many items does each character have? (Return first 20 rows)"""

if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()
    curs2 = conn.cursor()
    curs3 = conn.cursor()
    curs4 = conn.cursor()
    curs5 = conn.cursor()
    curs6 = conn.cursor()
    curs7 = conn.cursor()
    curs8 = conn.cursor()
    results = execute_query(curs, GET_CHARACTERS)
    cleric_class = execute_query(curs2, cleric )
    fighter_class = execute_query(curs3, fighter)
    mage_class = execute_query(curs4, mage)
    necromancer_class = execute_query(curs5, necromancer)
    thief_class = execute_query(curs6, thief)
    armory_item = execute_query(curs7, item)
    armory_weapon = execute_query(curs8, weapons)

    print(results[:5])
    print(cleric_class[:5])
    print(fighter_class[:5])
    print(mage_class[:5])
    print(necromancer_class[:5])
    print(thief_class[:5])
    print(armory_item[:5])
    print(len(results))
    print(len(cleric_class))
    print(len(fighter_class))
    print(len(mage_class))
    print(len(necromancer_class))
    print(len(thief_class))
    print(len(armory_item))
    print(len(armory_weapon))
    print(len(armory_item) - len(armory_weapon))


