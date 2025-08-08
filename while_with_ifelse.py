'''
correct format
average_marks = int(input("Enter your marks (0–100): "))
while average_marks < 0 or average_marks > 100:
    print(f"{average_marks} is invalid.")
    average_marks = int(input("Please enter marks between 0 and 100: "))

print(f"Valid marks entered: {average_marks}")

'''  # testing below

average_marks = int(input("Enter your marks average_marks: "))
while (0 > average_marks > 100):  # or or and
    print(average_marks)
    print("Invalid average_marks")
    average_marks = int(input("Enter your marks average_marks: "))

if average_marks < 50:
    print("fail")
else:
    print("pass")
if average_marks >= 80:
    print("Grade: Super class")
elif average_marks >= 60:
    print("Grade: Awesome class")
elif average_marks >= 50:
    print("Grade: Average class")
else:
    print("Grade: Need more class")
