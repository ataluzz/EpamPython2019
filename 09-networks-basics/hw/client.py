#client

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def receive():
    '''Handles receiving of messages'''
    while True:
        try:
            message = client.recv(1024).decode('utf8')
            print(message)
        except OSError: #if client left the chat
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 1111))
thread = threading.Thread(target=receive).start()
msg = ''

while msg != '*quit':
    msg = input()
    client.send(bytes(msg, 'utf8'))

client.close()
