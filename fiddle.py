def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc


def has_seq(seq, l):
    count = [n for n in set(seq) if seq.count(n) == l]
    return bool(count), len(count)


def is_kind(seq, length, times=1):
    tst, ln = has_seq(seq, length)
    return tst and ln == times


def is_straight(seq):
    return len(set(seq)) == 5 and (max(seq) - min(seq)) == 4


labels = {
    32: 'Straight',
    16: 'Impossible',
    8: 'Four of a Kind',
    4: 'Three of a Kind',
    5: 'Full House',
    2: 'Two Pairs',
    1: 'One Pair'
}

test_funcs = [
    is_straight,
    partial(is_kind, length=5),
    partial(is_kind, length=4),
    partial(is_kind, length=3),
    partial(is_kind, length=2, times=2),
    partial(is_kind, length=2)
]


def check_combination(hand):
    return labels.get(int(''.join([str(int(f(hand))) for f in test_funcs]), 2), 'Nothing')
