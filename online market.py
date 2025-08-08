# write a example python program on online market to ask a user to do the following,
# A. how many items the user he wants to purchase,
# B. based on (A) ask the user to enter the name of the item and price and store them in different lists,
# C. print out the items in $ price from both lists, format-item, price ex manago:300
# then print out the total money spend

items = []
prices = []
num_items = int(input("How many items do you want to purchase? "))
for i in range(num_items):
    name = input("Enter name of item: ")
    price = int(input("Enter price in dollars): "))  # float for .99 or any .000 value or just use int
    items.append(name)
    prices.append(price)
for i in range(num_items):
    print(items[i], prices[i])
print(f"Items purchased:{items}:{prices}")  # print(f"Items purchase:{items[i]}:{prices[i]})
total = sum(prices)  # or Total = 0 ,  for price in prices  toatl = price + total
print("total amount purchased:", total)
