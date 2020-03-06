#For this code, you need to download users.txt file from this link ( https://github.com/vvrofficial/PyChamp/blob/master/users.txt )

try:
    file = open ("users.txt", "r")
    
except:
    print("Something went wrong!")
    
else:
    for i in file:
        print("Checking %i"%i)
    file.close()
    print("Reading Completed")
    
finally:
    print("Quitting Process")
