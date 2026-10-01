import pandas as pd

products = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Accessories"],
    "Price": [60000, 30000, 25000, 15000, 2000],
    "Quantity": [2, 5, 3, 4, 10]
}

df = pd.DataFrame(products)
df["Total_Amount"] = df["Price"] * df["Quantity"]
print(df)
print("\nProduct with highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])
