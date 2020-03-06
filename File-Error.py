#For this code, you need to download users.txt file from this link 
try:
    file = open ("users.txt", "r")
    
except:
    print("Something went wrong!")
    
else:
    for i in file:
        print("Checking %i"%i)
    file.close()
    print("File Closed")
    
finally:
    print("Reading Completed")
