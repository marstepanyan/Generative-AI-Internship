import threading
import socket

host = 'localhost'
port = 8000
bytes_amount = 1024         # just for not using magic number

nickname = input('Choose a nickname :')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def client_receive():
    while True:
        # noinspection PyBroadException
        try:
            message = client.recv(bytes_amount).decode('utf-8')
            if message == 'my_nickname':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f"{nickname}: {input(' ')}"
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
