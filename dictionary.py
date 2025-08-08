# another form of a data structure used to store values in pai which is called key value pair
# we use {} for it key:value, key is always unique can repeate it again {A:10,b=20,c=10} u cant replicate A again in it
# dict_var={key1:value,Key2:value,....}if the key is variable use ""
# also dictnary can be empty like Score={} and provide input later on like score [simon]=70
# capture value later
# .get() will get the value
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
