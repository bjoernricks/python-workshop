class Person:
    last_name = "Doe"

    def __init__(self, first_name, age=None):
        self.first_name = first_name
        self.age = age

    def set_last_name(self, last_name):
        self.last_name = last_name

    def who_am_i(self):
        print(f"I am {self.first_name} {self.last_name}", end="")
        if self.age:
            print(f" and I am {self.age}.")
        else:
            print(".")


john = Person("John")
jack = Person("Jack", 33)

jack.set_last_name("Bauer")

john.who_am_i()  # prints out I am John Doe.
jack.who_am_i()  # prints out I am Jack Bauer and I am 33.
