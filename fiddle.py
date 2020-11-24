def _digit_to_roman(n, unit, half, next_unit):
    if n == '0':
        return ''
    if n in '123':
        return unit * int(n)
    if n in '45':
        return unit * (5 - int(n)) + half
    if n in '678':
        return half + unit * (int(n) - 5)
    if n == '9':
        return unit + next_unit


def to_roman(n: int) -> str:
    return ''.join(_digit_to_roman(v, *units) for v, units in zip(
        f'{n:04d}',
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


def _from_roman(roman, unit, half, next_unit):
    mul = multipliers[unit]
    ret = 0

    it = iter(roman)
    char = next(it)
    if char == unit:
        char = next(it, None)
        if char is None:
            ret = 1 * mul
        elif char == half:
            ret = 4 * mul
        elif char == next_unit:
            ret = 9 * mul
        else:
            char = next(it, None)
            if char is None:
                ret = 2 * mul
            elif char == unit:
                ret = 3 * mul

    elif char == half:
        char = next(it, None)
        if char is None:
            ret = 5 * mul
        elif char == unit:
            char = next(it, None)
            if char is None:
                ret = 6 * mul
            elif char == unit:
                char = next(it, None)
                if char is None:
                    ret = 7 * mul
                elif char == unit:
                    ret = 8 * mul
    return ret


def _ones_from_roman(roman):
    return _from_roman(roman, unit='I', half='V', next_unit='X')


def _tens_from_roman(roman):
    return _from_roman(roman, unit='X', half='L', next_unit='C')


def _hundreds_from_roman(roman):
    return _from_roman(roman, unit='C', half='D', next_unit='M')


def _thousands_from_roman(roman):
    return _from_roman(roman, unit='M', half='V̅', next_unit='X̅')


def parse_roman(roman: str) -> int:
    if roman in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']:
        return _ones_from_roman(roman)
    if roman in ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', ]:
        return _tens_from_roman(roman)
    if roman in ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']:
        return _hundreds_from_roman(roman)
    if roman in ['M', 'MM', 'MMM']:
        return _thousands_from_roman(roman)
    return _tens_from_roman(roman)
