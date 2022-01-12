from pyexpect import expect

# from solutions_old.flatten import flatten
from listoflists import flatten


def test_1():
    data = [1, ['a', 1], False, 0.0]
    expect(flatten(data)).to_equal([1, 'a', 1, False, 0.0])


def test_2():
    data = [[[[[[[[1, [[[False, 'lol', [2, 1], 3]]]]]]]]]], [], [], [], [], ['a', 1], False, 0.0]
    expect(flatten(data)).to_equal([1, False, 'lol', 2, 1, 3, 'a', 1, False, 0.0])


def test_3():
    data = [1, 2, 3, 4, 5, expect, [[[[[[[1, [[[False, 'lol', [2, 1], 3]]]]]]]]]], [], [], [], [], ['a', 1], False, 0.0]
    expect(flatten(data)).to_equal([1, 2, 3, 4, 5, expect, 1, False, 'lol', 2, 1, 3, 'a', 1, False, 0.0])


def test_4():
    data = [1, [2, 3], 4, 5, expect, [[[[[[[1, [[[False, 'lol', [2, 1], 3]]]]]]]]]]]
    expect(flatten(data)).to_equal([1, 2, 3, 4, 5, expect, 1, False, 'lol', 2, 1, 3])


def test_5():
    data = [1, [2, 3], 4, 5, expect, [[[[[[[1, [[[False, 'lol', [2, 1], 3]]]]]]]]]], 2]
    # expect(flatten(data)).to_equal([1, 2, 3, 4, 5, expect, 1, False, 'lol', 2, 1, 3, 2])
    assert flatten(data) == [1, 2, 3, 4, 5, expect, 1, False, 'lol', 2, 1, 3, 2]


# def test_find_missing_left_border():
#     n = 100
#     seq = list(range(1, n + 1))
#     random.shuffle(seq)
#     expected = seq.pop(seq.index(1))
#
#     expect(find_missing(seq=seq, n=n)).to_equal(expected)
#
#
# def test_find_missing_right_border():
#     n = 100
#     seq = list(range(1, n + 1))
#     random.shuffle(seq)
#     expected = seq.pop(seq.index(n))
#
#     expect(find_missing(seq=seq, n=n)).to_equal(expected)
#
#
# def test_find_duplicate_random():
#     n = 100
#     seq = list(range(1, n + 1))
#     random.shuffle(seq)
#     expected = random.choice(seq)
#     seq.append(expected)
#
#     expect(find_duplicate(seq=seq, n=n)).to_equal(expected)
#
#
# def test_find_duplicate_left_border():
#     n = 100
#     seq = list(range(1, n + 1))
#     random.shuffle(seq)
#     expected = 1
#     seq.append(expected)
#
#     expect(find_duplicate(seq=seq, n=n)).to_equal(expected)
#
#
# def test_find_duplicate_right_border():
#     n = 100
#     seq = list(range(1, n + 1))
#     random.shuffle(seq)
#     expected = n
#     seq.append(expected)
#
#     expect(find_duplicate(seq=seq, n=n)).to_equal(expected)
