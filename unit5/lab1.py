
# Bank Account System Using OOP

class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Enter a valid amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount!")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")

    def display(self):
        print("\n===== ACCOUNT DETAILS =====")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Available Balance: Rs.", self.balance)


name = input("Enter account holder name: ")
account_number = input("Enter account number: ")

account = BankAccount(name, account_number)

while True:
    print("\n===== BANK ACCOUNT SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "3":
        account.display()

    elif choice == "4":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Try again.")
