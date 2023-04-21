class Person:
    last_name = "Doe"


# create an instance of the class Person (an object) named john
john = Person()
# by default it is possible to assign additional variables
john.first_name = "John"

jack = Person()
jack.first_name = "Jack"
jack.age = 33

print(john.last_name)  # prints out Doe
print(john.first_name)  # prints out John

print(jack.last_name)  # prints out Doe
print(jack.first_name)  # prints out Jack
print(jack.age)  # prints out 33

print(john.age)  # john has no age. This will raise an error.

# changing a class variables changes the value for all instances
Person.last_name = "Taylor"

print(jack.last_name)  # prints out Taylor
print(john.last_name)  # prints out Taylor
