def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


def assign_grade(average):
    if average >= 80:
        return "Super class"
    elif average >= 60:
        return "Awesome class"
    elif average >= 50:
        return "Average class"
    else:
        return "Need more class"


def main():
    marks = []
    subjects = ['A', 'B', 'C', 'D']

    for subject in subjects:
        score = int(input(f"Enter your marks {subject}: "))
        marks.append(score)

    total, average = calculate_average(marks)
    print("Total Marks:", total)
    print("Average Marks:", average)

    result = "Pass" if average >= 50 else "Fail"
    print("Result:", result)

    grade = assign_grade(average)
    print("Grade:", grade)


main()
