#List all the alphabets, collect user input for a single letter, print the index number of the selected letter

#Assigning Alphabets to a variable
alphabets = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"

#To Identify the Index, I am splitting alphabets and storing in a list.
ListLetters = alphabets.split(",")

#Printing Splitted Alphabets
print(ListLetters)

#Collecting User Input of a letter
name = input("Enter a letter in alphabets : ")

#Assigning Index Value to a Variable
IndexNumber = ListLetters.index(name)

#Printing Index Number of Selected Letter
print("The Index number of %s is %s" %(name, IndexNumber))
