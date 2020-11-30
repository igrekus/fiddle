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


@pytest.mark.parametrize('exp,act', [romans[idx - 1] for idx in [10, 20, 30, 40, 50, 60, 70, 80, 90]])
def test_tens(exp, act):
    expect(parse_roman(act)).to_equal(exp)


@pytest.mark.parametrize('exp,act', [romans[idx - 1] for idx in [100, 200, 300, 400, 500, 600, 700, 800, 900]])
def test_hundreds(exp, act):
    expect(parse_roman(act)).to_equal(exp)


@pytest.mark.parametrize('exp,act', [romans[idx - 1] for idx in [1000, 2000, 3000]])
def test_thousands(exp, act):
    expect(parse_roman(act)).to_equal(exp)


def test_ones_errors():
    expect(parse_roman('IIX')).to_equal(-1)
    expect(parse_roman('IIV')).to_equal(-1)
    expect(parse_roman('IIII')).to_equal(-1)
    expect(parse_roman('O')).to_equal(-1)
    expect(parse_roman('VIIII')).to_equal(-1)

    expect(parse_roman('XXL')).to_equal(-1)
    expect(parse_roman('XXC')).to_equal(-1)
    expect(parse_roman('XXXX')).to_equal(-1)
    expect(parse_roman('LL')).to_equal(-1)
    expect(parse_roman('LXXXX')).to_equal(-1)

    expect(parse_roman('CCD')).to_equal(-1)
    expect(parse_roman('CCM')).to_equal(-1)
    expect(parse_roman('CCCC')).to_equal(-1)
    expect(parse_roman('DD')).to_equal(-1)
    expect(parse_roman('DCCCC')).to_equal(-1)

    expect(parse_roman('MMV̅')).to_equal(-1)
    expect(parse_roman('V̅V̅X̅')).to_equal(-1)
    expect(parse_roman('MMMM')).to_equal(-1)
    expect(parse_roman('V̅V̅')).to_equal(-1)
    expect(parse_roman('X̅MMM')).to_equal(-1)

    expect(parse_roman('')).to_equal(-1)
    expect(parse_roman('A')).to_equal(-1)
    expect(parse_roman('MMMA')).to_equal(-1)

