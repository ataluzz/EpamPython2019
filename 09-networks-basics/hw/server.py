import socket
from threading import Thread


def accept_connections():
    '''Handling incoming connections'''
    while True:
        client, client_address = server.accept()
        print("Received the connection from:", client_address)
        client.send(bytes("Nice to meet you! Type your name and press Enter", "utf-8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    '''Handles a single client connection'''
    name = client.recv(BUFSIZ).decode("utf8")
    welcome_msg = f"Welcome {name}! For quitting from chat, type *quit.\n" \
              f"To get list of chat members, type *members.\n" \
              f"To send private message, type @name of chat member and your message."
    client.send(bytes(welcome, "utf8"))
    msg = f'{name} has joined the chat'
    broadcast(bytes(msg, 'utf8'))
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZ)
        if msg == bytes('*quit', 'utf8'):
            client.send(bytes('*quit', 'utf8'))
            client.close()
            del clients[client]
            broadcast(bytes(f'{name} has left the chat', 'utf8'))
            break
        elif msg == bytes('*list', 'utf8'):
            members_list = '\n'.join(list(clients.values()))
            client.send(bytes(members_list, 'utf-8'))
        elif msg.startswith(bytes('@', 'utf8')):
            msg_to_member(client, msg)
        else:
            broadcast(msg, name + ": ")


def broadcast(msg, prefix=''):
    '''Broadcast message to all members'''
    for client in clients:
        client.send(bytes(prefix, 'utf8') + msg)

def msg_to_member(client, msg):
    '''Private message to specific member'''
    for client, name in clients.items():
        if msg.startswith(bytes(f'@{name}', 'utf8')):
            msg_data = str(msg[len(name)+2:])
            message = f'Message from {clients[client]}: {msg_data}'
            client.send(bytes(message, 'utf8'))


clients = {}
addresses = {}

IP_address = '0.0.0.0'
Port = 5060
BUFSIZ = 2048

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((IP_address, Port))

if __name__ == '__main__':
    server.listen(20)
    print('Waiting for incoming connections...')
    ACCEPT_THREAD = Thread(target=accept_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    server.close()

