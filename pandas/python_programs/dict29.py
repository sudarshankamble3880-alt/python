# 29. Create a dictionary containing book IDs and book names.
# Implement add, search, remove, display and count total books.

books = {
    101: "Python",
    102: "Java",
    103: "Data Structures"
}

books[104] = "DBMS"

id = 102

if id in books:
    print("Book found:", books[id])

del books[103]

print("All books:")

for id, name in books.items():
    print(id, ":", name)

print("Total books:", len(books))
