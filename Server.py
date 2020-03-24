import socket # Loads the socket module

HOST = '127.0.0.1' # The host to bind
PORT = 5534        # The port to bind

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a IPV4(AF_INET)/TCP(SOCK_STREAM) socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True) # Prevent the "Address already in use" error
server_socket.bind((HOST, PORT)) # The server will listen on 127.0.0.1:5534
server_socket.listen() # Start to listen the connections

while True: # Start a while loop(infinity loop)
    client_connection, client_address = server_socket.accept() # Accept the connection
    print(f'{client_address[0]}{client_address[1]} --> Connected') # Print who is connected
    client_connection.send(b'Welcome to my Server!') # Send a message to the client (the message need to be bytes not str)
