output = "Hello world"
print(output[0])  # zero based indexing, prints out H
print(output[6])  # prints out w
print(output[11])  # accessing an item outside of the range raises an exception
print(output[len(output) - 1])  # last character (remember zero based indexing)
print(output[-1])  # or just use builtin minus indexing :-)
print(output[-11])  # first item again
print(output[-12])  # outside of the range, an exception is raised

# get the index of a character
where_is_the_w = output.index("w")
print(where_is_the_w)  # prints out 6
print(output[where_is_the_w])  # index access with variables, prints out w
