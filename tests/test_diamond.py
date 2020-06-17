from pyexpect import expect
from fiddle import diamond


def test_diamond_to_A():
    expected = 'A'
    expect(diamond('A')).to_equal(expected)


def test_diamond_to_B():
    expected = ' A \n' \
               'B B\n' \
               ' A \n'
    expect(diamond('B')).to_equal(expected)


def test_diamond_to_C():
    expected = '  A  \n' \
               ' B B \n' \
               'C   C\n' \
               ' B B \n' \
               '  A  \n'
    expect(diamond('C')).to_equal(expected)


def test_diamond_to_D():
    expected = '   A   \n' \
               '  B B  \n' \
               ' C   C \n' \
               'D     D\n' \
               ' C   C \n' \
               '  B B  \n' \
               '   A   \n'
    expect(diamond('D')).to_equal(expected)
