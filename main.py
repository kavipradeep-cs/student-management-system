import json
import csv


students = []

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

            if not isinstance(students, list):
                print("\nInvalid student data found.")
                students = []

    except FileNotFoundError:
        students = []

    except json.JSONDecodeError:
        print("\nWarning: students.json is corrupted or empty.")
        print("Starting with an empty student list.")
        students = []

def get_student_id():
    while True:
        student_id = input("Enter student ID: ").strip().upper()

        if student_id == "":
            print("Student ID cannot be empty.")
            continue

        if " " in student_id:
            print("Student ID cannot contain spaces.")
            continue

        if not student_id.startswith("STU"):
            print("Student ID must start with STU.")
            continue

        if not student_id[3:].isdigit():
            print("Student ID must be like STU001.")
            continue

        for student in students:
            if student.get("id") == student_id:
                print("Student ID already exists. Please enter a different ID.")
                break
        else:
            return student_id

def get_name():
    while True:
        name = input("Enter student name: ").strip()

        if name == "":
            print("Name cannot be empty.")
            continue

        if not all(char.isalpha() or char.isspace() for char in name):
            print("Name can contain only letters and spaces.")
            continue

        return name

def get_department():
    while True:
        department = input("Enter department: ").strip()

        if department == "":
            print("Department cannot be empty.")
            continue

        if not all(char.isalpha() or char.isspace() for char in department):
            print("Department can contain only letters and spaces.")
            continue

        return department.upper()

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

    student_id = get_student_id()
    name = get_name()
    age = get_age()
    department = get_department()

    mark1 = get_mark("mark 1")
    mark2 = get_mark("mark 2")
    mark3 = get_mark("mark 3")
    mark4 = get_mark("mark 4")
    mark5 = get_mark("mark 5")

    total = mark1 + mark2 + mark3 + mark4 + mark5
    average = round(total / 5, 2)

    grade = calculate_grade(average)
    status = calculate_status(average)

    print("\n================================")
    print("        STUDENT REPORT")
    print("================================")

    print("ID         :", student_id)
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
        "id": student_id,
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
        print("ID         :", student.get("id", "N/A"))
        print("Name       :", student.get("name", "N/A"))
        print("Age        :", student.get("age", "N/A"))
        print("Department :", student.get("department", "N/A"))

        print("--------------------------------")
        print("Mark 1     :", student.get("mark1", "N/A"))
        print("Mark 2     :", student.get("mark2", "N/A"))
        print("Mark 3     :", student.get("mark3", "N/A"))
        print("Mark 4     :", student.get("mark4", "N/A"))
        print("Mark 5     :", student.get("mark5", "N/A"))

        print("--------------------------------")
        print("Total      :", student.get("total", "N/A"))

        average = student.get("average", "N/A")
        if isinstance(average, (int, float)):
            average = f"{average:.2f}"

        print("Average    :", average)
        print("Grade      :", student.get("grade", "N/A"))
        print("Status     :", student.get("status", "N/A"))

        print("================================")

def search_student():
    search_id = input("\nEnter student ID to search: ").strip().upper()

    for student in students:
        if student.get("id", "").upper() == search_id:
            print("\n========================================")
            print("           STUDENT REPORT")
            print("========================================")

            print("ID         :", student.get("id", "N/A"))
            print("Name       :", student.get("name", "N/A"))
            print("Age        :", student.get("age", "N/A"))
            print("Department :", student.get("department", "N/A"))

            print("----------------------------------------")
            print("Mark 1     :", student.get("mark1", "N/A"))
            print("Mark 2     :", student.get("mark2", "N/A"))
            print("Mark 3     :", student.get("mark3", "N/A"))
            print("Mark 4     :", student.get("mark4", "N/A"))
            print("Mark 5     :", student.get("mark5", "N/A"))

            print("----------------------------------------")
            print("Total      :", student.get("total", "N/A"))

            average = student.get("average", "N/A")
            if isinstance(average, (int, float)):
                average = f"{average:.2f}"

            print("Average    :", average)
            print("Grade      :", student.get("grade", "N/A"))
            print("Status     :", student.get("status", "N/A"))

            print("========================================")

            return

    print("\nStudent not found.")

def update_student():
    search_id = input("\nEnter student ID to update: ").strip().upper()

    for student in students:
        if student.get("id", "").upper() == search_id:
            print("\nStudent found!")
            print("1. Update name")
            print("2. Update age")
            print("3. Update department")
            print("4. Update marks")

            choice = input("Enter your choice: ")

            if choice == "1":
                student["name"] = get_name()

            elif choice == "2":
                student["age"] = get_age()

            elif choice == "3":
                student["department"] = get_department()

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

                student["average"] = round(student["total"] / 5, 2)
                student["grade"] = calculate_grade(student["average"])
                student["status"] = calculate_status(student["average"])

            else:
                print("Invalid choice.")
                return

            print("\nStudent updated successfully!")
            return

    print("\nStudent not found.")

def delete_student():
    search_id = input("\nEnter student ID to delete: ").strip().upper()

    for student in students:
        if student.get("id", "").upper() == search_id:
            print("\nStudent found:")
            print("ID   :", student.get("id"))
            print("Name :", student.get("name"))

            confirm = input(
                "Are you sure you want to delete this student? (yes/no): "
            )

            if confirm.lower() == "yes":
                students.remove(student)
                print("\nStudent deleted successfully!")
            else:
                print("\nDeletion cancelled.")

            return

    print("\nStudent not found.")
def student_statistics():
    print("\n========================================")
    print("       CLASS PERFORMANCE REPORT")
    print("========================================")

    if len(students) == 0:
        print("No students available.")
        return

    total_students = len(students)
    passed = 0
    failed = 0
    total_average = 0

    highest_student = students[0]
    lowest_student = students[0]

    department_count = {}

    for student in students:
        average = student.get("average", 0)
        total_average += average

        if student.get("status", "").upper() == "PASS":
            passed += 1
        else:
            failed += 1

        if average > highest_student.get("average", 0):
            highest_student = student

        if average < lowest_student.get("average", 0):
            lowest_student = student

        department = student.get("department", "UNKNOWN")
        department_count[department] = department_count.get(department, 0) + 1

    class_average = round(total_average / total_students, 2)

    pass_percentage = round((passed / total_students) * 100, 2)
    fail_percentage = round((failed / total_students) * 100, 2)

    print("Total Students :", total_students)
    print("Passed         :", passed)
    print("Failed         :", failed)
    print("Pass Percentage:", f"{pass_percentage:.2f}%")
    print("Fail Percentage:", f"{fail_percentage:.2f}%")
    print("Class Average  :", f"{class_average:.2f}")

    print("----------------------------------------")
    print("HIGHEST PERFORMER")
    print("Name           :", highest_student.get("name", "N/A"))
    print("ID             :", highest_student.get("id", "N/A"))
    print("Average        :", f"{highest_student.get('average', 0):.2f}")

    print("----------------------------------------")
    print("LOWEST PERFORMER")
    print("Name           :", lowest_student.get("name", "N/A"))
    print("ID             :", lowest_student.get("id", "N/A"))
    print("Average        :", f"{lowest_student.get('average', 0):.2f}")

    print("----------------------------------------")
    print("DEPARTMENT-WISE STUDENT COUNT")

    for department, count in department_count.items():
        print(department, ":", count)

    print("----------------------------------------")
    print("Highest Average:", f"{highest_student.get('average', 0):.2f}")
    print("Lowest Average :", f"{lowest_student.get('average', 0):.2f}")

    print("========================================")

def sort_students():
    if len(students) == 0:
        print("\nNo students available.")
        return

    print("\n================================")
    print("        SORT STUDENTS")
    print("================================")
    print("1. Average - Highest to Lowest")
    print("2. Average - Lowest to Highest")
    print("3. Name - A to Z")
    print("4. Name - Z to A")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        sorted_students = sorted(
            students,
            key=lambda student: student.get("average", 0),
            reverse=True
        )

    elif choice == "2":
        sorted_students = sorted(
            students,
            key=lambda student: student.get("average", 0)
        )

    elif choice == "3":
        sorted_students = sorted(
            students,
            key=lambda student: student.get("name", "").lower()
        )

    elif choice == "4":
        sorted_students = sorted(
            students,
            key=lambda student: student.get("name", "").lower(),
            reverse=True
        )

    else:
        print("\nInvalid choice.")
        return

    print("\n================================")
    print("       SORTED STUDENTS")
    print("================================")

    for student in sorted_students:
        average = student.get("average", "N/A")

        if isinstance(average, (int, float)):
            average = f"{average:.2f}"

        print("ID         :", student.get("id", "N/A"))
        print("Name       :", student.get("name", "N/A"))
        print("Average    :", average)
        print("Grade      :", student.get("grade", "N/A"))
        print("Status     :", student.get("status", "N/A"))
        print("--------------------------------")


def filter_students():
    if len(students) == 0:
        print("\nNo students available.")
        return

    print("\n================================")
    print("       FILTER STUDENTS")
    print("================================")
    print("1. Show Passed Students")
    print("2. Show Failed Students")
    print("3. Filter by Department")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        filtered_students = [
            student for student in students
            if student.get("status", "").lower() == "pass"
        ]

        print("\n========== PASSED STUDENTS ==========")

    elif choice == "2":
        filtered_students = [
            student for student in students
            if student.get("status", "").lower() == "fail"
        ]

        print("\n========== FAILED STUDENTS ==========")

    elif choice == "3":
        department = input("Enter department: ").strip()

        filtered_students = [
            student for student in students
            if student.get("department", "").lower() == department.lower()
        ]

        print("\n========== FILTERED STUDENTS ==========")

    else:
        print("\nInvalid choice.")
        return

    if len(filtered_students) == 0:
        print("No matching students found.")
        return

    for student in filtered_students:
        print("--------------------------------")
        print("ID         :", student.get("id", "N/A"))
        print("Name       :", student.get("name", "N/A"))
        print("Department :", student.get("department", "N/A"))
        print("Average    :", student.get("average", "N/A"))
        print("Grade      :", student.get("grade", "N/A"))
        print("Status     :", student.get("status", "N/A"))

def export_to_csv():
    if len(students) == 0:
        print("\nNo students available to export.")
        return

    with open("students.csv", "w", newline="") as file:
        fieldnames = [
            "id",
            "name",
            "age",
            "department",
            "mark1",
            "mark2",
            "mark3",
            "mark4",
            "mark5",
            "total",
            "average",
            "grade",
            "status"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for student in students:
            writer.writerow(student)

    print("\nStudents exported successfully to students.csv")


load_students()

while True:
    print("\n========================================")
    print("       STUDENT MANAGEMENT SYSTEM")
    print("========================================")
    print("Total Students:", len(students))
    print("----------------------------------------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Statistics")
    print("7. Sort Students")
    print("8. Filter Students")
    print("9. Export Students to CSV")
    print("10. Exit")
    print("========================================")

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
        student_statistics()

    elif choice == "7":
        sort_students()

    elif choice == "8":
       filter_students()

    elif choice == "9":
       export_to_csv()

    elif choice == "10":
       confirm = input("\nAre you sure you want to exit? (yes/no): ")

       if confirm.lower() == "yes":
        print("\nThank you for using Student Management System!")
        break
       else:
        print("\nReturning to main menu...")

    else:
        print("\nInvalid choice. Please enter a number from 1 to 10.")