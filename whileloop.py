'''password=input("Enter your password: ")
while password == "PASSWORD":
    print("Permission granted")
    break
print("wrong password")  # while granted print one else print an another dont need else to be used just worng password ####break is must if granted

#if password != "PASSWORD":  # Not equal to
 #   print("Wrong Password. Please try again")'''

'''sum = 0     # need a while loop for this for statement
for i in range(5):
    sum =i+sum
    print (sum)'''

sum = 0
i = 0
while i < 5:
    sum += i
    i += 1
print(sum)
