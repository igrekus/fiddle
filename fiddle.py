bases = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}


def _ones(n):
    if n in [1, 2, 3]:
        return 'I' * n
    if n in [4, 5]:
        return 'I' * (5 - n) + 'V'
    if n in [6, 7, 8]:
        return 'V' + 'I' * (n - 5)
    if n in [9]:
        return 'I' * (10 - n) + 'X'
    return ''


def _tens(n):
    if n in [10, 20, 30]:
        return 'X' * (n // 10)
    if n in [40, 50]:
        return 'X' * (50 // 10 - n // 10) + 'L'
    if n in [60, 70, 80]:
        return 'L' + 'X' * (n // 10 - 50 // 10)
    if n in [90]:
        return 'X' * (100 // 10 - 90 // 10) + 'C'
    return ''


def _hundreds(n):
    if n in [100, 200, 300]:
        return 'C' * (n // 100)
    if n in [400, 500]:
        return 'C' * (500 // 100 - n // 100) + 'D'
    if n in [600, 700, 800]:
        return 'D' + 'C' * (n // 100 - 500 // 100)
    if n in [900]:
        return 'C' * (1000 // 100 - 900 // 100) + 'M'
    return ''


def _thousands(n):
    if n in [1000, 2000, 3000]:
        return 'M' * (n // 1000)
    if n in [4000, 5000]:
        return 'C' * (5000 // 1000 - n // 1000) + 'D'
    if n in [6000, 7000, 8000]:
        return 'D' + 'C' * (n // 1000 - 5000 // 1000)
    if n in [9000]:
        return 'C' * (10000 // 1000 - 9000 // 1000) + 'M'
    return ''


def _gen(n, place=100, unit='C', next_half='D', next_unit='M'):
    n //= place
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
    if n in range(4000):
        thousands = (n // 1000 % 10) * 1000
        hundreds = (n // 100 % 10) * 100
        tens = (n // 10 % 10) * 10
        ones = n % 10
        return _thousands(thousands) + _gen(hundreds, 100, 'C', 'D', 'M') + _tens(tens) + _ones(ones)
    return 'stub'
