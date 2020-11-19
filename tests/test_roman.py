import ast
import pytest

from pyexpect import expect

from fiddle import to_roman

with open('romans.txt', mode='rt', encoding='utf-8') as f:
    romans = ast.literal_eval(f.readlines()[0])


def test_1():
    expect(to_roman(1)).to_equal('I')


def test_2():
    expect(to_roman(2)).to_equal('II')


def test_3():
    expect(to_roman(3)).to_equal('III')


@pytest.mark.parametrize("test_input,expected", romans[4:20] + romans[89:100])
def test_several(test_input, expected):
    expect(to_roman(test_input)).to_equal(expected)


@pytest.mark.parametrize('act,exp', [romans[idx - 1] for idx in [10, 20, 30, 40, 50, 60, 70, 80, 90]])
def test_tens(act, exp):
    expect(to_roman(act)).to_equal(exp)
