import string
from pyexpect import expect

from fiddle import password


def test_password_length_less_than_8():
    expect(lambda: password(7, False, False)).to_raise(ValueError, 'Minimal password length is 8')


def test_password_false_args():
    pw = password(10, False, False)
    pw_letters = set(pw)
    illegal_letters = set(string.ascii_uppercase + string.digits)
    expect(pw_letters.intersection(illegal_letters)).to_be_empty()
    expect(len(pw)).to_be(10)


def test_password_upper_true_digits_false():
    pw = password(10, True, False)
    pw_letters = set(pw)
    digits = set(string.digits)
    upper_letters = set(string.ascii_uppercase)
    lower_letters = set(string.ascii_lowercase)

    expect(pw_letters.intersection(digits)).to_be_empty()
    expect(pw_letters.intersection(upper_letters)).not_to_be_empty()
    expect(pw_letters.intersection(lower_letters)).not_to_be_empty()

    expect(len(pw)).to_be(10)


def test_password_upper_false_digits_true():
    pw = password(10, False, True)
    pw_letters = set(pw)
    digits = set(string.digits)
    upper_letters = set(string.ascii_uppercase)
    lower_letters = set(string.ascii_lowercase)

    expect(pw_letters.intersection(digits)).not_to_be_empty()
    expect(pw_letters.intersection(upper_letters)).to_be_empty()
    expect(pw_letters.intersection(lower_letters)).not_to_be_empty()

    expect(len(pw)).to_be(10)


def test_password_upper_true_digits_true():
    pw = password(10, True, True)
    pw_letters = set(pw)
    digits = set(string.digits)
    upper_letters = set(string.ascii_uppercase)
    lower_letters = set(string.ascii_lowercase)

    expect(pw_letters.intersection(digits)).not_to_be_empty()
    expect(pw_letters.intersection(upper_letters)).not_to_be_empty()
    expect(pw_letters.intersection(lower_letters)).not_to_be_empty()

    expect(len(pw)).to_be(10)

