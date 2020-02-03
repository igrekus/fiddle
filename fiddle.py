from functools import update_wrapper
from random import choice, choices
from string import ascii_lowercase, ascii_uppercase, digits

class chain:
    def __init__(self, function):
        self.function = function
        update_wrapper(self, function)
    def __ror__(self, other):
        return self.function(other)
    def __call__(self, *args, **kwargs):
        return chain(lambda x: self.function(x, *args, **kwargs))

@chain
def add_upper(it, should=False):
    for el in it: yield choice(ascii_uppercase) + el[1:] if should else el

@chain
def add_digit(it, should=False):
    for el in it: yield el[:-1] + choice(digits) if should else el

@chain
def base(it, k=8):
    for el in it: yield ''.join(choices(el, k=k))


def password(length: int, use_upper=False, use_digits=False) -> str:
    if length < 8:
        raise ValueError('Minimal password length is 8')
    return list([ascii_lowercase] | base(k=length) | add_upper(should=use_upper) | add_digit(should=use_digits))[0]
