import pandas as pd

prices = {"Laptop": 60000, "Phone": 30000, "Tablet": 25000, "Monitor": 15000, "Keyboard": 2000}
s = pd.Series(prices)

print("Products and prices:")
print(s)

s = s * 1.10
print("\nPrices after 10% increase:")
print(s)

print("\nMost expensive product:")
print(s.idxmax(), s.max())

print("\nProducts costing more than 1000:")
print(s[s > 1000])
