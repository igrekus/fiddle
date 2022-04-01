from pyexpect import expect

from solutions_old.flatten import flatten
from helper import some_assert


def test_1():
    data = [1, ['a', 1], False, 0.0, 2]
    expect(flatten(data)).to_equal([1, 'a', 1, False, 0.0])


def test_2():
    some_assert()
