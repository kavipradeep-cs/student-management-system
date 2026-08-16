students = []


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def calculate_status(average):
    if average >= 50:
        return "PASS"
    else:
        return "FAIL"


def add_student():
    print("\n================================")
    print("       ADD STUDENT")
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

    grade = calculate_grade(average)
    status = calculate_status(average)

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

    return {
        "name": name,
        "age": age,
        "department": department,
        "mark1": mark1,
        "mark2": mark2,
        "mark3": mark3,
        "mark4": mark4,
        "mark5": mark5,
        "total": total,
        "average": average,
        "grade": grade,
        "status": status
    }


def view_students():
    print("\n================================")
    print("        ALL STUDENTS")
    print("================================")

    for student in students:
        print("Name       :", student["name"])
        print("Age        :", student["age"])
        print("Department :", student["department"])
        print("Average    :", student["average"])
        print("Grade      :", student["grade"])
        print("Status     :", student["status"])
        print("--------------------------------")


def search_student():
    search_name = input("\nEnter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\n================================")
            print("        STUDENT FOUND")
            print("================================")

            print("Name       :", student["name"])
            print("Age        :", student["age"])
            print("Department :", student["department"])
            print("Average    :", student["average"])
            print("Grade      :", student["grade"])
            print("Status     :", student["status"])

            found = True
            break

    if not found:
        print("\nStudent not found.")


def update_student():
    search_name = input("\nEnter student name to update: ")

    for student in students:
        if student["name"].lower() == search_name.lower():

            print("\nStudent found!")
            print("1. Update name")
            print("2. Update age")
            print("3. Update department")
            print("4. Update marks")

            choice = input("Enter your choice: ")

            if choice == "1":
                student["name"] = input("Enter new name: ")

            elif choice == "2":
                student["age"] = int(input("Enter new age: "))

            elif choice == "3":
                student["department"] = input("Enter new department: ")

            elif choice == "4":
                student["mark1"] = int(input("Enter new mark 1: "))
                student["mark2"] = int(input("Enter new mark 2: "))
                student["mark3"] = int(input("Enter new mark 3: "))
                student["mark4"] = int(input("Enter new mark 4: "))
                student["mark5"] = int(input("Enter new mark 5: "))

                student["total"] = (
                    student["mark1"]
                    + student["mark2"]
                    + student["mark3"]
                    + student["mark4"]
                    + student["mark5"]
                )

                student["average"] = student["total"] / 5

                student["grade"] = calculate_grade(student["average"])
                student["status"] = calculate_status(student["average"])

            else:
                print("Invalid choice.")
                return

            print("\nStudent updated successfully!")
            return

    print("\nStudent not found.")


while True:
    student = add_student()
    students.append(student)

    choice = input("\nDo you want to add another student? (yes/no): ")

    if choice.lower() != "yes":
        break


view_students()
search_student()
update_student()