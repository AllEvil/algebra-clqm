
from .Integer import *
from .Natural import *

__all__ = ["Rational"]

class Rational():

    def __init__(self, n, m):
        self._numerator = Integer(n)
        self._denumerator = Natural(m)

    def __str__(self):
        return str(self._numerator) + " / " + str(self._denumerator)

    def integer_to_rational(self, n):
        # Преобразование целого числа в дробное
        # Трибунский Алексей
        self._numerator = n
        self._denumerator = "1"