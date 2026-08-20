import student_functions as sf

sf.load_students()

while True:
    print("\n========================================")
    print("       STUDENT MANAGEMENT SYSTEM")
    print("========================================")
    print("Total Students:", len(sf.students))
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
    print("10. Student Performance Report")
    print("11. Exit")
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
        confirm = input("\nAre you sure you want to exit? (yes/no): ")

        if confirm.lower() == "yes":
            print("\nThank you for using Student Management System!")
            break
        else:
            print("\nReturning to main menu...")

    else:
        print("\nInvalid choice. Please enter a number from 1 to 11.")