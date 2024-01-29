#server code
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
LISTENER_LIMIT = 5
active_clients = []


def listen_for_message(client, username):
    while 1:
        response = client.recv(2048).decode('utf-8')
        if response != '':
            final_msg = username + '-' + response
            send_messages_to_all(username, final_msg)  # Corrected function call
        else:
            print(f"The message sent from client {username} is empty")


def send_message_to_client(client, message):
    client.sendall(message.encode())

# Function to send any new message to all the clients that are currently connected to this server
def send_messages_to_all(from_username, message):
    for user in active_clients:
        send_message_to_client(user[1], message)


# Function to handle a client
def client_handler(client):
    while 1:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            break
        else:
            print("Client username is empty")
    threading.Thread(target=listen_for_message, args=(client, username,)).start()

# Main function
def main():
    # Creating the socket class object
    # AF_INET: we are going to use IPV4 addresses
    # SOCK_STREAMS: we are using TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Provide the server with an address in the form of
        # host IP and port
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    # Set server limit
    server.listen(LISTENER_LIMIT)
    while 1:
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")

        threading.Thread(target=client_handler, args=(client,)).start()

if __name__ == '__main__':
    main()#server code
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
LISTENER_LIMIT = 5
active_clients = []


def listen_for_message(client, username):
    while 1:
        response = client.recv(2048).decode('utf-8')
        if response != '':
            final_msg = username + '-' + response
            send_messages_to_all(username, final_msg)  # Corrected function call
        else:
            print(f"The message sent from client {username} is empty")


def send_message_to_client(client, message):
    client.sendall(message.encode())

# Function to send any new message to all the clients that are currently connected to this server
def send_messages_to_all(from_username, message):
    for user in active_clients:
        send_message_to_client(user[1], message)


# Function to handle a client
def client_handler(client):
    while 1:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            break
        else:
            print("Client username is empty")
    threading.Thread(target=listen_for_message, args=(client, username,)).start()

# Main function
def main():
    # Creating the socket class object
    # AF_INET: we are going to use IPV4 addresses
    # SOCK_STREAMS: we are using TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Provide the server with an address in the form of
        # host IP and port
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    # Set server limit
    server.listen(LISTENER_LIMIT)
    while 1:
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")

        threading.Thread(target=client_handler, args=(client,)).start()

if __name__ == '__main__':
    main()