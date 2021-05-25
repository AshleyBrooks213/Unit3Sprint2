"""Pymongo Assignment - Pipeline"""
import sqlite3
import pymongo 



PASSWORD = "yXJ18sSOLx57alCj"
DBNAME = "test"


#Local SQLite DB
EXTRACTION_DB = "rpg_db.sqlite3"


#Creating MongoDB Connection
def create_mongodb_connection(password=PASSWORD, dbname=DBNAME)
    client = pymongo.MongoClient(
        "mongodb+srv://AshleyBrooks213:{}@cluster0.5jw3p.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname)
    )
    return client


#Creating SQLite Connection
def create_sl_connection(extraction_db=EXTRACTION_DB)
    sl_conn = splite3.connect(extraction_db)
    return sl_conn


#Creating character documents for MongoDB
def doc_creation(db, sl_curs, character_table_query):
    characters = sl_curs.execute(character_table_query)
    for character in characters:
        doc = {
            "name": character[1],
            "level": character[2],
            "exp": character[3],
            "hp": character[4],
            "strength": character[5],
            "intelligence": character[6],
            "dexterity": character[7],
            "wisdom": character[8],
        }
        # Insert character document
        db.insert_one(doc)


# Function to show all documents in MongoDB
def show_all(db):
    all_docs = list(db.find())
    return all_docs


# SQlite Queries
GET_CHARACTER_TABLE = """
SELECT *
FROM charactercreator_character;
"""


if __name__ == "__main__":
    sl_conn = create_sl_connection()
    sl_curs = sl_conn.cursor()
    client = create_mongodb_connection()
    db = client.test.test
    db.drop({})
    doc_creation(db, sl_curs, GET_CHARACTER_TABLE)
    print(show_all(db))