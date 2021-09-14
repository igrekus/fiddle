import random

from pyexpect import expect

from fiddle import find_missing, find_duplicate
# from search_in_number_list import find_missing
# from search_in_number_list_2 import find_duplicate


def test_find_missing_random():
    n = 100
    seq = list(range(1, n + 1))
    random.shuffle(seq)
    expected = seq.pop(random.randint(0, n))

    expect(find_missing(seq=seq, n=n)).to_equal(expected)


def test_find_missing_left_border():
    n = 100
    seq = list(range(1, n + 1))
    random.shuffle(seq)
    expected = seq.pop(seq.index(1))

    expect(find_missing(seq=seq, n=n)).to_equal(expected)


def test_find_missing_right_border():
    n = 100
    seq = list(range(1, n + 1))
    random.shuffle(seq)
    expected = seq.pop(seq.index(n))

    expect(find_missing(seq=seq, n=n)).to_equal(expected)


def test_find_duplicate_random():
    n = 100
    seq = list(range(1, n + 1))
    random.shuffle(seq)
    expected = random.choice(seq)
    seq.append(expected)

    expect(find_duplicate(seq=seq, n=n)).to_equal(expected)


def test_find_duplicate_left_border():
    n = 100
    seq = list(range(1, n + 1))
    random.shuffle(seq)
    expected = 1
    seq.append(expected)

    expect(find_duplicate(seq=seq, n=n)).to_equal(expected)


def test_find_duplicate_right_border():
    n = 100
    seq = list(range(1, n + 1))
    random.shuffle(seq)
    expected = n
    seq.append(expected)

    expect(find_duplicate(seq=seq, n=n)).to_equal(expected)
