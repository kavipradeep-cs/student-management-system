import sys
import student_functions as sf


# ================= ADMIN LOGIN =================

if not sf.admin_login():
    print("\n========================================")
    print("          ACCESS DENIED")
    print("========================================")
    sys.exit()


# ================= LOAD STUDENTS =================

sf.load_students()


# ================= MAIN MENU =================

while True:

    print("\n========================================")
    print("       STUDENT MANAGEMENT SYSTEM")
    print("========================================")

    print("Total Students:", len(sf.students))

    print("\n--------------- MANAGEMENT -------------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")

    print("\n--------------- ANALYTICS ---------------")
    print("6. Student Statistics")
    print("7. Sort Students")
    print("8. Filter Students")
    print("9. Export Students to CSV")
    print("10. Student Performance Report")
    print("11. Student Ranking")

    print("\n--------------- ATTENDANCE --------------")
    print("12. Attendance Analytics")
    print("13. Low Attendance Students")
    print("14. Sort by Attendance")

    print("\n--------------- BACKUP ------------------")
    print("15. Backup Student Data")
    print("16. Restore Student Data")

    print("\n17. Exit")
    print("========================================")

    choice = input("Enter your choice: ").strip()

    # ================= MANAGEMENT =================

    if choice == "1":
        student = sf.add_student()
        sf.students.append(student)
        sf.save_students()

    elif choice == "2":
        sf.view_students()

    elif choice == "3":
        sf.search_student()

    elif choice == "4":
        sf.update_student()
        sf.save_students()

    elif choice == "5":
        sf.delete_student()
        sf.save_students()

    # ================= ANALYTICS =================

    elif choice == "6":
        sf.student_statistics()

    elif choice == "7":
        sf.sort_students()

    elif choice == "8":
        sf.filter_students()

    elif choice == "9":
        sf.export_to_csv()

    elif choice == "10":
        sf.performance_report()

    elif choice == "11":
        sf.student_ranking()

    # ================= ATTENDANCE =================

    elif choice == "12":
        sf.attendance_analytics()

    elif choice == "13":
        sf.low_attendance_students()

    elif choice == "14":
        sf.sort_by_attendance()

    # ================= BACKUP =================

    elif choice == "15":
        sf.backup_students()

    elif choice == "16":
        sf.restore_students()

    # ================= EXIT =================

    elif choice == "17":

        confirm = input(
            "\nAre you sure you want to exit? (yes/no): "
        ).strip().lower()

        if confirm == "yes":
            print("\n========================================")
            print(" Thank you for using Student Management System!")
            print("========================================")
            break

        else:
            print("\nReturning to main menu...")

    # ================= INVALID CHOICE =================

    else:
        print("\nInvalid choice.")
        print("Please enter a number from 1 to 17.")