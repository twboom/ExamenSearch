import sqlite3
from contextlib import closing

db_file = "db.sqlite3"


connection = sqlite3.connect(db_file)
cursor = connection.cursor()

def close():
    connection.close()