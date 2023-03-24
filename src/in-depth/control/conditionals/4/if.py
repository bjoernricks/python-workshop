def say_yes_please(condition):
    if condition:
        print("Computer says yes")


say_yes_please(True)
say_yes_please(False)
say_yes_please(1 > 2)
say_yes_please(None)  # None evaluates to False
say_yes_please("")  # Empty string evaluates to False
say_yes_please("some text")  # evaluates to True
say_yes_please([])  # Empty list evaluates to False
say_yes_please([1, 2, 3])  # evaluates to True
