import itertools

from pyexpect import expect
from fiddle import to_russian_string


_0_to_9 = [
    'ноль',
    'один',
    'два',
    'три',
    'четыре',
    'пять',
    'шесть',
    'семь',
    'восемь',
    'девять',
]

_10_to_19 = [
    'десять',
    'одиннадцать',
    'двенадцать',
    'тринадцать',
    'четырнадцать',
    'пятнадцать',
    'шестнадцать',
    'семнадцать',
    'восемнадцать',
    'девятнадцать',
]


_20_to_29 = ['двадцать'] + [f'двадцать {s}' for s in _0_to_9[1:]]
_30_to_39 = ['тридцать'] + [f'тридцать {s1}' for s1 in _0_to_9[1:]]
_40_to_49 = ['сорок'] + [f'сорок {s}' for s in _0_to_9[1:]]
_50_to_59 = ['пятьдесят'] + [f'пятьдесят {s}' for s in _0_to_9[1:]]
_60_to_69 = ['шестьдесят'] + [f'шестьдесят {s}' for s in _0_to_9[1:]]
_70_to_79 = ['семьдесят'] + [f'семьдесят {s}' for s in _0_to_9[1:]]
_80_to_89 = ['восемьдесят'] + [f'восемьдесят {s}' for s in _0_to_9[1:]]
_90_to_99 = ['девяносто'] + [f'девяносто {s}' for s in _0_to_9[1:]]
_99s_chain = list(itertools.chain(_0_to_9[1:], _10_to_19, _20_to_29, _30_to_39, _40_to_49, _50_to_59, _60_to_69, _70_to_79, _80_to_89, _90_to_99))
_100_to_199 = ['сто'] + [f'сто {s}' for s in _99s_chain]
_200_to_299 = ['двести'] + [f'двести {s}' for s in _99s_chain]
_300_to_399 = ['триста'] + [f'триста {s}' for s in _99s_chain]
_400_to_499 = ['четыреста'] + [f'четыреста {s}' for s in _99s_chain]
_500_to_599 = ['пятьсот'] + [f'пятьсот {s}' for s in _99s_chain]
_600_to_699 = ['шестьсот'] + [f'шестьсот {s}' for s in _99s_chain]
_700_to_799 = ['семьсот'] + [f'семьсот {s}' for s in _99s_chain]
_800_to_899 = ['восемьсот'] + [f'восемьсот {s}' for s in _99s_chain]
_900_to_999 = ['девятьсот'] + [f'девятьсот {s}' for s in _99s_chain]

d = {i: s for i, s in zip(range(1000), itertools.chain(
    [_0_to_9[0]],
    _99s_chain,
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


def test_input_value_not_in_range():
    expect(lambda: to_russian_string(-1)).to_raise(ValueError)
    expect(lambda: to_russian_string(1000)).to_raise(ValueError)

    print(_20_to_29)


def test_to_ru_string():
    for i in range(1000):
        expect(to_russian_string(i)).to_equal(d[i])

