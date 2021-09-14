from itertools import chain
from functools import reduce
from operator import xor

find_missing = find_duplicate = lambda seq, n: reduce(xor, chain(range(1, n + 1), seq))
