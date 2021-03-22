find_missing = lambda seq, n: \
    _recur_miss(sorted(seq), 1)
_recur_miss = \
    lambda seq, count: \
        (lambda head, *tail: head - 1 if head - count == 1 else _recur_miss(tail, count + 1))(*seq)

find_duplicate = lambda seq, n: \
    _recur_dupe(sorted(seq), 1)
_recur_dupe = lambda seq, count: \
    (lambda head, *tail: head if head != count else _recur_dupe(tail, count + 1))(*seq)
