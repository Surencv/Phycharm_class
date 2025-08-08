def staff_info():
    staff_list = []
    count = input("\nEnter a how many staff details u want to enter:")
    counter = 10000
    for i in range(count):
        print(f"\n Enter the staff detail :")
        name = input("Enter a staff name:")
        id = input("Enter a staff id:")
        DOB = input("Enter DOB: MM/DD/YYYY in this format:")
        counter += 1
        staff_list.append({"staff name": name, "staff id": id, "staff DOB": DOB, "Requisition ID": counter})
    print("\n Staff Details :")
    pr
