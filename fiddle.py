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
