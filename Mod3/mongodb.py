"""An example of how to import the character table into MongoDB from SQLite"""

import sqlite3
import pymongo


"""
Instantiate PASSWORD (from mongodb) 
and DBNAME (does not have to be same as what is in mongodb
"""
PASSWORD="aNsq9jZM56IBbAiT"
DBNAME="test2"


"""
Function that creates Mongodb connection
"""
def create_mdb_connection(password, dbname):
    client = pymongo.MongoClient(
        "mongodb+srv://Windows10-AshleyBrooks213:{}@cluster0.da32a.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname)
    )
    return client


"""Function that creates SQLite3 connection"""
def create_sl_connection(extraction_db="rpg_db.sqlite3"):
    sl_conn = sqlite3.connect(extraction_db)
    return sl_conn


"""
Function that executes SQLite 3 Queries
Takes in name of cursor and query
"""
def execute_query(curs, query):
    return curs.execute(query).fetchall()


"""
Creates DataBase using name of MongoDB Name 
and 
"""
def character_doc_creation(mongo_db, characters):
    # character - {id, name, level, exp, hp, strength, intelligence, dexterity, wisdom}
    for character in characters:
        character_doc = {
            "name": character[1], 
            "level": character[2], 
            "exp": character[3],
            "hp": character[4], 
            "strength": character[5], 
            "intelligence": character[6],
            "dexterity": character[7],
            "wisdom": character[8]
        }
        mongo_db.insert_one(character_doc) 


def show_sl_schema(table):
    schema = "PRAGMA table_info(" + table + ");"


def show_all(db):
    all_docs = list(db.find())
    return all_docs


GET_CHARACTERS = "SELECT * FROM charactercreator_character"


if __name__ == "__main__":
    sl_conn = create_sl_connection()
    sl_curs = sl_conn.cursor()
    client = create_mdb_connection(PASSWORD, DBNAME)
    db = client.test2
    characters = execute_query(sl_curs, GET_CHARACTERS) # returns list
    character_doc_creation(db.test2, characters)
    print(show_all(db.test2))





