from functools import reduce
from re import match

_romans = {1000: "M",
           900: "CM", 500: "D", 400: "CD", 100: "C",
           90: "XC", 50: "L", 40: "XL", 10: "X",
           9: "IX", 5: "V", 4: "IV", 1: "I"}


def to_roman(n: int) -> str:
    _tbl = _romans
    _func = lambda accum, el: (accum[0] + (accum[1] // el) * _tbl[el], accum[1] - (accum[1] // el) * el)
    return reduce(_func, _tbl.keys(), ("", n))[0]


def parse_roman(roman: str) -> int:
    _tbl = {v: k for k, v in _romans.items()}
    _roman_regex = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

    _func = lambda accum, sym: accum[:-1] + [accum[-1] + sym] if accum and accum[-1] + sym in _tbl else accum + [sym]
    _is_valid = lambda s: s and match(_roman_regex, s)

    return (lambda seq: sum(_tbl[el] for el in seq) if _is_valid(roman) else -1)(reduce(_func, roman, []))
