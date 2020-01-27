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


def is_one_pair(seq):
    nums = set(seq)
    count = [n for n in nums if seq.count(n) == 2]
    return bool(count) and len(count) == 1


def is_two_pairs(seq):
    nums = set(seq)
    count = [n for n in nums if seq.count(n) == 2]
    return bool(count) and len(count) == 2


def is_fullhouse(seq):
    return is_kind_3(seq) and is_one_pair(hand)


def check_combination(hand):
    # tests =
    # '1000000'
    # '0100000'
    # '0010000'
    # '0001000'
    # '0000100'
    # '0000010'
    # '0000001'
    if is_impossible(hand):
        return 'Impossible'
    elif is_straight(hand):
        return 'Straight'
    elif is_kind_4(hand):
        return 'Four of a Kind'
    elif is_fullhouse(hand):
        return 'Full House'
    elif is_kind_3(hand):
        return 'Three of a Kind'
    elif is_two_pairs(hand):
        return 'Two Pairs'
    elif is_one_pair(hand):
        return 'One Pair'
    else:
        return 'Nothing'


cards = [i for i in range(1, 15)] * 4

# hand = [2, 4, 4, 5, 5]

for _ in range(10):
    hand = random.sample(cards, 5)
    print(list(sorted(hand)))
    print(check_combination(hand))
