import student_functions as sf

sf.load_students()

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

    print("\n15. Exit")
    print("========================================")

    choice = input("Enter your choice: ")

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

    elif choice == "12":
        sf.attendance_analytics()

    elif choice == "13":
        sf.low_attendance_students()

    elif choice == "14":
        sf.sort_by_attendance()

    elif choice == "15":
      confirm = input(
        "\nAre you sure you want to exit? (yes/no): "
      )

      if confirm.lower() == "yes":
        print("\nThank you for using Student Management System!")
        break
      else:
        print("\nReturning to main menu...")