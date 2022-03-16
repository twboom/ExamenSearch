import asyncio
import websockets
import json


async def send_message(websocket, data):
    data = json.dumps(data)
    await websocket.send(data)


async def handle_message(websocket, path):
    data = {
        "subject": "CONNECTION",
        "data": "CONNECTED"
    }
    await send_message(websocket, data)
    async for message in websocket:
        data = json.loads(message)
        print(data)
        await send_message(websocket, data)


async def main():
    async with websockets.serve(handle_message, "localhost", 8080):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())