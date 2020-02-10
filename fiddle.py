from itertools import chain, repeat

tens = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
_0_to_9 = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
_10_to_19 = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
_0_to_99 = _0_to_9 + _10_to_19 + [f'{ten} {one}' for ten, one in zip(chain(*[[ten] * 10 for ten in tens]), chain(*repeat(_0_to_9, 8)))]
_100_to_199 = [f'сто {s}' for s in _0_to_99]
_200_to_299 = [f'двести {s}' for s in _0_to_99]
_300_to_399 = [f'триста {s}' for s in _0_to_99]
_400_to_499 = [f'четыреста {s}' for s in _0_to_99]
_500_to_599 = [f'пятьсот {s}' for s in _0_to_99]
_600_to_699 = [f'шестьсот {s}' for s in _0_to_99]
_700_to_799 = [f'семьсот {s}' for s in _0_to_99]
_800_to_899 = [f'восемьсот {s}' for s in _0_to_99]
_900_to_999 = [f'девятьсот {s}' for s in _0_to_99]

d = {i: s.replace(' ноль', '') for i, s in zip(range(1000), chain(
    _0_to_99,
    _100_to_199,
    _200_to_299,
    _300_to_399,
    _400_to_499,
    _500_to_599,
    _600_to_699,
    _700_to_799,
    _800_to_899,
    _900_to_999,
))}


def to_russian_string(value: int) -> str:
    if value not in range(1000):
        raise ValueError('Input value must be within [0..999]')
    return d[value]

# print(list(chain(*repeat(_0_to_9, 8))))
# print(list(chain(*[[ten]*10 for ten in tens])))
print(_0_to_99)
