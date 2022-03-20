import sqlite3
from contextlib import closing
import json
import asyncio


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


# Asynchronous  fetchall query
async def fetchall_async(query, data):
    with closing(sqlite3.connect(db_file, check_same_thread=False)) as connection:
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None, lambda: connection.cursor().execute(query, data).fetchall()
        )


# Search for a file
async def query(keywords=[]) -> list:
    query = "SELECT * FROM page"
    data = []
    for keyword in keywords:
        data.append(f"%{keyword}%")
        if keywords.index(keyword) == 0:
            query += " WHERE text_content LIKE ?"
            continue
        query += " OR text_content LIKE ?"
    data = tuple(data)
    return await fetchall_async(query, data)


async def get_files(page_list=[]):
    files = []
    for page in page_list:
        file_id = page[1]
        query = "SELECT * FROM file WHERE id = ?"
        data = (file_id,)
        files += await fetchall_async(query, data)
    return files
            


async def search(keywords) -> list:
    query_results = await query(keywords=keywords)
    files = await get_files(page_list=query_results)

    search_result = []
    for qr in query_results:
        file = files[query_results.index(qr)]
        result = {
            "page_number": qr[2] + 1,
            "url": file[1],
            "year": file[2],
            "subject": file[3],
            "level": file[4],
            "period": file[5],
            "document_type": file[6]
        }
        search_result.append(result)
    
    return search_result


# Stats
def get_total_files() -> int:
    with closing(sqlite3.connect(db_file)) as connection:
        with closing(connection.cursor()) as cursor:
            query = "SELECT COUNT(url) FROM file"
            cursor.execute(query)
            return cursor.fetchone()[0]

def get_total_pages() -> int:
    with closing(sqlite3.connect(db_file)) as connection:
        with closing(connection.cursor()) as cursor:
            query = "SELECT COUNT(text_content) FROM page"
            cursor.execute(query)
            return cursor.fetchone()[0]


if __name__ == "__main__":
    sr = search(keywords=["hartcyclus"])
    print(len(sr))
    print(sr[0])
    # print(get_total_files())
    # print(get_total_pages())