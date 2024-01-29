Basic Text-Based Chat Application
This is a simple text-based chat application created using Python, where two users can exchange messages in real-time using the command line. The application follows a client-server model for message exchange.

Features
Real-Time Messaging: Users can exchange messages instantly with each other.
Client-Server Architecture: Implements a basic client-server model for message exchange.
Username Support: Users can enter their usernames before starting the chat.
Simple Interface: Utilizes the command line for communication between users.
Components
Server Code
The server code (server.py) listens for incoming connections from clients and handles message distribution between clients.
Client Code
The client code (client.py) connects to the server and facilitates message exchange between users.
Usage
Clone the repository to your local machine.

Make sure you have Python installed.

Run the server code (server.py):

Copy code
python server.py
Run two instances of the client code (client.py):

Copy code
python client.py
Enter a username for each client when prompted.

Start sending messages between the clients.

Requirements
Python 3.x
Threading (for handling multiple clients simultaneously)
Sockets (for communication between client and server)
Configuration
Update the HOST and PORT variables in both server.py and client.py to match your server's address and port.
Note
This application is intended for educational purposes and demonstrates basic client-server communication in Python.
Author
Kasula Devika
