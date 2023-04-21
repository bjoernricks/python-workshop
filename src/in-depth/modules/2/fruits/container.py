class Basket:
    def __init__(self) -> None:
        self.fruits = []

    def add(self, new_fruit):
        for fruit in self.fruits:
            if fruit.add(new_fruit):
                return True

        self.fruits.append(new_fruit)
        return True

    def __len__(self):
        return len(self.fruits)

    def __add__(self, other):
        self.add(other)
        return self

    def __str__(self):
        output = ["The basket contains:"]
        for fruit in self.fruits:
            output.append(str(fruit))
        return "\n".join(output)


class Container(Basket):
    def __str__(self):
        output = ["------------------"]
        for fruit in self.fruits:
            output.append(f"|  {str(fruit)}")
        output.append("------------------")
        return "\n".join(output)
