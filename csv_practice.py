# Exercise 2

# import csv

# with open("data/sales.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#        print(row)

# Exercise 3
# import csv
# with open("data/sales.csv", "r") as file:
#     reader = csv.reader(file)
    
#     header = next(reader)
#     print("Header:", header)

#     for row in reader:
#         print(row)

# Exercise 4
# import csv
# with open("data/sales.csv", "r") as file:
#     reader = csv.reader(file)
    
#     header = next(reader)
#     print("Header:", header)

#     total_sales = 0

#     for row in reader:
#         product = row[0]
#         price = float(row[1])
#         quantity = int(row[2])
#         total = price * quantity
#         total_sales += total
#         print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

# print(f"Total sales: ${total_sales:.2f}")

# Exercise 5
# import csv

# original_count = 0
# cleaned_count = 0

# with open("data/sales.csv", "r") as infile:
#     reader = csv.reader(infile)
#     header = next(reader)
#     with open("data/cleaned_sales", "w", newline='') as outfile:
#         writer = csv.writer(outfile)
#         writer.writerow(["Product", "Price", "Quantity", "Total"])
         
#         for row in reader:
#             original_count += 1
#             product = row[0]
#             price = float(row[1])
#             quantity = int(row[2])

#             total = price * quantity
#             if total > 100:
#                 writer.writerow([product, price, quantity, total])
#                 cleaned_count += 1
# print(f"Original rows: {original_count}")
# print(f"Cleaned rows: {cleaned_count}")

# Exercise 6
# import csv

# total_sales = 0
# original_count = 0

# with open("data/sales.csv", "r") as infile:
#     reader = csv.DictReader(infile)
         
#     for row in reader:
#         product = row["product"]
#         price = float(row["price"])
#         quantity = int(row["quantity"])

#         total = price * quantity
#         total_sales += total
#         original_count += 1

#         print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")
# print(f"Total Sales: ${total_sales:.2f}")
# print(f"Original rows: {original_count}")

# when using csv.reader, you can access the information based on its position in the row. When it is DictReader, you access the info based on its column name.
# Exercise 7
# import csv
# product_sales = {}

# with open("data/sales.csv", "r") as infile:
#     reader = csv.DictReader(infile)
#     for row in reader:
#         product = row["product"]
#         price = float(row["price"])
#         quantity = int(row["quantity"])

#         total = price * quantity

#         if product in product_sales:
#             product_sales[product] += total
#         else:
#             product_sales[product] = total

# for product in sorted(product_sales):
#     print(f"{product}: ${product_sales[product]:.2f}")
#     print(f"Total Sales: ${sum(product_sales.values()):.2f}")

# Exercise 8
import csv
from datetime import datetime
product_sales = {}
total_sales = 0
with open("data/sales.csv", "r") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        total_sales += total

        if product in product_sales:
            product_sales[product] += total
        else:
            product_sales[product] = total
for product in sorted(product_sales):
    print(f"{product}: ${product_sales[product]:.2f}")
print(f"Total Sales: ${total_sales:.2f}")
with open("data/run_log.txt", "a") as logfile:
    timestamp = datetime.now()
    logfile.write(f"{timestamp} - Total Sales: ${total_sales:.2f}\n")