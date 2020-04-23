from pyexpect import expect
from fiddle import Bottles

b = Bottles()


def test_first_verse():
    expected = '''99 бутылок пива на стене, 99 бутылок пива!
Возьми одну, передай мне, 98 бутылок пива на стене
'''
    expect(b.verse(99)).to_equal(expected)


def test_another_verse():
    expected = '''89 бутылок пива на стене, 89 бутылок пива!
Возьми одну, передай мне, 88 бутылок пива на стене
'''
    expect(b.verse(89)).to_equal(expected)


def test_verse_2():
    expected = '''2 бутылки пива на стене, 2 бутылки пива!
Возьми одну, передай мне, 1 бутылка пива на стене
'''
    expect(b.verse(2)).to_equal(expected)


def test_verse_1():
    expected = '''1 бутылка пива на стене, 1 бутылка пива!
Возьми одну, передай мне, нет бутылок пива на стене
'''
    expect(b.verse(1)).to_equal(expected)


def test_verse_0():
    expected = '''Нет бутылок пива на стене, нет бутылок пива!
Сходи в магазин, купи ещё, 99 бутылок пива на стене
'''
    expect(b.verse(0)).to_equal(expected)


def test_a_couple_verses():
    expected = '''99 бутылок пива на стене, 99 бутылок пива!
Возьми одну, передай мне, 98 бутылок пива на стене

98 бутылок пива на стене, 98 бутылок пива!
Возьми одну, передай мне, 97 бутылок пива на стене
'''
    expect(b.verses(99, 98)).to_equal(expected)


def test_a_few_verses():
    expected = '''2 бутылки пива на стене, 2 бутылки пива!
Возьми одну, передай мне, 1 бутылка пива на стене

1 бутылка пива на стене, 1 бутылка пива!
Возьми одну, передай мне, нет бутылок пива на стене

Нет бутылок пива на стене, нет бутылок пива!
Сходи в магазин, купи ещё, 99 бутылок пива на стене
'''
    expect(b.verses(2, 0)).to_equal(expected)


def test_the_whole_song():
    expect(b.verses(99, 0)).to_equal(b.song)
