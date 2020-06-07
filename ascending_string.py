from itertools import zip_longest

__all__ = ['ascending']


def ascending(value: str) -> bool:
    return any(_check(value, i) for i in range(1, len(value) // 2 + 1))


def _check(seq, n):
    try:
        return _recur(map(int, _group(seq, n)))
    except TypeError:
        return False


def _recur(seq):
    one, two, *rest = seq
    return two - one == 1 and _recur([two] + rest) if rest else two - one == 1


def _group(it, n):
    border = f'{"9" * n}1'
    return \
        _make_groups(_left(it, border), n) + \
        _make_groups(_right(it, border), n + 1) \
        if border in it \
        else _make_groups(it, n)


def _make_groups(it, n):
    return [''.join(el) for el in zip_longest(*([iter(it)] * n))]


def _left(it, border):
    return it[:_index(it, border)]


def _right(it, border):
    return it[_index(it, border):]


def _index(it, border):
    return it.index(border) + len(border) - 1
