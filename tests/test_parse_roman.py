import ast
import pytest

from pyexpect import expect

from fiddle import parse_roman


with open('romans.txt', mode='rt', encoding='utf-8') as f:
    romans = ast.literal_eval(f.readlines()[0])


def test_1():
    expect(parse_roman('I')).to_equal(1)


def test_2():
    expect(parse_roman('II')).to_equal(2)


def test_3():
    expect(parse_roman('III')).to_equal(3)


@pytest.mark.parametrize('exp,act', [romans[idx] for idx in range(9)])
def test_ones(exp, act):
    expect(parse_roman(act)).to_equal(exp)
