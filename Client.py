import socket # Loads the socket module

HOST = '127.0.0.1' # The host to connect
PORT = 5534        # The port to connect

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a IPV4(AF_INET)/TCP(SOCK_STREAM) socket
client_socket.connect((HOST, PORT)) # Connect to the Server

data = client_socket.recv(1024).decode() # The data recived from client (the data recived are bytes type, so we need to decode)
print(data)
