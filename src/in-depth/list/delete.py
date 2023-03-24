colors = ["red", "green", "blue", "orange"]

del colors[1]  # delete item at index 1
print(colors)  # prints out ["red", "blue", "orange"]

del colors[1:]  # delete a slice from the list
print(colors)  # prints out ["red"]
