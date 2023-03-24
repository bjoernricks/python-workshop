def ask_computer(a, b):
    if a > b:
        return "no"
    else:
        return "yes"


i = 0
while i <= 3:
    computer_says = ask_computer(i, 2)
    print("Computer says", computer_says)
    i = i + 1


# iterating over the elements of a list
i = 0
checks = [2, 0, 3, 1]
while i < len(checks):
    check_value = checks[i]
    computer_says = ask_computer(check_value, 2)
    print("Computer says", computer_says)
    i = i + 1
