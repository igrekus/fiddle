from random import choice, choices
from string import ascii_lowercase, ascii_uppercase, digits


class Password:
    def __init__(self, length=8):
        self.password = ''.join(choices(ascii_lowercase, k=length))
        self.where = 0

    def using(self, what='', when=False):
        self.password = self.password[:self.where] + choice(what) + self.password[self.where + 1:] if when else self.password
        self.where += 1
        return self


def password(length: int, use_upper=False, use_digits=False) -> str:
    if length < 8:
        raise ValueError('Minimal password length is 8')
    return Password(length)\
        .using(what=ascii_uppercase, when=use_upper)\
        .using(what=digits, when=use_digits)\
        .password