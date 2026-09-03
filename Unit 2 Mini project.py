import random

print("----- OTP GENERATOR -----")

name = input("Enter your name: ")

otp = random.randint(100000, 999999)

print("\nHello,", name)
print("Your generated OTP is:", otp)

entered_otp = int(input("Enter the OTP to verify: "))

if entered_otp == otp:
    print("OTP Verified Successfully!")
else:
    print("Incorrect OTP. Verification Failed.")
