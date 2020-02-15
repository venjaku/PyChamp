"""
1. Create a List of Students
2. Collect First Names of Four Different Students
3. Append One by One to the Students List
4. Print Students List
"""
Students = []
FirstStudent = input("Enter first student's first name: ")
SecondStudent = input("Enter second student's first name: ")
ThirdStudent = input("Enter third student's first name: ")
FourthStudent = input("Enter fourth student's first name: ")
Students.append(FirstStudent)
Students.append(SecondStudent)
Students.append(ThirdStudent)
Students.append(FourthStudent)
print (Students)


#The above program can also be written through While Loop, but it will run until you type exit. Remove """ these before and after the program

"""
Students = []
y = input("Enter student's name: ")
while (y != "exit"):
    Students.append(y)
    y = input("Enter student's name: ")
print (Students)
"""
