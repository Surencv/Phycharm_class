'''def staff_info():
    staff_list = []
    c = int(input("\nEnter a how many staff details u want to enter:"))
    counter = 10000
    for i in range(c):
        print(f"\n Enter the staff detail :")
        name = input("Enter a staff name:")
        id = int(input("Enter a staff id:"))
        DOB = input("Enter DOB: MM/DD/YYYY in this format:")
        counter += 1
        staff_list.append({"staff name": name, "staff id": id, "staff DOB": DOB, "Requisition ID": counter})
    print("\n Staff Details :")
    for staff in staff_list:
        print(f"\nStaff Name:", staff.get("staff name"))
        print(staff.get("staff id"))
        print(staff.get("staff DOB"))
        print(staff.get("Requisition ID"))


staff_info()'''


# def staff_info()
# data_cur=date.today()
# except you can say the sytem what to do
def d():
    try:
        num1 = float(input("Enter number1: "))
        num2 = float(input("Enter number2: "))
        return (num1 / num2)
    except ZeroDivisionError:
        return "Cannot divide by zero"


d()
