ItemName = []
ItemPrice = []

num = int(input("How many Items: "))

for i in range(num):
    iname = input("Enter Item Name: ")
    iprice = input("Enter Item Price:  ")
    ItemName.append(iname)
    ItemPrice.append(iprice)

ItemNamesTup = tuple(ItemName[0:num])
ItemPriceTup = tuple(ItemPrice[0:num])

ItemsList = [ItemNamesTup, ItemPriceTup]
print(ItemsList)
print("############################")
TotalPrice = 0
for j in range(num):
    print("Item Name : %s, Item Price %s" %(ItemNamesTup[j], ItemPriceTup[j]))
    TotalPrice = TotalPrice + int(ItemPriceTup[j])
print("############################")
print("Price of Total Items %d" %TotalPrice)

if (TotalPrice > 100):
    print("############################")
    print("Oops! Out of budget :(")
else:
    print("############################")
    print("Hola, order placed")