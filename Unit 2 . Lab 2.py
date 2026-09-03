num = int(input("Enter a positive number: "))

# Checking Prime Number
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a Prime Number")
            break
    else:
        print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")

# Calculating Factorial
factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial = factorial * i

    print("Factorial of", num, "is", factorial)
