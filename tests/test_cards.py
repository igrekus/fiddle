import json

from pyexpect import expect

from fiddle import is_kind_5, is_straight, is_kind_4, is_kind_3, is_kind_2, is_two_pairs,  check_combination


def test_is_impossible():
    expect(is_kind_5([1, 1, 1, 1, 1])).to_equal(True)
    expect(is_kind_5([2, 1, 1, 1, 1])).to_equal(False)


def test_is_straight():
    expect(is_straight([1, 2, 3, 4, 5])).to_equal(True)
    expect(is_straight([5, 6, 7, 8, 9])).to_equal(True)
    expect(is_straight([5, 6, 1, 8, 9])).to_equal(False)


def test_is_kind_4():
    expect(is_kind_4([1, 1, 1, 1, 2])).to_equal(True)
    expect(is_kind_4([3, 3, 3, 3, 1])).to_equal(True)
    expect(is_kind_4([1, 1, 2, 1, 2])).to_equal(False)


def test_is_kind_3():
    expect(is_kind_3([1, 1, 1, 2, 2])).to_equal(True)
    expect(is_kind_3([3, 3, 3, 2, 1])).to_equal(True)
    expect(is_kind_3([1, 3, 2, 1, 2])).to_equal(False)


def test_is_one_pair():
    expect(is_kind_2([1, 2, 3, 4, 4])).to_equal(True)
    expect(is_kind_2([1, 2, 3, 3, 4])).to_equal(True)
    expect(is_kind_2([1, 1, 3, 4, 4])).to_equal(False)
    expect(is_kind_2([1, 5, 3, 4, 2])).to_equal(False)


def test_is_two_pairs():
    expect(is_two_pairs([1, 2, 3, 4, 5])).to_equal(False)
    expect(is_two_pairs([1, 2, 3, 4, 4])).to_equal(False)
    expect(is_two_pairs([1, 2, 2, 4, 4])).to_equal(True)
    expect(is_two_pairs([2, 2, 2, 4, 4])).to_equal(False)
    expect(is_two_pairs([1, 1, 2, 4, 4])).to_equal(True)


def test_check_combination():
    expect(check_combination([1, 2, 3, 4, 5])).to_equal('Straight')
    expect(check_combination([1, 1, 1, 1, 1])).to_equal('Impossible')
    expect(check_combination([1, 1, 1, 1, 2])).to_equal('Four of a Kind')
    expect(check_combination([1, 1, 2, 2, 2])).to_equal('Full House')
    expect(check_combination([2, 2, 1, 1, 1])).to_equal('Full House')
    expect(check_combination([2, 3, 1, 1, 1])).to_equal('Three of a Kind')
    expect(check_combination([2, 2, 3, 1, 1])).to_equal('Two Pair')
    expect(check_combination([2, 2, 3, 4, 1])).to_equal('Pair')
    expect(check_combination([2, 5, 3, 7, 1])).to_equal('Nothing')

    with open('D:\\work\\python\\fiddle\\dataset.json', mode='rt', encoding='utf-8') as f:
        js = json.loads(''.join(f.readlines()))

    for k, v in js.items():
        ns = [int(s) for s in k.split(' ')]
        expect(check_combination(ns)).to_equal(v)
