"""Unit3 Sprint2 MOD4- Assignment (Acid and database scalability tradeoffs)"""
"""Creating and inserting data with SQLite"""
import sqlite3
import psycopg2

# PostGreSQL Details - User & Default database 
DBNAME = "gvkythht"
# PostGreSQL Details - User & Defulat database
USER = "gvkythht"
#PostGreSQL Details - Password
PASSWORD = "IqY3WSXn5L9623EZc_tcO6WioHrAr9vc"
#PostGreSQL Details - Server
HOST = "isilo.db.elephantsql.com"


# Example of how to set up your code to create a table in SQL
CREATE_TABLE ="""
    CREATE_TABLE test_table(
        id SERIAL PRIMARY KEY,
        name VARCHAR(40) NOT NULL,
        data JSONB
    );
"""

#SQL Create Table Query 
CREATE_CHARACTER_TABLE = """
    CREATE_TABLE IF NOT EXISTS charactercreator_character (
        character_id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        level INT,
        exp INT,
        hp INT,
        strength INT,
        intelligence INT,
        dexterity INT,
        wisdom INT
    );
"""


# SQLite Queries
GET_CHARACTERS = """
SELECT *
FROM charactercreator_character;
"""



# Connect to PostGreSQL Database
def connect_pg_db(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST):
    pg_conn = psycopg2.connect(dbname=DBNAME, user=USER,
                                password=PASSWORD, host=HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

#Connect to SQLite Database
def connect_sl_db(dbname="rpg_db.sqlite3")
    sl_conn = sqlite3.connect(dbname)
    sl_curs = sl_conn.cursor()
    return sl_conn, sl_curs
    sl_curs.close()

# Execute Query
def execute_query(curs, query="SELECT * FROM charactercreator_character;"):
    curs.execute(query)
    return curs.fetchall()


def generate_characters_table(pg_conn, pg_curs, sl_curs):
    pg_curs.execute(CREATE_CHARACTER_TABLE)
    # list of characters from SQLite
    characters = sl_curs.execute(GET_CHARACTERS).fetchall()
    for character in characters:
        insert_character = """
        INSERT INTO charactercreator_character
        (name, level, ex, hp, strength, intelligence, dexterity, wisdom)
        VALUES {};
        """.format(character[1:]) # 0 indexed, but we are not including the id's
        pg_curs.execute(insert_character)
        
    print(insert_character)
    sl_curs.close()
    pg_curs.close()
    pg_conn.commit()






def create_table(conn):
    curs = conn.cursor()
    create_table = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name CHAR(20),
        favorite_number INTEGER,
        least_favorite_number INTEGER

    );
    """

    curs.execute(create_table)
    curs.close()
    conn.commit()


def insert_data(conn, data):
    curs = conn.cursor()
    for data_points in data:
        insert_data = """
        INSERT INTO students
        (name, favorite_number, least_favorite_number)
        VALUES {};
        """.format(data_points)
        curs.execute(insert_data)

    curs.close()
    conn.commit()


def show_all(conn):
    curs = conn.cursor()
    curs.execute("SELECT * FROM students")
    info = curs.fetchall()
    curs.close()
    return info

if __name__ == "__main__":
    data = [
        ("Nick", 77, 13),
        ("John", 101, 1010)
    ]
    conn = sqlite3.connect(mod)