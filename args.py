# (*args) positive arguments it operates like a list
# (**kwargs) arbitaty keyword arguments it operates like a dictonary
'''def per(*args):
    sum=0
    for arg in args:
        sum = sum + arg
    average = sum/len(args)
    print(f"\n The average is: {average}") #or ('Average=',avt)

percentage(56,61,73)  '''


def fruit_price(**kwargs):
    sum = 0
    for arg in kwargs.values():
        sum = sum + arg
    # return sum
    return sum / len(kwargs)


k = fruit_price(mango=10, apple=20, banana=30)
print(k)
