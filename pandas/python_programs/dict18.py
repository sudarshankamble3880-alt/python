# 18. Given two dictionaries, identify the values that are common to both dictionaries.

d1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

d2 = {
    "x": 20,
    "y": 40,
    "z": 30
}

common = set(d1.values()) & set(d2.values())

print("Common values:", common)
