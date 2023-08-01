import threading
import socket

host = 'localhost'
port = 8000
bytes_amount = 1024         # just for not using magic number

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle_client(client):
    while True:
        # noinspection PyBroadException
        try:
            message = client.recv(bytes_amount)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(index)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} has left the Chat".encode('utf-8'))
            nicknames.remove(index)
            break


def receive():
    while True:
        print('server is running and listening...')
        client, address = server.accept()
        print(f"connection is established with {str(address)}")
        client.send('my_nickname'.encode('utf-8'))
        nickname = client.recv(bytes_amount)

        nicknames.append(nickname)
        clients.append(client)

        print(f"the nickname of this client is {nickname}".encode('utf-8'))
        broadcast(f"{nickname} has connected to the Chat".encode('utf-8'))
        client.send('you are now connected!'.encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()
