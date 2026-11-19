
# MINI PROJECT: RETAIL SALES DASHBOARD
# Using CSV and Matplotlib

import csv
import os
import matplotlib.pyplot as plt

filename = "sales.csv"

# Create sample CSV file if it does not exist
if not os.path.exists(filename):
    data = [
        ["Product", "Quantity", "Price"],
        ["Laptop", 5, 50000],
        ["Mobile", 10, 15000],
        ["Headphones", 15, 2000],
        ["Keyboard", 8, 1000],
        ["Mouse", 20, 500]
    ]

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Read sales data
products = []
revenues = []
total_sales = 0
total_quantity = 0

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["Product"]
        quantity = int(row["Quantity"])
        price = float(row["Price"])

        revenue = quantity * price

        products.append(product)
        revenues.append(revenue)

        total_sales += revenue
        total_quantity += quantity

# Display sales report
print("\n================================")
print("       RETAIL SALES DASHBOARD")
print("================================")

print("Total Revenue: Rs.", total_sales)
print("Total Products:", len(products))
print("Total Quantity Sold:", total_quantity)

print("\n===== PRODUCT SALES REPORT =====")

for i in range(len(products)):
    print(products[i], ": Rs.", revenues[i])

print("\n================================")
print("Generating Sales Dashboard...")
print("================================")

# Create graphical dashboard
plt.figure(figsize=(12, 5))

# Bar Chart
plt.subplot(1, 2, 1)
plt.bar(products, revenues)
plt.title("Product-wise Sales")
plt.xlabel("Products")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=30)

# Pie Chart
plt.subplot(1, 2, 2)
plt.pie(revenues, labels=products, autopct="%1.1f%%")
plt.title("Sales Distribution")

plt.tight_layout()
plt.show()

print("Sales dashboard displayed successfully!")

