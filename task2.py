class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError
        if other < 0:
            raise ValueError

        return Item(self.__name, other + self.__quantity, self.__price)

    def __radd__(self, other):
        if not isinstance(other, int):
            raise TypeError
        if other < 0:
            raise ValueError

        return Item(self.__name, other + self.__quantity, self.__price)

    def __sub__(self, other):
        if not isinstance(other, int):
            raise TypeError
        if self.__quantity - other < 0:
            raise ValueError

        return Item(self.__name, self.__quantity - other, self.__price)

    def __rsub__(self, other):
        if not isinstance(other, int):
            raise TypeError
        if other - self.__quantity < 0:
            raise ValueError

        return Item(self.__name, other - self.__quantity, self.__price)

    def __iadd__(self, other):
        if not isinstance(other, int):
            raise TypeError
        if other < 0:
            raise ValueError

        self.__quantity += other
        return self

    def __isub__(self, other):
        if not isinstance(other, int):
            raise TypeError
        if self.__quantity - other < 0:
            raise ValueError

        self.__quantity -= other
        return self

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError

        self.__name = name

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError
        if quantity < 0:
            raise ValueError

        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise TypeError
        if price < 0:
            raise ValueError

        self.__price = price


class Composition:
    def __init__(self, products):
        self.__products = products

    def __add__(self, other):
        if not isinstance(other, Item):
            raise TypeError
        return Composition(self.__products + other)

    def __radd__(self, other):
        if not isinstance(other, Item):
            raise TypeError
        return Composition(self.__products + other)

    def __iadd__(self, other):
        if not isinstance(other, Item):
            raise TypeError
        self.__products += other
        return self

    def __sub__(self, other):
        if not isinstance(other, Item):
            raise TypeError
        if not (other in self.__products):
            raise ValueError
        return Composition(self.__products.remove(other))

    def __rsub__(self, other):
        if not isinstance(other, Item):
            raise TypeError
        if not (other in self.__products):
            raise ValueError
        return Composition(self.__products.remove(other))

    def __isub__(self, other):
        if not isinstance(other, Item):
            raise TypeError
        if not (other in self.__products):
            raise ValueError
        self.__products = self.__products.remove(other)
        return self

    def __mul__(self, other):
        if not isinstance(other, Item):
            raise TypeError
        if not (other in self.__products):
            raise ValueError
        return other.__quantity


obj = Composition("dd", 9, 9)
if obj:
    print("yjhd")
