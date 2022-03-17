import asyncio
import websockets
import json

from db_read import search, get_total_files, get_total_pages


async def send_message(websocket, data):
    data = json.dumps(data)
    await websocket.send(data)


async def handle_query(websocket, data):
    data = data["data"]
    if not "keywords in data":
        send_message(websocket, {
            "subject": "ERROR",
            "data": "No keywords found on 'data' attribute"
        })
    
    keywords = data["keywords"]
    results = search(keywords=keywords)

    await send_message(websocket, {
        "subject": "QUERY_RESPONSE",
        "data": {
            "total_results": len(results),
            "total_files": get_total_files(),
            "total_pages": get_total_pages(),
            "results": results,
        }
    })


async def handle_message(websocket, message):
        try:
            data = json.loads(message)
            if data["subject"] == "QUERY":
                await handle_query(websocket, data)
        except Exception as e:
            print(e)
            await send_message(websocket, {
                "subject": "ERROR",
                "data": {
                    "message": "Exception occured while handling the message",
                }
            })


async def handle_connection(websocket, path):
    data = {
        "subject": "CONNECTION",
        "data": "CONNECTED"
    }
    await send_message(websocket, data)
    async for message in websocket:
        await handle_message(websocket, message)


async def main():
    async with websockets.serve(handle_connection, "localhost", 8080):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())