#Question: Write a program in python which will take budget from customer and bill all the items, if the total amount is within the budget place the order, otherwise show out of budget.

print("#############################")
print("★ POS by Venkatesh Vanjaku ★")
print("#############################")

ItemName = []
ItemPrice = []

budget = int(input("Customer Budget: "))
num = int(input("Number of Items: "))

for i in range(num):
    iname = input("Enter Item Name: ")
    iprice = input("Enter Item Price:  ")
    ItemName.append(iname)
    ItemPrice.append(iprice)

ItemNamesTup = tuple(ItemName[0:num])
ItemPriceTup = tuple(ItemPrice[0:num])

ItemsList = [ItemNamesTup, ItemPriceTup]
print("############################")
TotalPrice = 0
for j in range(num):
    print("Item Name: %s, Item Price: %s" %(ItemNamesTup[j], ItemPriceTup[j]))
    TotalPrice = TotalPrice + int(ItemPriceTup[j])
print("############################")
print("TOTAL PRICE = %d" %TotalPrice)

if (TotalPrice > budget):
    print("############################")
    print("Oops! Out of budget :(")
else:
    print("############################")
    print("Hola, order placed")
