from iteration_utilities import deepflatten
from fiddle import flatten
from pyexpect import expect


def test_1():
    test = [[1, 2], 3, [4, [5, [6]], 7]]
    expect(list(flatten(test))).to_equal(list(deepflatten(test)))


def test_2():
    test = [[1, 2], 3, [4, [5, [6]], 7]]
    expect(list(flatten(test, 1))).to_equal(list(deepflatten(test, 1)))


def test_3():
    test = [[1, 2], 3, [4, [5, [6]], 7]]
    expect(list(flatten(test, 2))).to_equal(list(deepflatten(test, 2)))


def test_4():
    test = [[1, 2], 3, [4, [5, [6]], 7]]
    expect(list(flatten(test, 3))).to_equal(list(deepflatten(test, 3)))


def test_5():
    test = [[1, 2], [[[[]]], 3], [[[4]], [5, [6]], 7]]
    expect(list(flatten(test))).to_equal(list(deepflatten(test)))

