class Fruit:
    def __init__(self, kind, amount=1):
        self.kind = kind
        self.amount = amount

    def add(self, fruit):
        if isinstance(fruit, Fruit) and self.kind == fruit.kind:
            self.amount += fruit.amount
            return True
        return False

    def __add__(self, other):
        self.add(other)
        return self

    def __len__(self):
        return self.amount

    def __str__(self):
        return f"{len(self)} {self.kind}"


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

    def __str__(self):
        return f"A box of {len(self)} {self.kind}s"
