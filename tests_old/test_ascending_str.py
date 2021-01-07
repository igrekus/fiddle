from pyexpect import expect
from ascending_string import ascending


def test_ones():
    expect(ascending('123456789')).to_equal(True)
    expect(ascending('12345679')).to_equal(False)
    expect(ascending('1234567810')).to_equal(False)


def test_ones_to_tens():
    expect(ascending('12345678910')).to_equal(True)
    expect(ascending('91011')).to_equal(True)
    expect(ascending('910')).to_equal(True)
    expect(ascending('78911')).to_equal(False)
    expect(ascending('911')).to_equal(False)


def test_tens():
    expect(ascending('101112131415')).to_equal(True)
    expect(ascending('192021')).to_equal(True)
    expect(ascending('979899')).to_equal(True)
    expect(ascending('9998')).to_equal(False)
    expect(ascending('98999')).to_equal(False)


def test_tens_to_hundreds():
    expect(ascending('979899100')).to_equal(True)
    expect(ascending('99100')).to_equal(True)
    expect(ascending('99100101')).to_equal(True)
    expect(ascending('99101')).to_equal(False)
    expect(ascending('98101')).to_equal(False)
