# Program Name: Benel-ProgramA.py
# Course: IT3883/Section 01
# Student Name: Benel Kawata
# Assignment Number: Assignment 4
# Due date: 10/06/2026
# Purpose:
# This program acts as a client in a socket communication. It prompts the user for a string,
# It sends the string to a server, receives the modified string (converted to uppercase) from the server,
# and displays the modified string to the user once everything went through.

# Here, an import statement is used to include the socket module, which will provide the necessary functions and classes for creating and managing sockets in Python.
import socket

# These lines of code are the same as in Program B, but with a different purpose. The client connects to the server, sends a message, and receives a response.
HOST = "127.0.0.1"      # This points to the localhost, which means the client will connect to a server running on the same machine.
PORT = 45000            # This points to the port number that the client will use to connect to the server - It must match the port number used by the server to listen for connections.

# This line creates a socket object for the client using IPv4 and TCP protocols.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This line connects the client socket to the server using the specified host and port.
client_socket.connect((HOST, PORT))

# This line prompts the user to enter a message, which will be sent to the server for processing. The input is stored in the variable 'message'.
message = input("Enter a message: ")

# This line sends the user's message to the server after encoding it to bytes. The server will receive this message and process it.
client_socket.send(message.encode())

# This line receives the response from the server, which is expected to be the modified string (converted to uppercase). The received data should be decoded from bytes to a string and stored in the variable 'response'.
response = client_socket.recv(1024).decode()

# It displays the server's response to the user, which would be the modified string that was sent back from the server after processing the original message.
print("\nResponse from server:")
print(response)

# Then, it closes the connection
client_socket.close()

#Note: The client program is designed to work in conjunction with the server program (Program B). The server must be running and listening for connections before the client can successfully connect and send a message.
#Therefore, I suggest running the server program first, and then running the client program to test the communication between them. Both from different terminals or command prompts. 