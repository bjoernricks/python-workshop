def ask_computer(a, b):
    if a > b:
        return "no"
    else:
        return "yes"


checks = [2, 0, 3, 1]
for check_value in checks:
    computer_says = ask_computer(check_value, 2)
    print("Computer says", computer_says)
