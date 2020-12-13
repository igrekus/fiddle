import ast
import pytest

from pyexpect import expect

from fiddle import to_roman

with open('romans.txt', mode='rt', encoding='utf-8') as f:
    romans = ast.literal_eval(f.readlines()[0])


@pytest.mark.parametrize('act,exp', [romans[idx] for idx in range(9)])
def test_ones(act, exp):
    expect(to_roman(act)).to_equal(exp)


@pytest.mark.parametrize('act,exp', [romans[idx - 1] for idx in [10, 20, 30, 40, 50, 60, 70, 80, 90]])
def test_tens(act, exp):
    expect(to_roman(act)).to_equal(exp)


@pytest.mark.parametrize('act,exp', [romans[idx - 1] for idx in [100, 200, 300, 400, 500, 600, 700, 800, 900]])
def test_hundreds(act, exp):
    expect(to_roman(act)).to_equal(exp)


@pytest.mark.parametrize('act,exp', [romans[idx - 1] for idx in [1000, 2000, 3000]])
def test_thousands(act, exp):
    expect(to_roman(act)).to_equal(exp)


def test_all():
    for act, exp in romans:
        expect(to_roman(act)).to_equal(exp)
