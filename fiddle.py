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


def check_combination(hand):
    # tests =
    # '1000000'
    # '0100000'
    # '0010000'
    # '0001000'
    # '0000100'
    # '0000010'
    # '0000001'
    if is_full_house(hand):
        return 'Full House'
    if is_straight(hand):
        return 'Straight'
    if is_kind_5(hand):
        return 'Impossible'
    if is_kind_4(hand):
        return 'Four of a Kind'
    if is_kind_3(hand):
        return 'Three of a Kind'
    if is_two_pairs(hand):
        return 'Two Pair'
    if is_kind_2(hand):
        return 'Pair'
    else:
        return 'Nothing'


# cards = [i for i in range(1, 13)] * 4
