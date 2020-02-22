"""
1. Create a List of Students
2. Collect First Names of Four Different Students
3. Append One by One to the Students List
4. Print Students List
"""

#Declaring Blank Students List
Students = []

#Collecting Students Namesto Different Variables
FirstStudent = input("Enter first student's first name: ")
SecondStudent = input("Enter second student's first name: ")
ThirdStudent = input("Enter third student's first name: ")
FourthStudent = input("Enter fourth student's first name: ")

#Appending Allt the Collected Names to Students List.
Students.append(FirstStudent)
Students.append(SecondStudent)
Students.append(ThirdStudent)
Students.append(FourthStudent)

#Printing the Students List
print (Students)

print ("Credits: Venkatesh Vanjaku")
