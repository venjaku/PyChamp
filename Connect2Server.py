#Importing Sockets
import socket

#Creating a test socket
TestSocket = socket.socket()
IP = input("Enter Server IP Address: ")
Port = int(input("Enter port number: "))

try:
    #Conneting to Server
    TestSocket.connect((IP,Port))

    # # Connected Succesfully
    # print("Connected Succesfully")

except Exception as exc:
    print("Error: %s" %exc)

else:
    # Connected Succesfully
    print("Connected Succesfully")

#Closing test socket
TestSocket.close()
print("Socket Closed")
