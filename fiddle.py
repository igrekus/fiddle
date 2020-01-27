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

import random


def has_set_of_len(seq, n):
    return len(set(seq)) == 5 - n + 1


def is_impossible(seq):
    return len(set(seq)) == 1


def is_straight(seq):
    return len(seq) == 5 and (max(seq) - min(seq)) == 4


def is_kind_4(seq):
    nums = set(seq)
    count = [n for n in nums if seq.count(n) == 4]
    return bool(count)


def is_kind_3(seq):
    nums = set(seq)
    count = [n for n in nums if seq.count(n) == 3]
    return bool(count)


def has_one_pair(seq):
    nums = set(seq)
    count = [n for n in nums if seq.count(n) == 2]
    return bool(count) and len(count) == 1


def has_two_pairs(seq):
    nums = set(seq)
    count = [n for n in nums if seq.count(n) == 2]
    return bool(count) and len(count) == 2


def is_fullhouse(seq):
    return has_set_of_len(seq, 2) and has_set_of_len(seq, 3)


def check_combination(hand):
    print(hand)
    print('same', is_impossible(hand))
    print('straight', is_straight(hand))
    print('4 kind', is_kind_4(hand))
    print('one pair', has_one_pair(hand))
    print('two pairs', has_two_pairs(hand))
    print('kind 3', is_kind_3(hand))
    print('fullhouse', is_kind_3(hand) and has_one_pair(hand))


cards = [i for i in range(14)] * 4
hand = random.sample(cards, 5)

# check_combination(hand)
check_combination([2, 4, 4, 2, 2])
# check_combination([2, 3, 4, 5, 6])
