import json

students = []


def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []


def get_age():
    while True:
        try:
            age = int(input("Enter student age: "))

            if 1 <= age <= 100:
                return age
            else:
                print("Please enter a valid age.")

        except ValueError:
            print("Please enter a valid number.")


def get_mark(subject):
    while True:
        try:
            mark = int(input("Enter " + subject + ": "))

            if 0 <= mark <= 100:
                return mark
            else:
                print("Mark must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


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
    age = get_age()
    department = input("Enter department: ")

    mark1 = get_mark("mark 1")
    mark2 = get_mark("mark 2")
    mark3 = get_mark("mark 3")
    mark4 = get_mark("mark 4")
    mark5 = get_mark("mark 5")

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

    if len(students) == 0:
        print("No students available.")
        return

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

            return

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
                student["age"] = get_age()

            elif choice == "3":
                student["department"] = input("Enter new department: ")

            elif choice == "4":
                student["mark1"] = get_mark("new mark 1")
                student["mark2"] = get_mark("new mark 2")
                student["mark3"] = get_mark("new mark 3")
                student["mark4"] = get_mark("new mark 4")
                student["mark5"] = get_mark("new mark 5")

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


def delete_student():
    search_name = input("\nEnter student name to delete: ")

    for student in students:
        if student["name"].lower() == search_name.lower():

            students.remove(student)

            print("\nStudent deleted successfully!")
            return

    print("\nStudent not found.")


load_students()


while True:
    print("\n================================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        student = add_student()
        students.append(student)
        save_students()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()
        save_students()

    elif choice == "5":
        delete_student()
        save_students()

    elif choice == "6":
        print("\nThank you for using Student Management System!")
        break

    else:
        print("\nInvalid choice. Please try again.")