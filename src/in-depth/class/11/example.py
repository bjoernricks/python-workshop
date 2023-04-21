class Fruit:
    def __init__(self, kind, amount=1):
        self.kind = kind
        self.amount = amount

    def add(self, fruit):
        if isinstance(fruit, Fruit) and self.kind == fruit.kind:
            self.amount += fruit.amount
            return True
        return False

    def print(self):
        print(f"{self.amount} {self.kind}")


class Basket:
    def __init__(self) -> None:
        self.fruits = []

    def add(self, new_fruit):
        for fruit in self.fruits:
            if fruit.add(new_fruit):
                return True

        self.fruits.append(new_fruit)
        return True

    def print(self):
        print("The basket contains:")
        for fruit in self.fruits:
            fruit.print()


class Apple(Fruit):
    def __init__(self):
        super().__init__("apple")


class Pear(Fruit):
    def __init__(self):
        super().__init__("pear")


class Orange(Fruit):
    def __init__(self):
        super().__init__("orange")


class Kiwi(Fruit):
    def __init__(self):
        super().__init__("kiwi")


class BoxOf(Fruit):
    def __init__(self, fruit, amount):
        super().__init__(fruit.kind, amount)

    def print(self):
        print(f"A box of {self.amount} {self.kind}s")


class Container(Basket):
    def print(self):
        print("------------------")
        print("| A container with")
        for fruit in self.fruits:
            print("|  ", end="")
            fruit.print()
        print("-----------------")


apple = Apple()
pear = Pear()
orange = Orange()
kiwi = Kiwi()
box_of_oranges = BoxOf(Orange(), 6)
container = Container()

basket = Basket()
basket.add(apple)
basket.add(box_of_oranges)
basket.add(container)
basket.add(pear)
basket.add(kiwi)
basket.add(orange)

basket.print()
# prints out:
# The basket contains:
# 1 apple
# A box of 7 oranges
# ------------------
# | A container with
# |  1 pear
# |  1 kiwi
# ------------------
