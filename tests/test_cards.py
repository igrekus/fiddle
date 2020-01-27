import json

from pyexpect import expect

from fiddle import is_straight, check_combination


def test_is_straight():
    expect(is_straight([1, 2, 3, 4, 5])).to_equal(True)
    expect(is_straight([5, 6, 7, 8, 9])).to_equal(True)
    expect(is_straight([5, 6, 1, 8, 9])).to_equal(False)


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
