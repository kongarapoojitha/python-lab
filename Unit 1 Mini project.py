print("----- BILL GENERATOR -----")

name = input("Enter customer name: ")
product = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

total = quantity * price
tax = total * 0.05
final_bill = total + tax

print("\n----- BILL -----")
print("Customer Name:", name)
print("Product:", product)
print("Quantity:", quantity)
print("Price per Item:", price)
print("Total Amount:", total)
print("Tax (5%):", tax)
print("Final Bill:", final_bill)
