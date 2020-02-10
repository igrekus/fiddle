from itertools import chain, repeat


def high_places(place, times):
    yield from chain(*[[p] * times for p in place])


def prev_nums(place, times):
    yield from chain(*repeat(place, times))


def decimal_pairs(higher_places, lower_places):
    yield from zip(high_places(higher_places, len(lower_places)), prev_nums(lower_places, len(higher_places)))


def place_to_string(high_place, prev_nums):
    return [f'{high} {low}' for high, low in decimal_pairs(high_place, prev_nums)]


_10s = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
_100s = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
ones = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']

first_hundred = ones + teens + place_to_string(_10s, ones)
first_thousand = first_hundred + place_to_string(_100s, first_hundred)

d = {i: s.replace(' ноль', '') for i, s in zip(range(1000), first_thousand)}


def to_russian_string(value: int) -> str:
    if value not in range(1000):
        raise ValueError('Input value must be within [0..999]')
    return d[value]
