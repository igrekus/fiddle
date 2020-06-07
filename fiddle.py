from itertools import zip_longest

__all__ = ['ascending']


def _is_consequent(one, two):
    return one < two and two - one == 1


def _recur(seq):
    one, two, *rest = seq
    return _is_consequent(one, two) and _recur([two] + rest) if rest else _is_consequent(one, two)


def _group_by(it, n):
    return [''.join(el) for el in zip_longest(*([iter(it)] * n), fillvalue=None)]


def _index(it, border):
    return it.index(border) + len(border) - 1


def _group(it, n):
    border = f'8{"9" * n}1'
    return _group_by(it[:_index(it, border)], n) + _group_by(it[_index(it, border):], n + 1) if border in it else _group_by(it, n)


def _check(seq, n):
    try:
        return _recur(map(int, _group(seq, n)))
    except TypeError:
        return False


def ascending(value: str) -> bool:
    return any(_check(value, i) for i in range(1, len(value) // 2))
