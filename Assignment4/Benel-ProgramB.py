# Program Name: Benel-ProgramB.py
# Course: IT3883/Section 01
# Student Name: Benel Kawata
# Assignment Number: Assignment 4
# Due date: 10/06/2026
# Purpose:
# This program acts as a server in a socket communication. It listens for incoming connections from clients
# Once it receives a string from a client, it converts the string to uppercase and sends it back to the client. 
# The server will continues to listen for new connections until the program is manually stopped.

#An import statement is used to include the socket module, which will provide the necessary functions and classes for creating and managing sockets in Python.
import socket

# These lines identify the host and port for the server to listen on.
HOST = "127.0.0.1"      # This points to the localhost, which means the server will only accept connections from the same machine.
PORT = 45000            # This points to the port number that the server will listen on. It must match the port number used by the client to connect to the server.

# This line creates a socket object for the server using IPv4 and TCP protocols.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This line binds the server socket to the specified host and port.
server_socket.bind((HOST, PORT))

# In this line, the server socket is set to listen for incoming connections. The argument '1' specifies the maximum number of queued connections.
server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}")

# The server is told to accept a connection from a client. This line blocks until a client connects, at which point it returns a new socket object (conn) for the connection and the address of the client (addr).
conn, addr = server_socket.accept()

print(f"Connected by {addr}")

# If a client is connected, the server receives a message from the client. The received data is decoded from bytes to a string and stored in the variable 'message'.
message = conn.recv(1024).decode()

print(f"Received from client: {message}")

# Once the message is received, the server converts the string to uppercase and stores it in the variable 'response'.
response = message.upper()

print(f"Sending back: {response}")

# The server will then send the modified string back to the client after encoding it to bytes.
conn.send(response.encode())

# After sending the response, the server closes the connection with the client and then closes the server socket, effectively shutting down the server.
conn.close()
server_socket.close()

print("Server closed.")

# Note: The server program is designed to work in conjunction with the client program (Program A). The server must be running and listening for connections before the client can successfully connect and send a message. 
# Therefore, I suggest running the server program first, and then running the client program to test the communication between them. 
# Both from different terminals or command prompts.