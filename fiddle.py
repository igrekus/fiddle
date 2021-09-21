# def find_missing(seq, n):
#     missing = 0
#     for i in range(1, n + 1):
#         missing ^= i
#
#     for i in seq:
#         missing ^= i
#     return missing


# find_missing, find_duplicate = \
#     (lambda it, fn, op:
#         it.repeat(lambda seq, n: fn.reduce(op.xor, it.chain(range(1, n + 1), seq)), 2)) \
#             (__import__('itertools'), __import__('functools'), __import__('operator'))


find_missing = lambda seq, n: \
    _recur_miss(sorted(seq), 1)
_recur_miss = \
    lambda seq, count: \
        (lambda head, *tail: head - 1 if head - count == 1 else _recur_miss(tail, count + 1))(*seq)

find_duplicate = lambda seq, n: \
    _recur_dupe(sorted(seq), 1)
_recur_dupe = lambda seq, count: \
    (lambda head, *tail: head if head != count else _recur_dupe(tail, count + 1))(*seq)


_enum = lambda idx, seq: (lambda head, *tail: ([(head, idx)] + _enum(idx + 1, tail)))(*seq) if len(seq) > 1 else [(*seq, idx)]
_zip = lambda s1, s2: (lambda h1, *t1: (lambda h2, *t2: ([(h1, h2)] + _zip(t1, t2)) if t1 else [(h1, h2)]))(*s1)(*s2)
solve = lambda a, b: \
    list(_zip(
        (lambda f: f(f))(lambda h: lambda n: () if n < 1 else (lambda f: f(f))(h)(n - 1) + (n - 1,))(len(a)),
        (lambda d: map(d.get, a))(dict(_enum(0, b)))
    ))

print(solve(
    [15, 12, 13, 19, 14, 10, 16, 20, 9, 18, 8, 7],
    [19, 14, 8, 16, 20, 9, 18, 15, 12, 13, 7, 10]
))   # => [(0, 7), (1, 8), (2, 9), (3, 0), (4, 1), (5, 11), (6, 3), (7, 4), (8, 5), (9, 6), (10, 2), (11, 10)]
