import re

_digit = {
    **dict.fromkeys('123', lambda n, unit, *_: unit * int(n)),
    **dict.fromkeys('45', lambda n, unit, half, *_: unit * (5 - int(n)) + half),
    **dict.fromkeys('678', lambda n, unit, half, *_: half + unit * (int(n) - 5)),
    '9': lambda _, unit, half, next: unit + next
}


def to_roman(n: int) -> str:
    return ''.join(
        _digit.get(v, lambda *_: '')(v, *units)
        for v, units in zip(
            f'{n:04d}',
            [['M', 'V̅', 'X̅'],
             ['C', 'D', 'M'],
             ['X', 'L', 'C'],
             ['I', 'V', 'X']]
        )
    )


pairs = list(zip(
    ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'],
    [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
))

roman_re = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')


def _parse_digit(total, digit, value, rest):
    return _parse_digit(total + value, digit, value, rest[len(digit):]) if rest.startswith(digit) else (total, rest)


def parse_roman(roman):
    if not roman or not roman_re.match(roman):
        return -1
    total = 0
    for r, a in pairs:
        total, roman = _parse_digit(total, r, a, roman)
    return total


if __name__ == '__main__':
    print(parse_roman('MMMCMXCIX'))
    print(parse_roman('MMMCMXCVIII'))
