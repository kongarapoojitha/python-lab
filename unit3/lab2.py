
# Student Grading System

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        continue

    students[name] = marks

print("\n===== STUDENT GRADING SYSTEM =====")

for name, marks in students.items():

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    print("\nStudent Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)

print("\nTotal Students:", len(students))
