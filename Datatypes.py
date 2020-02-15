print("########################## Printing Dictionaries ##########################")
Info = {"Name": "Venkatesh Vanjaku", "Age": "22", "Height": "5.4", "Weight": "65"}

print("Before Changing Age")

print(Info)

Info["Height"] = 5.9

print("After Changing Age")

print(Info)

print("############################# Printing Tuples #############################")

FirstName = ("Venkatesh", "Rama", "Dinesh", "Karthik")

LastName = ("Vanjaku", "Chandra", "Reddy", "Krishna")

print(FirstName, "\n", LastName)

print("############################# Printing Lists ##############################")

Students = ["Venky", "Raju", "Kiran"]

print("Before Removing Student Raju")

print(Students)

print("After Removing Student Raju")

Students.remove(Students[1])

print(Students)
