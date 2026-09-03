print("DAILY STUDY TIME TRACKER")

name = input("Enter student name: ")
hours = float(input("Enter number of study hours: "))

print("\n----- STUDY DETAILS -----")
print("Student Name:", name)
print("Study Hours:", hours)

if hours >= 5:
    print("Great! You studied for a good amount of time.")
else:
    print("Keep going! Try to study a little more tomorrow.")
