from itertools import repeat, chain
from functools import reduce
from operator import xor

find_missing, find_duplicate = repeat(lambda seq, n: reduce(xor, chain(range(1, n + 1), seq)), 2)
