#Scenario: Write a program in python to check whether the user input is a palindrome or not. It may be a number or name.

Input = input("Enter something here: ")
Reverse = ""

for i in Input:
    Reverse = i + Reverse
    
#In this for loop we are arranging all the letters in reverse order, to check remove the # in the next line
#print("Reversed string= %s"%Reverse)

if Reverse == Input:
    print("%s is a palindrome" %Input)
else:
    print("%s is not a palindrome" %Input)
