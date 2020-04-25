from pyexpect import expect
from bottles_oop import verses
# from bottles_func import verses


def test_verse_99():
    expected = '''99 бутылок пива на стене, 99 бутылок пива!
Возьми одну, передай мне, 98 бутылок пива на стене.'''
    expect(verses(99, 99)).to_equal(expected)


def test_verse_89():
    expected = '''89 бутылок пива на стене, 89 бутылок пива!
Возьми одну, передай мне, 88 бутылок пива на стене.'''
    expect(verses(89, 89)).to_equal(expected)


def test_verse_2():
    expected = '''2 бутылки пива на стене, 2 бутылки пива!
Возьми одну, передай мне, последняя бутылка пива на стене.'''
    expect(verses(2, 2)).to_equal(expected)


def test_verse_1():
    expected = '''Последняя бутылка пива на стене, последняя бутылка пива!
Возьми её, передай мне, нет бутылок пива на стене.'''
    expect(verses(1, 1)).to_equal(expected)


def test_verse_0():
    expected = '''Нет бутылок пива на стене, нет бутылок пива!
Сходи в магазин, купи ещё, 99 бутылок пива на стене.'''
    expect(verses(0, 0)).to_equal(expected)


def test_two_verses():
    expected = '''99 бутылок пива на стене, 99 бутылок пива!
Возьми одну, передай мне, 98 бутылок пива на стене.

98 бутылок пива на стене, 98 бутылок пива!
Возьми одну, передай мне, 97 бутылок пива на стене.'''
    expect(verses(99, 98)).to_equal(expected)


def test_three_verses():
    expected = '''2 бутылки пива на стене, 2 бутылки пива!
Возьми одну, передай мне, последняя бутылка пива на стене.

Последняя бутылка пива на стене, последняя бутылка пива!
Возьми её, передай мне, нет бутылок пива на стене.

Нет бутылок пива на стене, нет бутылок пива!
Сходи в магазин, купи ещё, 99 бутылок пива на стене.'''
    expect(verses(2, 0)).to_equal(expected)
