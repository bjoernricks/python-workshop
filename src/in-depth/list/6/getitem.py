colors = ["red", "green", "blue", "orange"]

print(colors[0])  # first item (zero indexing), prints out red
print(colors[3])  # first item (zero indexing), prints out orange
print(colors[11])  # accessing an item outside of the range raises an exception
print(colors[-1])  # last color, prints out orange
print(colors[-4])  # first item again
print(colors[-5])  # first item again
print(colors[-6])  # outside of the range, an exception is raised

# get the index of a color
where_is_blue = colors.index("blue")
print(where_is_blue)  # prints out 2
print(colors[where_is_blue])  # index access with variables, prints out blue
