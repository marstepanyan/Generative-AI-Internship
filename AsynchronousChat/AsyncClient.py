import asyncio
import websockets


async def receive_message(websocket):
    try:
        while True:
            message = await websocket.recv()
            print(message)
    except websockets.ConnectionClosed:
        print("Connection to the server is closed.")


async def send_message(websocket):
    try:
        while True:
            message = f"{await asyncio.get_event_loop().run_in_executor(None, input, ' ')}"
            await websocket.send(message)
    except websockets.ConnectionClosed:
        print("Connection to the server is closed.")


async def main():
    async with websockets.connect("ws://localhost:8765") as websocket:
        username = input("Enter your username: ")
        await websocket.send(username)
        print("Connected to the server.")

        receive_task = asyncio.create_task(receive_message(websocket))
        send_task = asyncio.create_task(send_message(websocket))

        await asyncio.gather(receive_task, send_task)


if __name__ == "__main__":
    asyncio.run(main())
