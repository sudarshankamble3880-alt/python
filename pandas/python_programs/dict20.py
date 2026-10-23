# 20. Create a dictionary and display its elements in ascending order of keys.

d = {
    4: "D",
    2: "B",
    5: "E",
    1: "A",
    3: "C"
}

for key in sorted(d):
    print(key, ":", d[key])
