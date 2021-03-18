import random

from pyexpect import expect

from find_num_lex_draven import find_missing, find_duplicate


def test_find_missing():
    n = 100
    seq = list(range(1, n + 1))
    random.shuffle(seq)
    expected = seq.pop(random.randint(1, n + 1))

    expect(find_missing(seq, n)).to_equal(expected)


def test_find_duplicate():
    n = 100
    seq = list(range(1, n + 1))
    random.shuffle(seq)
    expected = random.choice(seq)
    seq.append(expected)

    expect(find_duplicate(seq, n)).to_equal(expected)
