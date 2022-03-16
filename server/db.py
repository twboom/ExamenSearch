import sqlite3
from contextlib import closing


db_file = "db.sqlite3"


# Load the schema in the database
with closing(sqlite3.connect(db_file)) as connection:
    with closing(connection.cursor()) as cursor:
        with open("schema.sql", "r") as f:
            schema = f.read()
            statements = schema.split(";")
            for statement in statements:
                cursor.execute(statement)


# Load the data in the database
def new_file(url, year, subject, level, period, document_type):
    with closing(sqlite3.connect(db_file)) as connection:
        with closing(connection.cursor()) as cursor:
            query = "INSERT or IGNORE INTO file (url, year, subject, level, period, document_type) VALUES (?, ?, ?, ?, ?, ?)"
            data = (
                url,
                year,
                subject,
                level,
                period,
                document_type,
            )
            cursor.execute(query, data)
            connection.commit()

def new_page(file_id, page_number, text_content):
    with closing(sqlite3.connect(db_file)) as connection:
        with closing(connection.cursor()) as cursor:
            query = "INSERT or IGNORE INTO page (file_id, page_number, text_content) VALUES (?, ?, ?)"
            data = (
                file_id,
                page_number,
                text_content
            )
            cursor.execute(query, data)
            connection.commit()