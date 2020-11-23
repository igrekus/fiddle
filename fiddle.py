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


def _ones_from_roman():
    pass


def parse_roman(roman: str) -> int:
    it = iter(roman)
    char = next(it)
    if char == 'I':
        if roman == 'II':
            return 2
        if roman == 'III':
            return 3
        if roman == 'IV':
            return 4
        if roman == 'IX':
            return 9
        return 1

    if char == 'V':
        if roman == 'VI':
            return 6
        if roman == 'VII':
            return 7
        if roman == 'VIII':
            return 8
        return 5
    return 0
