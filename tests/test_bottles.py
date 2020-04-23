from pyexpect import expect
from fiddle import Bottles


def test_first_verse():
    b = Bottles()
    verse = 99
    expected = '''99 бутылок пива на стене
99 бутылок пива!
Возьми одну, передай мне
98 бутылок пива на стене
'''
    expect(b.verse(verse)).to_equal(expected)


def test_another_verse():
    b = Bottles()
    verse = 89
    expected = '''89 бутылок пива на стене
89 бутылок пива!
Возьми одну, передай мне
88 бутылок пива на стене
'''
    expect(b.verse(verse)).to_equal(expected)


def test_verse_2():
    b = Bottles()
    verse = 2
    expected = '''2 бутылки пива на стене
2 бутылки пива!
Возьми одну, передай мне
1 бутылка пива на стене
'''
    expect(b.verse(verse)).to_equal(expected)


def test_verse_1():
    b = Bottles()
    verse = 1
    expected = '''1 бутылка пива на стене
1 бутылка пива!
Возьми одну, передай мне
Нет бутылок пива на стене
'''
    expect(b.verse(verse)).to_equal(expected)


def test_verse_0():
    b = Bottles()
    verse = 0
    expected = '''Нет бутылок пива на стене
Нет бутылок пива!
Сходи в магазин, купи ещё
99 бутылок пива на стене
'''
    expect(b.verse(verse)).to_equal(expected)
