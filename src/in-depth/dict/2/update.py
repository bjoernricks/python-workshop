fruits = {
    "apple": 12,
    "pear": 6,
    "orange": 10,
    "kiwi": 9,
}

fruits["banana"] = 7  # adding a new item
print(fruits)

fruits["orange"] = 13  # updating an item
print(fruits)

fruits.update({"apple": 13, "mango": 3})  # update from another dict
print(fruits)
