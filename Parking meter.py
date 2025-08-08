print("Welcome to the Parking Meter!")
A

num = int(input("How many cars do you want to purchase? "))
items_price = {}
for i in range(num):
    items_name = input("Enter item name: ")
    price = float(input("Enter the price of the item"))
    items_price[items_name] = price
    print(items_name)
# print("total value",sum(items_price.values()))   # we can finsih the program in this way el;se the following
total = 0
for i, j in items_price.items():
    total = j + total

print(total)
