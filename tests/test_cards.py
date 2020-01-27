from pyexpect import expect

from fiddle import is_kind_5, is_straight, is_kind_4, is_kind_3, is_kind_2, is_two_pairs, is_full_house


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


def test_is_full_house():
    expect(is_full_house([1, 1, 2, 2, 2])).to_equal(True)
    expect(is_full_house([1, 1, 1, 2, 2])).to_equal(True)
    expect(is_full_house([1, 1, 1, 1, 2])).to_equal(False)
    expect(is_full_house([1, 2, 3, 4, 5])).to_equal(False)
    expect(is_full_house([1, 1, 3, 2, 2])).to_equal(False)
    expect(is_full_house([1, 1, 1, 2, 3])).to_equal(False)
