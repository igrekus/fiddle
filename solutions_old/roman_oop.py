import re


class Roman:
    _pairs = [('M', 1000),
              ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
              ('XC', 90), ('L', 50), ('XL', 40), ('X', 10),
              ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
    _validator = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')

    def __init__(self, n: int):
        self._value = n

    def __str__(self):
        ret = ''
        for roman, arabic in Roman._pairs:
            repeats, self._value = divmod(self._value, arabic)
            ret += roman * repeats
        return ret

    @property
    def arab(self):
        return self._value

    @property
    def roman(self):
        return str(self)

    @classmethod
    def from_string(cls, roman):
        if not cls._is_valid(roman):
            return cls(-1)
        total = 0
        for digit, value in cls._pairs:
            while roman.startswith(digit):
                total += value
                roman = roman[len(digit):]
        return cls(total)

    @staticmethod
    def _is_valid(roman):
        return roman and bool(Roman._validator.match(roman))


def to_roman(n: int) -> str:
    return Roman(n).roman


def parse_roman(roman):
    return Roman.from_string(roman).arab
