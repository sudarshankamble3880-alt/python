import pandas as pd

sales = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Accessories"],
    "Price": [60000, 30000, 25000, 15000, 2000],
    "Quantity": [2, 5, 3, 4, 10]
}

df = pd.DataFrame(sales)
df["Total_Sales"] = df["Price"] * df["Quantity"]

print(df)
print("\nSales greater than 10000:")
print(df[df["Total_Sales"] > 10000])
print("\nProduct with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])
print("\nAverage sales:", df["Total_Sales"].mean())
