#Question: Write a program in python which will take budget from customer and bill all the items, if the total amount is within the budget place the order, otherwise show out of budget.

print("#############################")
print("★ POS by Venkatesh Vanjaku ★")
print("#############################")

#Declaring Reusale Lists
ItemName = []
ItemPrice = []

#Collecting Customer Budget
budget = int(input("Customer Budget: "))

#Collecting No.Of Items in Basket
num = int(input("Number of Items: "))

#Adding Items to the Bills
for i in range(num):
    iname = input("Enter Item Name: ")
    iprice = input("Enter Item Price:  ")
    ItemName.append(iname)
    ItemPrice.append(iprice)

ItemNamesTup = tuple(ItemName[0:num])
ItemPriceTup = tuple(ItemPrice[0:num])

#Printing Item's List
ItemsList = [ItemNamesTup, ItemPriceTup]
print("############################")

#Calculating Total Price using For Loop
TotalPrice = 0
for j in range(num):
    print("Item Name: %s, Item Price: %s" %(ItemNamesTup[j], ItemPriceTup[j]))
    TotalPrice = TotalPrice + int(ItemPriceTup[j])
print("############################")
print("TOTAL PRICE = %d" %TotalPrice)

#Comparing the Bill with Budget
if (TotalPrice > budget):
    print("############################")
    print("Oops! Out of budget :(")
else:
    print("############################")
    print("Transaction Successfully Completed")
    print("## THANK YOU, VISIT AGAIN ##")
