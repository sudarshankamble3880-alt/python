import pandas as pd

orders = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["A", "B", "C", "D", "E"],
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "Quantity": [1, 2, 3, 2, 5],
    "Price": [60000, 30000, 25000, 15000, 2000],
    "Discount": [5000, 2000, 1000, 500, 200]
}

df = pd.DataFrame(orders)
df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All orders:")
print(df)
print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])
print("\nHighest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])
print("\nAverage order value:", df["Final_Amount"].mean())
