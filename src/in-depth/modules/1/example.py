from fruits import Apple, Basket, BoxOf, Container, Kiwi, Orange, Pear

apple = Apple()
pear = Pear()
orange = Orange()
kiwi = Kiwi()
box_of_oranges = BoxOf(Orange(), 6)
container = Container()

basket = Basket()
basket += apple
basket += box_of_oranges
basket += container
basket += pear
basket += kiwi
basket += orange

print(basket)
# prints out:
# The basket contains:
# 1 apple
# A box of 7 oranges
# ------------------
# | A container with
# |  1 pear
# |  1 kiwi
# ------------------
