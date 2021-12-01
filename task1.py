from math import gcd


class Rational:

    def __init__(self, numerator=1, denominator=1):
        self.__numerator = numerator // gcd(numerator, denominator)
        self.__denominator = denominator // gcd(numerator, denominator)

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise TypeError
        self.__numerator = numerator

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator):
        if not isinstance(denominator, int):
            raise TypeError
        if not denominator:
            raise ValueError

        self.__denominator = denominator
        
    def __add__(self, other):
        return self.result() + other.result()

    def __sub__(self, other):
        return self.result() - other.result()

    def __mul__(self, other):
        return self.result() * other.result()

    def __truediv__(self, other):
        return self.result() / other.result()

    def __eq__(self, other):
        return self.result() == other.result()

    def fraction(self):
        return f'{self.__numerator} / {self.__denominator}'

    def result(self):
        return self.__numerator / self.__denominator
