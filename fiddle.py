from functools import partial, reduce
from itertools import chain


def diamond(letter: str, background: str=' '):
    ls = ''.join(map(chr, range(ord('A'), ord(letter) + 1)))

    _id = lambda x: x
    _compose = lambda *funcs: reduce(lambda f, g: lambda *args: f(g(*args)), funcs, _id)
    _apply_many = lambda fs, *args: (f(*args) for f in fs)
    _mirror = lambda seq: seq[-2::-1]
    _flatten = lambda args: chain(*args)
    _quarter = lambda i, l: ''.join((background * (len(ls) - i - 1), l, background * i))
    _line_parts = partial(_apply_many, (_quarter, _compose(_mirror, _quarter)))
    _make_halfs = partial(_apply_many, (_id, _mirror))
    _make_line = _compose(partial(str.join, ''), _line_parts)
    _make_pic = _compose(partial(str.join, '\n'), _flatten)

    return _make_pic(_make_halfs([_make_line(i, l) for i, l in enumerate(ls)])) + '\n'
