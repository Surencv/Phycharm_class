''''cars=["A","B","c","d"]   #slicing an item from this list
print(cars[:1]) #only the position 1 was displayed
print(cars[1:2])# here only position 1 to 2 which is just 1 will be diplayed'''
# deleet and add numbers in a list
# create an empty list called scroes and populate it with 20,10,5,10,20
# then delete the number 5 and then addd 30 to the list in python
'''scores=[]
scores.extend([20, 10, 5, 10, 20])
scores.remove(5) 
scores.append(30)
print(scores)'''

# combining the total for the scores

'''scores=[]
scores.extend([20, 10, 5, 10, 20])
scores.remove(5)
scores.append(30)
print(scores)
total = 0 #- You're initializing a variable called total to hold the sum of all the values.
# We start at zero because we haven't added anything yet.
for scores in scores: #- This is a loop that goes through each item in the list scroes one by one. On each pass:
#The variable score temporarily holds one number from the list.
    total = scores + total #- It adds the current score to the running total.or toatl+=scores
print("Total score:", total) '''

# numbers[40,-20,60,4,-4,-8] write a python program to separate the +ve and the -ve using
# if statement  to create the list either the positive or negative numbers
positive_numbers = []
negative_numbers = []
numbers = [40, -20, 60, 4, -4, -8]
for i in numbers:
    if i > 0:
        positive_numbers.append(i)  # .append adds the obj to the list
    else:
        negative_numbers.append(i)
print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)
# and add the numbers in positive and negative values later
