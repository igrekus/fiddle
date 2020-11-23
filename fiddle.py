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


def _ones_from_roman(roman):
    it = iter(roman)
    char = next(it)
    if char == 'I':
        char = next(it, None)
        if char is None:
            return 1
        if char == 'V':
            return 4
        if char == 'X':
            return 9
        char = next(it, None)
        if char is None:
            return 2
        if char == 'I':
            return 3

    if char == 'V':
        char = next(it, None)
        if char is None:
            return 5
        if char == 'I':
            char = next(it, None)
            if char is None:
                return 6
            if char == 'I':
                char = next(it, None)
                if char is None:
                    return 7
                if char == 'I':
                    return 8


def _tens_from_roman(roman):
    if roman == 'X':
        return 10
    if roman == 'XX':
        return 20
    if roman == 'XXX':
        return 30
    if roman == 'XL':
        return 40
    if roman == 'L':
        return 50
    if roman == 'LX':
        return 60
    if roman == 'LXX':
        return 70
    if roman == 'LXXX':
        return 80
    if roman == 'XC':
        return 90


def parse_roman(roman: str) -> int:
    if roman in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']:
        return _ones_from_roman(roman)
    if roman in ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', ]:
        return _tens_from_roman(roman)
    return -1
