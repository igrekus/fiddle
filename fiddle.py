def _digit_to_roman(n, unit, next_half, next_unit):
    if n in [1, 2, 3]:
        return unit * n
    if n in [4, 5]:
        return unit * (5 - n) + next_half
    if n in [6, 7, 8]:
        return next_half + unit * (n - 5)
    if n == 9:
        return unit + next_unit
    return ''


def to_roman(n: int) -> str:
    return ''.join(_digit_to_roman(v, *units) for v, units in zip(
        map(int, f'{n:04d}'),
        [['M', 'V̅', 'X̅'],
         ['C', 'D', 'M'],
         ['X', 'L', 'C'],
         ['I', 'V', 'X']]
    ))


multipliers = {
    'I': 1,
    'X': 10,
    'C': 100,
    'M': 1000,
}


def _from_roman(roman, unit='I', half='V', next_unit='X'):
    mul = multipliers[unit]
    it = iter(roman)
    char = next(it)
    if char == unit:
        char = next(it, None)
        if char is None:
            return 1 * mul
        if char == half:
            return 4 * mul
        if char == next_unit:
            return 9 * mul
        char = next(it, None)
        if char is None:
            return 2 * mul
        if char == unit:
            return 3 * mul

    if char == half:
        char = next(it, None)
        if char is None:
            return 5 * mul
        if char == unit:
            char = next(it, None)
            if char is None:
                return 6 * mul
            if char == unit:
                char = next(it, None)
                if char is None:
                    return 7 * mul
                if char == unit:
                    return 8 * mul


def _ones_from_roman(roman):
    return _from_roman(roman, unit='I', half='V', next_unit='X')


def _tens_from_roman(roman):
    it = iter(roman)
    char = next(it)
    if char == 'X':
        char = next(it, None)
        if char is None:
            return 10
        if char == 'L':
            return 40
        if char == 'C':
            return 90
        char = next(it, None)
        if char is None:
            return 20
        if char == 'X':
            return 30

    if char == 'L':
        char = next(it, None)
        if char is None:
            return 50
        if char == 'X':
            char = next(it, None)
            if char is None:
                return 60
            if char == 'X':
                char = next(it, None)
                if char is None:
                    return 70
                if char == 'X':
                    return 80


def _hundreds_from_roman(roman):
    it = iter(roman)
    char = next(it)
    if char == 'C':
        char = next(it, None)
        if char is None:
            return 100
        if char == 'D':
            return 400
        if char == 'M':
            return 900
        char = next(it, None)
        if char is None:
            return 200
        if char == 'C':
            return 300

    if char == 'D':
        char = next(it, None)
        if char is None:
            return 500
        if char == 'C':
            char = next(it, None)
            if char is None:
                return 600
            if char == 'C':
                char = next(it, None)
                if char is None:
                    return 700
                if char == 'C':
                    return 800


def _thousands_from_roman(roman):
    it = iter(roman)
    char = next(it)
    if char == 'M':
        char = next(it, None)
        if char is None:
            return 1000
        if char == 'V̅':
            return 4000
        if char == 'X̅':
            return 9000
        char = next(it, None)
        if char is None:
            return 2000
        if char == 'M':
            return 3000

    if char == 'V̅':
        char = next(it, None)
        if char is None:
            return 5000
        if char == 'M':
            char = next(it, None)
            if char is None:
                return 6000
            if char == 'M':
                char = next(it, None)
                if char is None:
                    return 7000
                if char == 'M':
                    return 8000


def parse_roman(roman: str) -> int:
    if roman in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']:
        return _ones_from_roman(roman)
    if roman in ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', ]:
        return _tens_from_roman(roman)
    if roman in ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']:
        return _hundreds_from_roman(roman)
    if roman in ['M', 'MM', 'MMM']:
        return _thousands_from_roman(roman)
    return -1
