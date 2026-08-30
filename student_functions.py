import json
import csv


students = []


def admin_login():
    max_attempts = 3

    print("\n========================================")
    print("          ADMIN LOGIN")
    print("========================================")

    for attempt in range(max_attempts):
        username = input("\nUsername: ").strip()
        password = input("Password: ").strip()

        if username == "admin" and password == "admin123":
            print("\nLogin successful!")
            print("Welcome, Administrator.")
            return True

        remaining = max_attempts - attempt - 1

        if remaining > 0:
            print("\nInvalid username or password.")
            print("Attempts remaining:", remaining)
        else:
            print("\nToo many failed login attempts.")

    return False


def save_students():
    try:
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

    except OSError as error:
        print("\nError: Unable to save student data.")
        print("Details:", error)

def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            data = json.load(file)

            if isinstance(data, list):
                students = data
            else:
                print("\nWarning: Invalid student data format.")
                students = []

    except FileNotFoundError:
        students = []

    except json.JSONDecodeError:
        print("\nWarning: students.json is corrupted or empty.")
        students = []

    except OSError as error:
        print("\nError: Unable to load student data.")
        print("Details:", error)
        students = []

def backup_students():
    try:
        with open("students_backup.json", "w") as file:
            json.dump(students, file, indent=4)

        print("\nStudent data backup created successfully.")
        print("Backup file: students_backup.json")

    except OSError as error:
        print("\nError: Unable to create student data backup.")
        print("Details:", error)

def restore_students():
    global students

    try:
        with open("students_backup.json", "r") as file:
            data = json.load(file)

            if isinstance(data, list):
                students = data
                save_students()

                print("\nStudent data restored successfully.")
                print("Restored data saved to students.json.")
            else:
                print("\nError: Invalid backup data format.")

    except FileNotFoundError:
        print("\nError: Backup file not found.")

    except json.JSONDecodeError:
        print("\nError: Backup file is corrupted or empty.")

    except OSError as error:
        print("\nError: Unable to restore student data.")
        print("Details:", error)

        
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

def get_total_classes():
    while True:
        try:
            total_classes = int(input("Enter total classes: "))

            if total_classes > 0:
                return total_classes
            else:
                print("Total classes must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


def get_attended_classes(total_classes):
    while True:
        try:
            attended_classes = int(input("Enter classes attended: "))

            if 0 <= attended_classes <= total_classes:
                return attended_classes
            else:
                print(
                    "Classes attended must be between 0 and",
                    total_classes
                )

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

    total_classes = get_total_classes()
    attended_classes = get_attended_classes(total_classes)

    attendance_percentage = round(
    (attended_classes / total_classes) * 100, 2
    )

    if attendance_percentage >= 75:
       attendance_status = "GOOD"
    else:
       attendance_status = "LOW"

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
        "status": status,
        "total_classes": total_classes,
        "attended_classes": attended_classes,
        "attendance_percentage": attendance_percentage,
        "attendance_status": attendance_status
    }

def display_student_report(student):
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

    attendance = student.get("attendance_percentage", "N/A")
    if isinstance(attendance, (int, float)):
        attendance = f"{attendance:.2f}%"

    print("----------------------------------------")
    print("Total Classes    :", student.get("total_classes", "N/A"))
    print("Classes Attended :", student.get("attended_classes", "N/A"))
    print("Attendance       :", attendance)
    print("Attendance Status:", student.get("attendance_status", "N/A"))

    print("========================================")

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

        attendance = student.get("attendance_percentage", "N/A")

        if isinstance(attendance, (int, float)):
            attendance = f"{attendance:.2f}%"

        print("--------------------------------")
        print("Total Classes    :", student.get("total_classes", "N/A"))
        print("Classes Attended :", student.get("attended_classes", "N/A"))
        print("Attendance       :", attendance)
        print("Attendance Status:", student.get("attendance_status", "N/A"))

        print("================================")

def search_student():
    search_value = input(
        "\nEnter student ID or name to search: "
    ).strip()

    if not search_value:
        print("\nSearch value cannot be empty.")
        return

    found_students = []

    for student in students:
        student_id = str(student.get("id", "")).upper()
        student_name = str(student.get("name", "")).lower()

        if (
            search_value.upper() == student_id
            or search_value.lower() in student_name
        ):
            found_students.append(student)

    if not found_students:
        print("\nStudent not found.")
        return

    print(f"\n{len(found_students)} student(s) found.")

    for student in found_students:
        display_student_report(student)

    print("\nSearch completed successfully.")


def update_student():
    search_id = input("\nEnter student ID to update: ").strip().upper()

    for student in students:
        if student.get("id", "").upper() == search_id:

            print("\n================================")
            print("       CURRENT STUDENT DETAILS")
            print("================================")
            print("ID         :", student.get("id", "N/A"))
            print("Name       :", student.get("name", "N/A"))
            print("Age        :", student.get("age", "N/A"))
            print("Department :", student.get("department", "N/A"))
            print("Mark 1     :", student.get("mark1", "N/A"))
            print("Mark 2     :", student.get("mark2", "N/A"))
            print("Mark 3     :", student.get("mark3", "N/A"))
            print("Mark 4     :", student.get("mark4", "N/A"))
            print("Mark 5     :", student.get("mark5", "N/A"))
            print("Attendance :", student.get("attendance_percentage", "N/A"), "%")

            print("\nWhat do you want to update?")
            print("1. Update name")
            print("2. Update age")
            print("3. Update department")
            print("4. Update marks")
            print("5. Update attendance")

            choice = input("Enter your choice: ").strip()

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

            elif choice == "5":
                total_classes = get_total_classes()
                attended_classes = get_attended_classes(total_classes)

                attendance_percentage = round(
                    (attended_classes / total_classes) * 100, 2
                )

                if attendance_percentage >= 75:
                    attendance_status = "GOOD"
                else:
                    attendance_status = "LOW"

                student["total_classes"] = total_classes
                student["attended_classes"] = attended_classes
                student["attendance_percentage"] = attendance_percentage
                student["attendance_status"] = attendance_status

            else:
                print("\nInvalid choice.")
                return

            save_students()

            print("\nStudent updated successfully!")

            print("\n================================")
            print("        UPDATED DETAILS")
            print("================================")
            display_student_report(student)

            return

    print("\nStudent not found.")

def delete_student():
    search_id = input("\nEnter student ID to delete: ").strip().upper()

    for student in students:
        if student.get("id", "").upper() == search_id:

            print("\n================================")
            print("       STUDENT TO BE DELETED")
            print("================================")
            print("ID         :", student.get("id", "N/A"))
            print("Name       :", student.get("name", "N/A"))
            print("Age        :", student.get("age", "N/A"))
            print("Department :", student.get("department", "N/A"))
            print("Average    :", student.get("average", "N/A"))
            print("Grade      :", student.get("grade", "N/A"))
            print("Status     :", student.get("status", "N/A"))
            print(
                "Attendance :",
                student.get("attendance_percentage", "N/A"),
                "%"
            )

            confirm = input(
                "\nAre you sure you want to delete this student? (yes/no): "
            )

            if confirm.strip().lower() == "yes":
                students.remove(student)
                save_students()

                print("\nStudent deleted successfully!")
                print("Remaining students:", len(students))
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

def attendance_analytics():
    print("\n========================================")
    print("        ATTENDANCE ANALYTICS")
    print("========================================")

    if len(students) == 0:
        print("No students available.")
        return

    attendance_students = []

    for student in students:
        attendance = student.get("attendance_percentage")

        if isinstance(attendance, (int, float)):
            attendance_students.append(student)

    if len(attendance_students) == 0:
        print("No attendance data available.")
        return

    total_students = len(attendance_students)
    total_attendance = 0
    good_attendance = 0
    low_attendance = 0

    highest_student = attendance_students[0]
    lowest_student = attendance_students[0]

    for student in attendance_students:
        attendance = student.get("attendance_percentage", 0)

        total_attendance += attendance

        if attendance >= 75:
            good_attendance += 1
        else:
            low_attendance += 1

        if attendance > highest_student.get("attendance_percentage", 0):
            highest_student = student

        if attendance < lowest_student.get("attendance_percentage", 0):
            lowest_student = student

    average_attendance = round(
        total_attendance / total_students, 2
    )

    good_percentage = round(
        (good_attendance / total_students) * 100, 2
    )

    low_percentage = round(
        (low_attendance / total_students) * 100, 2
    )

    print("Total Students       :", total_students)
    print("Average Attendance   :", f"{average_attendance:.2f}%")
    print("Good Attendance      :", good_attendance)
    print("Low Attendance       :", low_attendance)
    print("Good Attendance %    :", f"{good_percentage:.2f}%")
    print("Low Attendance %     :", f"{low_percentage:.2f}%")

    print("----------------------------------------")
    print("HIGHEST ATTENDANCE")
    print("Name                 :", highest_student.get("name", "N/A"))
    print("ID                   :", highest_student.get("id", "N/A"))
    print(
        "Attendance           :",
        f"{highest_student.get('attendance_percentage', 0):.2f}%"
    )

    print("----------------------------------------")
    print("LOWEST ATTENDANCE")
    print("Name                 :", lowest_student.get("name", "N/A"))
    print("ID                   :", lowest_student.get("id", "N/A"))
    print(
        "Attendance           :",
        f"{lowest_student.get('attendance_percentage', 0):.2f}%"
    )

    print("========================================")

def low_attendance_students():
    print("\n========================================")
    print("       LOW ATTENDANCE STUDENTS")
    print("========================================")

    if len(students) == 0:
        print("No students available.")
        return

    low_students = []

    for student in students:
        attendance = student.get("attendance_percentage")

        if isinstance(attendance, (int, float)) and attendance < 75:
            low_students.append(student)

    if len(low_students) == 0:
        print("No students have low attendance.")
        return

    print("\nStudents below 75% attendance:")
    print("----------------------------------------")

    for student in low_students:
        print("ID         :", student.get("id", "N/A"))
        print("Name       :", student.get("name", "N/A"))
        print("Department :", student.get("department", "N/A"))
        print(
            "Attendance :",
            f"{student.get('attendance_percentage', 0):.2f}%"
        )
        print("Status     :", student.get("attendance_status", "LOW"))
        print("----------------------------------------")

    print("Total Low Attendance Students:", len(low_students))
    print("========================================")

def sort_by_attendance():
    print("\n========================================")
    print("       SORT BY ATTENDANCE")
    print("========================================")

    if len(students) == 0:
        print("No students available.")
        return

    print("1. Highest to Lowest")
    print("2. Lowest to Highest")
    print("----------------------------------------")

    choice = input("Enter your choice: ")

    attendance_students = [
        student for student in students
        if isinstance(
            student.get("attendance_percentage"),
            (int, float)
        )
    ]

    if len(attendance_students) == 0:
        print("No attendance data available.")
        return

    if choice == "1":
        sorted_students = sorted(
            attendance_students,
            key=lambda student: student.get(
                "attendance_percentage", 0
            ),
            reverse=True
        )

    elif choice == "2":
        sorted_students = sorted(
            attendance_students,
            key=lambda student: student.get(
                "attendance_percentage", 0
            )
        )

    else:
        print("Invalid choice.")
        return

    print("\n========================================")
    print("       ATTENDANCE SORTING")
    print("========================================")

    for student in sorted_students:
        print(
            student.get("id", "N/A"),
            "-",
            student.get("name", "N/A"),
            "-",
            f"{student.get('attendance_percentage', 0):.2f}%"
        )

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
            if department.lower() in student.get("department", "").lower()
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
            "status",
            "total_classes",
            "attended_classes",
            "attendance_percentage",
            "attendance_status"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
            extrasaction="ignore"
        )

        writer.writeheader()

        for student in students:
            writer.writerow(student)

    print("\nStudents exported successfully to students.csv")

def performance_report():
    if len(students) == 0:
        print("\nNo students available.")
        return

    student_id = input("\nEnter student ID: ").strip().upper()

    for student in students:
        if student.get("id", "").upper() == student_id:
            display_student_report(student)
            return

    print("\nStudent not found.")

def student_ranking():
    print("\n========================================")
    print("           STUDENT RANKING")
    print("========================================")

    if len(students) == 0:
        print("\nNo students available.")
        return

    ranked_students = []

    for student in students:
        average = student.get("average")

        if isinstance(average, (int, float)):
            ranked_students.append(student)

    if len(ranked_students) == 0:
        print("\nNo students with marks available for ranking.")
        return

    ranked_students.sort(
        key=lambda student: student.get("average", 0),
        reverse=True
    )

    print("\nRank  ID         Name                 Average")
    print("-----------------------------------------------")

    rank = 1
    previous_average = None

    for index, student in enumerate(ranked_students):
        average = student.get("average", 0)

        if previous_average is not None and average < previous_average:
            rank = index + 1

        print(
            f"{rank:<6}"
            f"{student.get('id', 'N/A'):<11}"
            f"{student.get('name', 'N/A'):<21}"
            f"{average:.2f}"
        )

        previous_average = average

    print("===============================================")
