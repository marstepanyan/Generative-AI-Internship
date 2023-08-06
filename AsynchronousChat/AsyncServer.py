import asyncio
import websockets
import datetime

message_history_max = 10
message_history = []

connected_clients = {}


async def handle_client(websocket):
    global connected_clients
    username = await authenticate_user(websocket)
    if not username:
        return

    connected_clients[username] = websocket

    try:
        while True:
            message = await websocket.recv()
            if message.startswith("@"):
                await send_private_message(username, message)
            else:
                await handle_message(username, message)
    except websockets.ConnectionClosed:
        pass


async def authenticate_user(websocket):
    username = await websocket.recv()
    if username.strip() == "" or username in connected_clients:
        await websocket.send("Username not available. Please choose another one.")
        return await authenticate_user(websocket)
    print(f"User {username} connected to server.")
    return username


async def handle_message(sender, message):
    global message_history
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"[{timestamp}] {sender}: {message}"

    message_history.append(formatted_message)
    if len(message_history) > message_history_max:
        message_history = message_history[-message_history_max:]

    print(formatted_message)
    await broadcast_message(formatted_message)


async def send_private_message(sender, message):
    recipient_username, _, content = message.partition(" ")
    recipient = connected_clients.get(recipient_username[1:])
    if recipient:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"[{timestamp}] {sender} (private): {content}"
        await recipient.send(formatted_message)


async def broadcast_message(message):
    for client in connected_clients.values():
        await client.send(message)


async def start_server():
    server = await websockets.serve(handle_client, "localhost", 8765)
    print("Server started.")
    await server.wait_closed()

asyncio.run(start_server())
