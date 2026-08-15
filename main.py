def add_student():
    print("================================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("================================")

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    department = input("Enter department: ")

    mark1 = int(input("Enter mark 1: "))
    mark2 = int(input("Enter mark 2: "))
    mark3 = int(input("Enter mark 3: "))
    mark4 = int(input("Enter mark 4: "))
    mark5 = int(input("Enter mark 5: "))

    total = mark1 + mark2 + mark3 + mark4 + mark5
    average = total / 5

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    if average >= 50:
        status = "PASS"
    else:
        status = "FAIL"

    print("\n================================")
    print("        STUDENT REPORT")
    print("================================")
    print("Name       :", name)
    print("Age        :", age)
    print("Department :", department)

    print("--------------------------------")
    print("Mark 1     :", mark1)
    print("Mark 2     :", mark2)
    print("Mark 3     :", mark3)
    print("Mark 4     :", mark4)
    print("Mark 5     :", mark5)

    print("--------------------------------")
    print("Total      :", total)
    print("Average    :", average)
    print("Grade      :", grade)
    print("Status     :", status)
    print("================================")


add_student()