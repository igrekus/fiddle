from collections import Counter
from functools import reduce

_romans = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
           50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}


def to_roman(n: int) -> str:
    _tbl = _romans
    _func = lambda accum, el: (accum[0] + (accum[1] // el) * _tbl[el], accum[1] - (accum[1] // el) * el)
    return reduce(_func, _tbl.keys(), ("", n))[0]


def from_roman(roman: str) -> int:
    _tbl = {v: k for k, v in _romans.items()}

    _func = lambda accum, sym: accum[:-1] + [accum[-1] + sym] if accum and accum[-1] + sym in _tbl else accum + [sym]
    _is_descending = lambda seq: all(seq[idx] >= seq[idx + 1] for idx in range(len(seq) - 1))
    _is_counted = lambda seq: all(
        (lambda k, v: v <= 3 and len(k) == 1 or v <= 1 and len(k) == 2)(k, v) for k, v in Counter(seq).items())
    _is_valid = lambda seq: all(el in _tbl for el in seq) and _is_counted(seq) and _is_descending(
        [_tbl[el] for el in seq])

    return (lambda seq: sum(_tbl[el] for el in seq) if _is_valid(seq) else -1)(reduce(_func, roman, []))
