bases = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}


def _gen(n, unit='C', next_half='D', next_unit='M'):
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
    thousands = (n // 1000 % 10)
    hundreds = (n // 100 % 10)
    tens = (n // 10 % 10)
    ones = n % 10
    return _gen(thousands, 'M', 'V̅', 'X̅') + \
           _gen(hundreds, 'C', 'D', 'M') + \
           _gen(tens, 'X', 'L', 'C') + \
           _gen(ones, 'I', 'V', 'X')
