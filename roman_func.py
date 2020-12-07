import re

_get = (
    lambda f, *args: lambda *a: f(*(a + args)))(
    {
        **dict.fromkeys('123', lambda n, unit, *_: unit * int(n)),
        **dict.fromkeys('45', lambda n, unit, half, *_: unit * (5 - int(n)) + half),
        **dict.fromkeys('678', lambda n, unit, half, *_: half + unit * (int(n) - 5)),
        '9': lambda _, unit, half, next: unit + next
    }.get,
    lambda *_: ''
)

to_roman = lambda n: \
    ''.join(
        _get(v)(v, *units)
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


_parse_digit = \
    lambda total, digit, value, rest: \
        _parse_digit(total + value, digit, value, rest[len(digit):]) if rest.startswith(digit) else (total, rest)

_recur = \
    lambda total, roman, ps: \
        (total, '') if len(ps) == 0 else _recur(*(lambda t, r: _parse_digit(t, *ps[0], r))(total, roman), ps[1:])


parse_roman = \
    lambda roman: \
        -1 if not roman or not roman_re.match(roman) else _recur(0, roman, pairs)[0]


if __name__ == '__main__':
    print(parse_roman('MMMCMXCIX'))
    print(parse_roman('MMMCMXCVIII'))
