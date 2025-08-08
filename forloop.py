def a():


    for i in range(1, 1001):
        print("hello world",
              i)  ### printing hellow world 1000, where i is the variable range(start,stop): stop value always n-1
        # for i in range(start,stop)

        # sum the numbers 0 to 999 ?????


def b():


    sum = 0
for i in range(0, 1000):
    sum = i + sum
    print(sum)


def C():
    for i in range(2, 1000, 2):  # to print the even number in a range   # for i in range(start,stop,step or count):
        print(i)


def d():  # get strat and stop input from the user
    start = int(input("Enter your starting number: "))
    end = int(input("Enter your ending number: "))

    for i in range(start, end):
        print(i)


d()
