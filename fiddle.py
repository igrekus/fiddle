from itertools import zip_longest

s1 = '0123456789'
s2 = '123567894'
s3 = '5152535455'
s4 = '100101102103104'
s5 = '1111111211131114111511161117111811191120'


def _is_consequent(one, two):
    return one < two and two - one == 1


def _recur(seq):
    print(seq)
    one, two, *rest = seq
    return _is_consequent(one, two) and _recur([two] + rest) if rest else _is_consequent(one, two)


def _group_by(it, n):
    return [''.join(el) for el in zip_longest(*([iter(it)] * n), fillvalue=None)]


def check(seq, n: int) -> bool:
    try:
        seq = _group_by(seq, n)
    except TypeError:
        return False
    return _recur(list(map(int, seq)))


print(check(s5, 4))
# print(list(group_by(s2, 2)))
