"""Unit 3 - Sprint 2 - MOD 2"""

import pandas as pd 
import psycopg2


"""Info from Elephant PostgreSQL"""
dbname = 'iotfyowi'
user = 'iotfyowi'
password = 'cWBH7UakBhZuVGYNZqbGSBXFEfeX8DQB'
host = 'ziggy.db.elephantsql.com'


"""1. Create connection"""
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)


"""2. Create cursor"""
pg_curs = pg_conn.cursor()


"""Read in dataframe"""
df = pd.read_csv("titanic.csv")


"""Turn Pclass and Survived into strings"""
df['Pclass'] = df['Pclass'].apply(lambda i: str(i))
df['Survived'] = df['Survived'].apply(lambda i: str(i))


"""Turn Dataframe into list of tuples"""
tups = list(df.itertuples(index=False))


CREATE_PASSENGER_CLASS_TYPE = """
DROP TYPE IF EXISTS passenger_class_type CASCADE;
CREATE TYPE passenger_class_type AS ENUM ('1', '2', '3');
"""
"""Execute Create_TABLE query"""
pg_curs.execute(CREATE_PASSENGER_CLASS_TYPE)


CREATE_PASSENGER_SEX_TYPE = """
DROP TYPE IF EXISTS passenger_sex_type CASCADE;
CREATE TYPE passenger_sex_type AS ENUM ('male', 'female');
"""
"""Execute Create_TABLE query"""
pg_curs.execute(CREATE_PASSENGER_SEX_TYPE)


"""Create Table PostgreSQL Query"""
CREATE_TABLE = """
    DROP TABLE IF EXISTS titanic_data CASCADE;
    CREATE TABLE IF NOT EXISTS titanic_data (
        id SERIAL PRIMARY KEY,
        survived BOOLEAN NOT NULL,
        pclass passenger_class_type,
        name VARCHAR(100),
        sex passenger_sex_type,
        age SMALLINT,
        siblings_spouses_aboard SMALLINT,
        parents_children_aboard SMALLINT,
        fare REAL
);
"""

"""Execute Create_TABLE query"""
pg_curs.execute(CREATE_TABLE)


"""Commit New Table on the Connection"""
pg_conn.commit()


"""Insert data into new table using PostgreSQL insert statement"""
INSERT_TUPLES_INTO_TABLE = """
INSERT INTO titanic_data
    (survived, pclass, name, sex, age,
    siblings_spouses_aboard, parents_children_aboard, fare)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
    """

"""For loop that inserts each tuple into new table"""
for tup in tups:
    pg_curs.execute(INSERT_TUPLES_INTO_TABLE, tup)


"""Commit inserted rows(tuples) on the Connection"""
pg_conn.commit()

pg_curs.close()
pg_curs2 = pg_conn.cursor()

"""Check to make sure insertion of rows was successful"""
SELECT_ALL_FROM_NEW_TABLE = """
    SELECT * FROM titanic_data;
"""


"""Execute Query"""
# -> does not work. It will not return database. Not sure why.
# check to see if fetchall works for PostgreSQL
#response = pg_curs2.execute(SELECT_ALL_FROM_NEW_TABLE).fetchall()

#print(response)




