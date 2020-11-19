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


def to_roman(n: int) -> str:
    if n in range(1000):
        hundreds = (n // 100) * 100
        tens = (n // 10) * 10
        ones = n % 10
        return _hundreds(hundreds) + _tens(tens) + _ones(ones)
    return 'stub'
