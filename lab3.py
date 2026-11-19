
# CSV-Based Payroll Management System

import csv
import os

filename = "payroll.csv"

# Create CSV file with headings if it does not exist
if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Employee ID",
            "Name",
            "Basic Salary",
            "HRA",
            "DA",
            "Gross Salary",
            "Deduction",
            "Net Salary"
        ])

while True:
    print("\n===== PAYROLL MANAGEMENT SYSTEM =====")
    print("1. Add Employee Salary")
    print("2. Display Payroll")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        basic = float(input("Enter Basic Salary: "))

        if basic < 0:
            print("Salary cannot be negative!")
            continue

        hra = basic * 0.20
        da = basic * 0.10
        gross = basic + hra + da
        deduction = basic * 0.05
        net = gross - deduction

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                emp_id, name, basic, hra, da,
                gross, deduction, net
            ])

        print("\nEmployee payroll added successfully!")
        print("Gross Salary: Rs.", round(gross, 2))
        print("Deduction: Rs.", round(deduction, 2))
        print("Net Salary: Rs.", round(net, 2))

    elif choice == "2":
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)

            print("\n========== PAYROLL RECORDS ==========")

            for row in reader:
                print(" | ".join(row))

            print("=====================================")

    elif choice == "3":
        print("Thank you for using Payroll System!")
        break

    else:
        print("Invalid choice! Please try again.")

