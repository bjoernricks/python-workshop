output = "Hello world"
print(output.upper())
print(output.lower())

print(output.startswith("Hello"))  # prints out True
print(output.startswith("hello"))  # prints out False
print(output.endswith("world"))  # prints out True
print(output.startswith("World"))  # prints out False

splitted = output.split(" ")  # returns a tuple
print(splitted)
