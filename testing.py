def year1():
    A = int(input("Enter your marks A: "))
    B = int(input("Enter your marks B: "))
    C = int(input("Enter your marks C: "))
    D = int(input("Enter your marks D: "))
    total_marks = A + B + C + D
    print("Total Marks", total_marks)
    average_marks = total_marks / 4
    print("Average Marks", average_marks)
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


def year2():
    A = int(input("Enter your marks A: "))
    B = int(input("Enter your marks B: "))
    C = int(input("Enter your marks C: "))
    D = int(input("Enter your marks D: "))
    E = int(input("Enter your marks E: "))
    total_marks = A + B + C + D + E
    print("Total Marks", total_marks)
    average_marks = total_marks / 5
    print("Average Marks", average_marks)
    if average_marks < 50:
        print("fail")
    else:
        print("pass")


# print(year2())
# print(year1())


'''average_marks = int(input("Enter your marks average_marks: "))
while (average_marks < 0 or average_marks > 100):      #or or and
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
    print("Grade: Need more class") #test statement '''
