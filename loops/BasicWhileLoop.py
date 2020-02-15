"""
Task:
1) Create program using while loop to collect student's names.
2) Create a list and append student names to that list
3) Exit from the loop if the user enters exit
4. Print the Students List
"""
Students = []
y = input("Enter student's name: ")
while (y != "exit"):
    Students.append(y)
    y = input("Enter student's name: ")
print (Students)
