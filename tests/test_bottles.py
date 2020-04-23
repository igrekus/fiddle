from pyexpect import expect
from fiddle import Bottles


def test_the_first_verse():
    b = Bottles()
    expect(b.verse(99)).to_equal('''99 бутылок пива на стене
99 бутылок пива!
Возьми одну, передай мне
98 бутылок пива на стене
''')
