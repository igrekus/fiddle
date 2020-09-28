from itertools import chain, repeat


def gen_nums(high_place, prev_nums):
    return [f'{high} {low}' for high, low in decimal_pairs(high_place, prev_nums)]


def decimal_pairs(places, prev_nums):
    yield from zip(repeat_place(places, len(prev_nums)), repeat_nums(prev_nums, len(places)))


def repeat_place(place, times):
    yield from chain(*[[p] * times for p in place])


def repeat_nums(nums, times):
    yield from chain(*repeat(nums, times))


ones = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
_10s = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
_100s = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

first_hundred = ones + teens + gen_nums(_10s, ones)
first_thousand = [s.replace(' ноль', '') for s in first_hundred + gen_nums(_100s, first_hundred)]


def to_russian_string(value: int) -> str:
    if value not in range(1000):
        raise ValueError('Input value must be within [0..999]')
    return first_thousand[value]
