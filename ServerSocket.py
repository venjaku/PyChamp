#Importing Sockets
import socket

#Gave zero to listen for all communications.
host = "0.0.0.0"

#Collecting port number from user input
port = int(input("Enter port number --> "))

print("[+] Will be listening on port %s" %port)

#Creating a socket
server_socket = socket.socket()

#Binding IP with Port Number
server_socket.bind((host, port))

#Listener for Connection
server_socket.listen(2)

#Accepting Connections
conn, address = server_socket.accept()
print("[+] Client Connected: " + str(address))

#Infinite Loop
while True:

    #Receving message
    data = conn.recv(1024).decode()

    #If no data found, break the loop
    if not data:
        break

    #Printing Client Message
    print("Client message: " + str(data))

    #Collecting Server Response
    data = input("Enter response --> ")

    #Sending server response to client.
    conn.send(data.encode())

#Closing connection
conn.close()
