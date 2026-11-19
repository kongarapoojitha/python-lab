
# Student Data Manager Using Files

while True:
    print("\n===== STUDENT DATA MANAGER =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        with open("students.txt", "a") as file:
            file.write(roll + "," + name + "," + marks + "\n")

        print("Student record added successfully!")

    elif choice == "2":
        try:
            with open("students.txt", "r") as file:
                print("\n===== STUDENT RECORDS =====")

                records = file.readlines()

                if not records:
                    print("No student records found.")
                else:
                    for record in records:
                        data = record.strip().split(",")

                        if len(data) == 3:
                            print("Roll Number:", data[0])
                            print("Name:", data[1])
                            print("Marks:", data[2])
                            print("----------------------")

        except FileNotFoundError:
            print("Student file not found!")

    elif choice == "3":
        print("Thank you! Program ended.")
        break

    else:
        print("Invalid choice! Try again.")

