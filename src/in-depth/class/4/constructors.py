class Person:
    last_name = "Doe"

    def __init__(self, first_name, age=None):
        self.first_name = first_name
        self.age = age


john = Person("John")
jack = Person("Jack", 33)

print(john.last_name)  # prints out Doe
print(john.first_name)  # prints out John

print(jack.last_name)  # prints out Doe
print(jack.first_name)  # prints out Jack
print(jack.age)  # prints out 33

print(john.age)  # john's age is not set. This time it will just print None.

# changing a class variables still changes the value for all instances
Person.last_name = "Taylor"

print(jack.last_name)  # prints out Taylor
print(john.last_name)  # prints out Taylor
