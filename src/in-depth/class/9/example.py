class Fruit:
    def __init__(self, kind, amount=1):
        self.kind = kind
        self.amount = amount


class Basket:
    def __init__(self) -> None:
        self.fruits = {}

    def add(self, fruit):
        current_amount = self.fruits.get(fruit.kind, 0)
        self.fruits[fruit.kind] = current_amount + fruit.amount

    def print(self):
        print("The basket contains:")
        for key, value in self.fruits.items():
            print(f"{value} {key}")


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


class BoxOfOranges(Fruit):
    def __init__(self, amount):
        super().__init__("orange", amount)


apple = Apple()
pear = Pear()
orange = Orange()
kiwi = Kiwi()

basket = Basket()
basket.add(apple)
basket.add(pear)
basket.add(orange)
basket.add(kiwi)
# add a box of oranges
box_of_oranges = BoxOfOranges(6)
basket.add(box_of_oranges)

basket.print()
# prints out:
# The basket contains:
# 1 apple
# 1 pear
# 7 orange
# 1 kiwi
