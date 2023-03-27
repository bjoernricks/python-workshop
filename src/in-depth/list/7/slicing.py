colors = ["red", "green", "blue", "orange"]

print(colors[0:1])  # prints out ["red"]
print(colors[2:4])  # prints out ["blue", "orange"]

print(colors[1:-1])  # prints out ["green", "blue"]
print(colors[-4:-3])  # prints out ["red"]

print(colors[3 : len(colors)])  # prints out ["orange"]
print(colors[3:])  # prints out world ["orange"]

print(colors[:2])  # prints out ["red", "green"]

# creates a copy (!) of the list, prints out ["red", "green", "blue", "orange"]
print(colors[:])

# no exception, prints out ["red", "green", "blue", "orange"]
print(colors[0:100])
print(colors[100:])  # no exception, prints out empty list
