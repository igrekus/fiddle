def _gen(n, unit, next_half, next_unit):
    if n in [1, 2, 3]:
        return unit * n
    if n in [4, 5]:
        return unit * (5 - n) + next_half
    if n in [6, 7, 8]:
        return next_half + unit * (n - 5)
    if n in [9]:
        return unit * (10 - 9) + next_unit
    return ''


def to_roman(n: int) -> str:
    thousands = n // 1000 % 10
    hundreds = n // 100 % 10
    tens = n // 10 % 10
    ones = n % 10
    return ''.join(_gen(v, *txt) for v, txt in zip(
        [thousands, hundreds, tens, ones],
        [['M', 'V̅', 'X̅'], ['C', 'D', 'M'], ['X', 'L', 'C'], ['I', 'V', 'X'], ]
    ))
