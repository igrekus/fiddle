import re


class Roman:
    _letters = {
        1000: ['M', 'V̅', 'X̅'],
        100: ['C', 'D', 'M'],
        10: ['X', 'L', 'C'],
        1: ['I', 'V', 'X'],
    }
    _pairs = [('M', 1000),
              ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
              ('XC', 90), ('L', 50), ('XL', 40), ('X', 10),
              ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

    _validator = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')

    def __init__(self, n: int):
        self._arab = n
        self._digits = {} if n == -1 else {k: self._arab // k % 10 for k in [1000, 100, 10, 1]}

    def __str__(self):
        return f'{self[1000]}{self[100]}{self[10]}{self[1]}'

    def __getitem__(self, item):
        return self._digit_to_roman(self._digits[item], *self._letters[item])

    @property
    def arab(self):
        return self._arab

    @property
    def roman(self):
        return str(self)

    @classmethod
    def from_string(cls, roman):
        if not cls._is_valid(roman):
            return cls(-1)
        total = 0
        for symbol, value in cls._pairs:
            while roman.startswith(symbol):
                total += value
                roman = roman[len(symbol):]
        return cls(total)

    @staticmethod
    def _digit_to_roman(n, unit, next_half, next_unit):
        if n in (1, 2, 3):
            return unit * n
        elif n in (4, 5):
            return unit * (5 - n) + next_half
        elif n in (6, 7, 8):
            return next_half + unit * (n - 5)
        elif n == 9:
            return unit + next_unit
        return ''

    @staticmethod
    def _is_valid(roman):
        return roman and bool(Roman._validator.match(roman))


def to_roman(n: int) -> str:
    return Roman(n).roman


def parse_roman(roman):
    return Roman.from_string(roman).arab
