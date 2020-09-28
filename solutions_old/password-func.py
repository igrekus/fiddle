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


def add(st, what='', at=0, should=False):
    return st[:at] + choice(what) + st[at + 1:] if should else st


@chain
def with_chars(container, what, at=0, should=False):
    yield from (add(el, what, at, should) for el in container)


@chain
def base(it, k=8):
    yield from (''.join(choices(el, k=k)) for el in it)


def password(length: int, use_upper=False, use_digits=False) -> str:
    if length < 8:
        raise ValueError('Minimal password length is 8')
    return list(
        [ascii_lowercase]
        | base(k=length)
        | with_chars(ascii_uppercase, at=0, should=use_upper)
        | with_chars(digits, at=1, should=use_digits)
    )[0]
