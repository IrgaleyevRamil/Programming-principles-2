import os
from functools import reduce

base = os.path.dirname(__file__)
sales_path = os.path.join(base, "sales")

files = os.listdir(sales_path)

print("Files in directory:")
print(files)

products = []

for file in files:
    path = os.path.join(sales_path, file)

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            name, qty = line.split(",")
            products.append((name, int(qty)))

print("\nAll products:")
print(products)

total_records = len(products)

quantities = [qty for name, qty in products]

total_quantity = sum(quantities)

highest = max(quantities)
lowest = min(quantities)

average = total_quantity / total_records

increased = list(map(lambda x: (x[0], x[1] + 2), products))

filtered = list(filter(lambda x: x[1] > 5, products))

product_all = reduce(lambda x, y: x * y, quantities)

print("\nTotal records:", total_records)
print("Total quantity sold:", total_quantity)
print("Average quantity:", round(average, 2))
print("Highest:", highest)
print("Lowest:", lowest)

print("\nIncreased (+2):")
print(increased)

print("\nFiltered (>5):")
print(filtered)

print("\nProduct of all quantities:", product_all)

print("\nEnumerate:")
for i, (name, qty) in enumerate(products, start=1):
    print(i, name, qty)

names = [name for name, qty in products]
quantities = [qty for name, qty in products]

zipped = list(zip(names, quantities))
print("\nZipped:")
print(zipped)

sorted_products = sorted(products, key=lambda x: x[1])
print("\nSorted:")
print(sorted_products)

with open("sales_report.txt", "w") as f:
    f.write(f"Total records: {total_records}\n")
    f.write(f"Average quantity sold: {round(average, 2)}\n")
    f.write(f"Highest quantity sold: {highest}\n")
    f.write(f"Lowest quantity sold: {lowest}\n\n")

    f.write("Popular products:\n")
    for name, qty in filtered:
        f.write(f"{name} {qty}\n")