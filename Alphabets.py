"""
Question:
1) Print Alphabets, collect a letter in the list as input from the user.
2) Collect an input how many letters to printed from the selected letter in the list
3) Print [Given Number] of letters from [Selected Letter]
"""

#Assigning Alphabets to a variable
alphabets = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"

#To Identify the Index, I am splitting alphabets and storing in a list.
ListLetters = alphabets.split(",")

#Printing Splitted Alphabets
print(ListLetters)

#Collecting User Input of a letter
name = input("Enter a letter in alphabets : ")

#User Input to know the number of letters to be printed
num = int(input("How many letters you want to print from %s : "%name))

#Confirmation to the User
print("[+] Confirmation: Selected Alphabet is %s and Number is %d" % (name, num))

# Index of given letter in list
i = ListLetters.index(name)
j = i
str2 = ''

#For loop to capture selected number of letters from selected letter.
for k in range(num):
    str2 += ListLetters[i]
    i = i + 1

print("Printing %s letters from %s = %s" % (num,name,str2))
print("### Credits: Venkatesh Vanjaku ###")
print("### Special Thanks to Vladi Fidchuk & Rama Chandra Prasad Mylapuram ###")
