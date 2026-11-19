file = open("log.txt", "w")
file.write("Application started\n")
file.write("User logged in\n")
file.write("File opened successfully\n")
file.close()

file = open("log.txt", "r")

print("Log File Contents:")

for line in file:
    print(line.strip())

file.close()
