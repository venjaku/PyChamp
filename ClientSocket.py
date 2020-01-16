#Importing Sockets
import socket

#Collecting Server IP Address
host = input("Enter Server IP Address --> ")

#Collecting an Integer Input of Port Number
Port = int(input("Enter the port Number --> "))

#Creating Client Socket
client_socket = socket.socket()

#Connecting to Server
client_socket.connect((host, Port))
print("[+] Connected to Server %s, on port %d" %(host,Port))

#Collecting message to send to server
message = input("Enter the message --> ")

#While condition to check for exit in message
while message.lower().strip() != 'exit':
    #Sending message to server
    client_socket.send(message.encode())

    #Receiving message from server
    data = client_socket.recv(1024).decode()

    #Printing server message
    print("Server message: %s" %data)

    #Collecting response for client
    message = input("Enter response (type exit to quit) --> ")

#Closing Socket
client_socket.close()