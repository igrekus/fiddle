from functools import reduce

find_missing   = lambda seq, n: reduce(lambda acc, x: (acc[0] ^ acc[1] ^ x, acc[1] + 1), seq, (n, 1))[0]
find_duplicate = lambda seq, n: reduce(lambda acc, x: (acc[0] ^ acc[1] ^ x, acc[1] + 1), seq[1:], (seq[0], 1))[0]
