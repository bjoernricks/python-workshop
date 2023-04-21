class Fruit:
    def __init__(self, kind):
        self.kind = kind


class Basket:
    def __init__(self) -> None:
        self.fruits = {}

    def add(self, fruit):
        current_amount = self.fruits.get(fruit.kind, 0)
        self.fruits[fruit.kind] = current_amount + 1

    def print(self):
        print("The basket contains:")
        for key, value in self.fruits.items():
            print(f"{value} {key}")


apple = Fruit("apple")
pear = Fruit("pear")
orange = Fruit("orange")
kiwi = Fruit("kiwi")

basket = Basket()
basket.add(apple)
basket.add(pear)
basket.add(orange)
basket.add(kiwi)

basket.print()
# prints out:
# The basket contains:
# 1 apple
# 1 pear
# 1 orange
# 1 kiwi

# we'll add another orange
another_orange = Fruit("orange")
basket.add(another_orange)

basket.print()
# prints out:
# The basket contains:
# 1 apple
# 1 pear
# 1 orange
# 1 kiwi
