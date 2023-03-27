fruits = {
    "apple": 12,
    "pear": 6,
    "orange": 10,
    "kiwi": 9,
}

print(fruits["apple"])  # prints out 12
print(fruits["banana"])  # raises an exception

print(fruits.get("banana"))  # prints out None
print(fruits.get("banana", 0))  # prints out 0
