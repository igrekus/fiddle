s1 = '0123456789'
s2 = '0123567894'


def _is_consequent(one, two):
    return one < two and two - one == 1


def _recur(seq):
    one, two, *rest = seq
    return _is_consequent(one, two) and _recur([two] + rest) if rest else _is_consequent(one, two)


def check(seq, n: int) -> bool:
    return _recur(map(int, seq))


print(check(s1, 1))
