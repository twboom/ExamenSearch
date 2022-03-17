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
def query(keywords=[], levels="*", subjects="*", years="*", document_types="*", periods="*"):
    with closing(sqlite3.connect(db_file)) as connection:
        with closing(connection.cursor()) as cursor:
            query = """
                SELECT file_id
                FROM page
                WHERE CONTAINS(text_content, {keywords})
            """
            data = (
                keywords
            )
            cursor.execute(query)
            return cursor.fetchall()


if __name__ == "__main__":
    query(keywords=["score"])