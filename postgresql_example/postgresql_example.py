"""Module 2: example with PostGreSQL"""

import psycopg2
from queries import CREATE_TABLE_STATEMENT, INSERT_STATEMENT

#DO NOT PUT THIS INFO ON GITHUB
#PostGreSQL Details  - User & Default database
DBNAME = "vceuyerc"
#PostGreSQL Details - User & Default database
USER = "vceuyerc"
# Password
PASSWORD = "dprhv5SxTCkr8gQk5Jh0aKfIpw2PjnLa"
HOST = "suleiman.db.elephantsql.com "

def connect_db(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST):
    pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, 
                            password=PASSWORD, host=HOST) 
    pg_curs = pg_conn.cursor()
    return pg_conn

def execute_query(curs, query):
    curs.execute(query)

if __name__ == "__main__":
    pg_conn, pg_curs = connect_db()
    execute_query(pg_curs, CREATE_TABLE_STATEMENT)
    execute_query(pg_curs, INSERT_STATEMENT)
    pg_conn.commit()
