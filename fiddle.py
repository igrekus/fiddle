def _digit_to_roman(n, unit, next_half, next_unit):
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
    return ''.join(_digit_to_roman(v, *units) for v, units in zip(
        map(int, f'{n:04d}'),
        [['M', 'V̅', 'X̅'],
         ['C', 'D', 'M'],
         ['X', 'L', 'C'],
         ['I', 'V', 'X']]
    ))
