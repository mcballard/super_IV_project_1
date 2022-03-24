import os
from psycopg import connect, OperationalError

def create_connection():
    try:
        conn = connect(
            host=os.environ.get("HOST"),
            dbname=os.environ.get("DBNAME"),
            user=os.environ.get("DBUSER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
        )
        return conn
    except OperationalError as e:
        raise OperationalError("Could not connect to database")

connection = create_connection()
print(connection)
