# 27. Create a dictionary containing product names and quantities.
# Perform add, update, delete, search and display products with quantity below 10.

products = {
    "Pen": 20,
    "Book": 5,
    "Bag": 15,
    "Pencil": 8
}

products["Bottle"] = 12
products["Pen"] = 25

del products["Bag"]

name = "Book"

if name in products:
    print("Product found:", products[name])

print("Products:", products)

print("Products below 10:")

for name, quantity in products.items():
    if quantity < 10:
        print(name, quantity)
