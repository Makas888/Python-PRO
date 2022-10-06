# 2) Создайте класс «Правильная дробь» и реализуйте методы сравнения,
# сложения, вычитания и произведения для экземпляров этого класса.
import math


class Proper_fraction:
    """
    It takes two parameters (a=numerator, b=denominator) "a" must be less than "b".
    Implements comparison, addition, subtraction, and product methods for instances of this class.
    """

    def __init__(self, a, b):
        if not isinstance(a, int):
            raise ValueError('"a" is not "int"')
        if not isinstance(b, int):
            raise ValueError('"b" is not "int"')
        if a <= 0 or b <= 0:
            raise ValueError('value "a" or "b" cannot be less than zero')
        self.a = a
        self.b = b

    def __add__(self, other):
        if isinstance(other, Proper_fraction):
            return Proper_fraction(self.a * other.b + self.b * other.a, self.b * other.b)
        if isinstance(other, int):
            return Proper_fraction(self.a + self.b * other, self.b)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int):
            return Proper_fraction(self.a + self.b * other, self.b)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Proper_fraction):
            self.a = self.a * other.b + self.b * other.a
            self.b *= other.b
            return self
        if isinstance(other, int):
            self.a += self.b * other
            return self
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Proper_fraction):
            return Proper_fraction(self.a * other.b - self.b * other.a, self.b * other.b)
        if isinstance(other, int):
            return Proper_fraction(self.a - self.b * other, self.b)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, int):
            return Proper_fraction(self.b * other - self.a, self.b)
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, int):
            self.a -= self.b * other
            return self
        if isinstance(other, Proper_fraction):
            self.a = self.a * other.b - self.b * other.a
            self.b *= other.b
            return self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return Proper_fraction(self.a * other, self.b)
        if isinstance(self, Proper_fraction) and isinstance(other, Proper_fraction):
            return Proper_fraction(self.a * other.a, self.b * other.b)
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int):
            return Proper_fraction(self.a * other, self.b)
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            self.a *= other
            return self
        elif isinstance(other, Proper_fraction):
            self.a *= other.b
            self.b *= other.a
            return self
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Proper_fraction):
            return self.a * other.b < other.a * self.b
        if isinstance(other, int):
            return self.a < other * self.b
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, int):
            return self.a > other * self.b
        return NotImplemented

    def __ge__(self, other):
        if other == 0:
            raise ZeroDivisionError('can not by zero')
        if isinstance(other, Proper_fraction):
            return self.a * other.b >= other.a * self.b
        if isinstance(other, int):
            return self.a >= other * self.b
        return NotImplemented

    def __le__(self, other):
        if other == 0:
            raise ZeroDivisionError('can not by zero')
        if isinstance(other, int):
            return self.a <= other * self.b
        return NotImplemented

    def __eq__(self, other):
        if other == 0:
            raise ZeroDivisionError('can not by zero')
        if isinstance(other, Proper_fraction):
            return self.a * other.b == other.a * self.b
        if isinstance(other, int):
            return self.a == other * self.b
        return NotImplemented

    def __ne__(self, other):
        if other == 0:
            raise ZeroDivisionError('can not by zero')
        if isinstance(other, int):
            return self.a != other * self.b
        return NotImplemented

    def __str__(self):
        cd = math.gcd(self.a, self.b)
        if self.a == 0:
            raise '0'
        if self.a == self.b:
            return '1'
        if self.b // cd == 1:
            return f'{self.a // self.b}'
        if self.a > self.b:
            return f'{self.a // self.b} whole {self.a % self.b // cd}/{self.b // cd}'
        else:
            return f'{self.a // cd}/{self.b // cd}'


if __name__ == '__main__':

    try:
        fr = Proper_fraction(2, 1)
        fr1 = Proper_fraction(2, 6)
        print(fr, fr1, sep='\n')

        print(fr >= 2)
        print(2 >= fr1)
        print(fr != 2)
        print(fr == 2)
        print(2 < fr)
        print(fr < 2)

        fr3 = fr1 + fr
        print(fr3)
        fr4 = fr - fr1
        print(fr4)
        fr5 = fr * fr1
        print(fr5)
        fr += fr1
        print(fr)
        fr6 = 2 * fr
        print(fr6)
        x = fr + 5 + 5

        print(x)
    except Exception as error:
        print(error)
