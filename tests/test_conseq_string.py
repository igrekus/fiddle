from pyexpect import expect
from fiddle import ascending


def test_1s():
    consec1 = '0123456789'
    consec2 = '45678'
    non_consec1 = '123567894'
    non_consec2 = '45289'

    expect(ascending(consec1)).to_be(True)
    expect(ascending(consec2)).to_be(True)

    expect(ascending(non_consec1)).to_be(False)
    expect(ascending(non_consec2)).to_be(False)


def test_10s():
    consec1 = '1011121314151617181920212223242526'
    consec2 = '5152535455'
    non_consec1 = '22232420'
    non_consec2 = '9998'

    expect(ascending(consec1)).to_be(True)
    expect(ascending(consec2)).to_be(True)
    expect(ascending(non_consec1)).to_be(False)
    expect(ascending(non_consec2)).to_be(False)


def test_100s():
    consec1 = '100101102103104'
    consec2 = '555556557558559560561'
    non_consec1 = '111112113114115119'
    non_consec2 = '111112113114110'

    expect(ascending(consec1)).to_be(True)
    expect(ascending(consec2)).to_be(True)
    expect(ascending(non_consec1)).to_be(False)
    expect(ascending(non_consec2)).to_be(False)


def test_1000s():
    consec1 = '1111111211131114111511161117111811191120'
    consec2 = '9990999199929993999499959996999799989999'
    non_consec1 = '23452346234912340'
    non_consec2 = '123412351230'

    expect(ascending(consec1)).to_be(True)
    expect(ascending(consec2)).to_be(True)
    expect(ascending(non_consec1)).to_be(False)
    expect(ascending(non_consec2)).to_be(False)


def test_10000s():
    consec1 = '111111111211113111141111511116'
    consec2 = '555555555655557555585555955560'
    non_consec1 = '55555555565555755559'
    non_consec2 = '555555555655552'

    expect(ascending(consec1)).to_be(True)
    expect(ascending(consec2)).to_be(True)
    expect(ascending(non_consec1)).to_be(False)
    expect(ascending(non_consec2)).to_be(False)


def test_1s_border():
    consec1 = '45678910111213'
    non_consec1 = '6789101113'

    expect(ascending(consec1)).to_be(True)
    expect(ascending(non_consec1)).to_be(False)


def test_10s_border():
    consec1 = '979899100101102103104'
    non_consec1 = '97989910099'

    expect(ascending(consec1)).to_be(True)
    expect(ascending(non_consec1)).to_be(False)


def test_100s_border():
    consec1 = '99799899910001001100210031004'
    non_consec1 = '99799810001001'

    expect(ascending(consec1)).to_be(True)
    expect(ascending(non_consec1)).to_be(False)


def test_1000s_border():
    consec1 = '999899991000010001'
    non_consec1 = '9998999910000999'

    expect(ascending(consec1)).to_be(True)
    expect(ascending(non_consec1)).to_be(False)


def test_close_border():
    expect(ascending('910')).to_be(True)

    expect(ascending('991')).to_be(False)
    expect(ascending('9910')).to_be(False)
    expect(ascending('99100')).to_be(True)

    expect(ascending('991000')).to_be(False)
    expect(ascending('9991000')).to_be(True)
    expect(ascending('999100')).to_be(False)
