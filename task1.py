from math import gcd


class Rational:

    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.find_gcd()

    def find_gcd(self):
        greatest_common_divisor = gcd(self.__numerator, self.__denominator)
        self.__numerator //= greatest_common_divisor
        self.__denominator //= greatest_common_divisor

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
        if isinstance(other, Rational):
            numerator = other.__denominator * self.__numerator + other.__numerator * self.__denominator
            denominator = self.__denominator * other.__denominator
            return Rational(numerator, denominator)
        if isinstance(other, int):
            numerator = self.__numerator + self.__denominator * other
            return Rational(numerator, self.__denominator)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Rational):
            numerator = other.__denominator * self.__numerator - other.__numerator * self.__denominator
            denominator = self.__denominator * other.__denominator
            return Rational(numerator, denominator)
        if isinstance(other, int):
            numerator = self.__numerator - self.__denominator * other
            return Rational(numerator, self.__denominator)
        raise TypeError

    def __mul__(self, other):
        if isinstance(other, Rational):
            numerator = self.__numerator * other.__numerator
            denominator = self.__denominator * other.__denominator
            return Rational(numerator, denominator)
        if isinstance(other, int):
            numerator = self.__numerator * other
            return Rational(numerator, self.__denominator)
        raise TypeError

    def __truediv__(self, other):
        if isinstance(other, Rational):
            numerator = self.__numerator * other.__denominator
            denominator = self.__denominator * other.__numerator
            return Rational(numerator, denominator)
        if isinstance(other, int):
            denominator = self.__denominator * other
            return Rational(self.__numerator, denominator)
        raise TypeError

    def __iadd__(self, other):
        if isinstance(other, Rational):
            self.__numerator = other.__denominator * self.__numerator + other.__numerator * self.__denominator
            self.__denominator = self.__denominator * other.__denominator
            self.find_gcd()
            return self
        if isinstance(other, int):
            self.__numerator = self.__numerator + self.__denominator * other
            self.find_gcd()
            return self
        raise TypeError

    def __isub__(self, other):
        if isinstance(other, Rational):
            self.__numerator = other.__denominator * self.__numerator - other.__numerator * self.__denominator
            self.__denominator = self.__denominator * other.__denominator
            self.find_gcd()
            return self
        if isinstance(other, int):
            self.__numerator = self.__numerator - self.__denominator * other
            self.find_gcd()
            return self
        raise TypeError

    def __imul__(self, other):
        if isinstance(other, Rational):
            self.__numerator *= other.__numerator
            self.__denominator *= other.__denominator
            self.find_gcd()
            return self
        if isinstance(other, int):
            self.__numerator *= other
            self.find_gcd()
            return self
        raise TypeError

    def __itruediv__(self, other):
        if isinstance(other, Rational):
            self.__numerator *= other.__denominator
            self.__denominator *= other.__numerator
            self.find_gcd()
            return self
        if isinstance(other, int):
            self.__denominator *= other
            self.find_gcd()
            return self
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.result() == other.result()
        if isinstance(other, (int, float)):
            return self.result() == other
        raise TypeError

    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.result() < other.result()
        if isinstance(other, (int, float)):
            return self.result() < other
        raise TypeError

    def __le__(self, other):
        if isinstance(other, Rational):
            return self.result() <= other.result()
        if isinstance(other, (int, float)):
            return self.result() <= other
        raise TypeError

    def __ne__(self, other):
        if isinstance(other, Rational):
            return self.result() != other.result()
        if isinstance(other, (int, float)):
            return self.result() != other
        raise TypeError

    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.result() > other.result()
        if isinstance(other, (int, float)):
            return self.result() > other
        raise TypeError

    def __ge__(self, other):
        if isinstance(other, Rational):
            return self.result() >= other.result()
        if isinstance(other, (int, float)):
            return self.result() >= other
        raise TypeError

    def fraction(self):
        return f'{self.__numerator} / {self.__denominator}'

    def result(self):
        return self.__numerator / self.__denominator
