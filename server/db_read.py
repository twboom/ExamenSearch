import sqlite3
from contextlib import closing
import json


db_file = "db.sqlite3"

data = json.load(open("data.json", "r"))


# Load the schema in the database
with closing(sqlite3.connect(db_file)) as connection:
    with closing(connection.cursor()) as cursor:
        with open("schema.sql", "r") as f:
            schema = f.read()
            statements = schema.split(";")
            for statement in statements:
                cursor.execute(statement)


# Search for a file
def query(keywords=[], levels="*", subjects="*", years="*", document_types="*", periods="*") -> list:
    with closing(sqlite3.connect(db_file)) as connection:
        with closing(connection.cursor()) as cursor:
            results = []
            
            for keyword in keywords:
                keyword = str(keyword).lower()
                query = "SELECT * FROM page WHERE text_content LIKE ?"
                data = (
                    f"%{keyword}%",
                )
                cursor.execute(query, data)
                results += cursor.fetchall()
            return results


if __name__ == "__main__":
    result = query(keywords=["hart", "lees"])
    # result = [result[1] for result in result]
    print(len(result))