"""
Question:
1) Print Alphabets, collect a letter in the list as input from the user.
2) Collect an input how many letters to printed from the selected letter in the list
3) Print [Given Number] of letters from [Selected Letter]
"""

alphabets = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,a,v,w,x,y,z"

ListLetters = alphabets.split(",")

print(ListLetters)

name = input("Enter a letter in alphabets : ")

num = int(input("How many letters you want to print from %s : "%name))

print("[+] Confirmation: Selected Alphabet is %s and Number is %d" % (name, num))

# Index of given letter in list
i = ListLetters.index(name)
j = i
str2 = ''
for k in range(num):
    str2 += ListLetters[i]
    i = i + 1

print("Printing %s letters from %s = %s" % (num,name,str2))
print("### Credits: Venkatesh Vanjaku ###")
