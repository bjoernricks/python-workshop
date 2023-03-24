a = [1, 2]

a.insert(1, 3)  # insert 3 at index 1 (remember zero indexing)
print(a)  # prints out [1, 3, 2]

a.insert(99999, 4)  # gets appended
print(a)  # prints out [1, 3, 2, 4]
