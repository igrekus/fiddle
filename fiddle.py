import itertools
import json


def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc


def has_seq_of(seq, length, times=1):
    count = [n for n in set(seq) if seq.count(n) == length]
    return bool(count) and len(count) == times


def check_combination(hand):
    return {
        32: 'Straight',
        16: 'Impossible',
        8: 'Four of a Kind',
        4: 'Three of a Kind',
        5: 'Full House',
        2: 'Two Pairs',
        1: 'One Pair'
    }.get(int(''.join([str(int(f(hand))) for f in [
        lambda seq: partial(has_seq_of, length=1, times=5)(seq) and (max(seq) - min(seq)) == 4,
        partial(has_seq_of, length=5),
        partial(has_seq_of, length=4),
        partial(has_seq_of, length=3),
        partial(has_seq_of, length=2, times=2),
        partial(has_seq_of, length=2)
    ]]), 2), 'Nothing')


perms = list(itertools.permutations([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5], 5))

out = dict()
for p in perms:
    out[f"{p[0]} {p[1]} {p[2]} {p[3]} {p[4]}"] = check_combination(p)

with open('perms.json', mode='wt', encoding='utf-8') as f:
    f.write(json.dumps(out))
