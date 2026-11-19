
# MINI PROJECT: STUDENT ATTENDANCE TRACKER

attendance = {}

while True:
    print("\n================================")
    print("     STUDENT ATTENDANCE TRACKER")
    print("================================")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Attendance Percentage")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        if name in attendance:
            print("Student already exists!")
        else:
            attendance[name] = {
                "Present": 0,
                "Absent": 0
            }
            print("Student added successfully!")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in attendance:
            status = input("Enter P for Present or A for Absent: ")
            status = status.upper()

            if status == "P":
                attendance[name]["Present"] += 1
                print("Attendance marked as Present!")
            elif status == "A":
                attendance[name]["Absent"] += 1
                print("Attendance marked as Absent!")
            else:
                print("Invalid attendance status!")

        else:
            print("Student not found!")

    elif choice == "3":
        if not attendance:
            print("No student records available.")
        else:
            print("\n===== ATTENDANCE REPORT =====")

            for name, record in attendance.items():
                print("\nStudent:", name)
                print("Present:", record["Present"])
                print("Absent:", record["Absent"])

    elif choice == "4":
        name = input("Enter student name: ")

        if name in attendance:
            present = attendance[name]["Present"]
            absent = attendance[name]["Absent"]
            total = present + absent

            if total > 0:
                percentage = (present / total) * 100
                print("Student:", name)
                print("Attendance Percentage:", round(percentage, 2), "%")
            else:
                print("No attendance marked yet.")

        else:
            print("Student not found!")

    elif choice == "5":
        print("Thank you for using Attendance Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")
