# 17. Given two dictionaries, find the keys that are common to both dictionaries.

d1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

d2 = {
    "b": 40,
    "c": 50,
    "d": 60
}

common = d1.keys() & d2.keys()

print("Common keys:", common)
