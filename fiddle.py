# Итак, новая задача для всех желающих попробовать свои силы, в этот раз попроще (Никита жаловался).
# Реализовать функцию, которая принимает на вход список из 5 целых положительных чисел и возвращает название комбинации в покере:
# + если одинаковы 5, то вернуть "Impossible", иначе
# + если есть 5 последовательных ([1,2,3,4,5]), то вернуть "Straight", иначе
# + если одинаковы 4, то вернуть "Four of a Kind", иначе
# + если одинаковы 2, то вернуть "One Pair", иначе
# - если одинаковы 2 и 2, то вернуть "Two Pairs", иначе
# - если одинаковы 3, то вернуть "Three of a Kind", иначе
# - если одинаковы 3 и 2 ([1,1,3,3,3]), то вернуть "Full House", иначе
# - вернуть "Nothing".
# сигнатура def check_combination(cards: list) -> str:
# нужно только дописать код в функции, не нужно ничего лишнего, импорт чего-либо запрещен (разве что рандом для проверки)
import itertools
import json
import random


def is_straight(seq):
    return len(set(seq)) == 5 and (max(seq) - min(seq)) == 4


def has_seq(seq, l):
    count = [n for n in set(seq) if seq.count(n) == l]
    return bool(count), len(count)


def is_kind(seq, length, times):
    tst, ln = has_seq(seq, length)
    return tst and ln == times


def is_kind_5(seq):
    return is_kind(seq, 5, 1)


def is_kind_4(seq):
    return is_kind(seq, 4, 1)


def is_kind_3(seq):
    return is_kind(seq, 3, 1)


def is_kind_2(seq):
    return is_kind(seq, 2, 1)


def is_two_pairs(seq):
    return is_kind(seq, 2, 2)


def is_full_house(seq):
    return is_kind_3(seq) and is_kind_2(seq)


labels = {
    69: 'Full House',
    32: 'Straight',
    16: 'Impossible',
    8: 'Four of a Kind',
    4: 'Three of a Kind',
    2: 'Two Pair',
    1: 'Pair'
}

test_funcs = [is_full_house, is_straight, is_kind_5, is_kind_4, is_kind_3, is_two_pairs, is_kind_2]


def check_combination(hand):
    # tests =
    # '0000101' 5
    return labels.get(int(''.join([str(int(f(hand))) for f in test_funcs]), 2), 'Nothing')

# cards = [i for i in range(1, 13)] * 4
