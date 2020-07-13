import math
from itertools import count


def _make_sieve(n):
    out = [1, 1, 0] + [0, 1] * n
    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if out[i] == 0:
            for j in range(i ** 2, n + 1, i + i):
                out[j] = 1
    return out


def _is_prime(n):
    return sieve[n] == 0


def _is_left_right_trunc(n):
    div = 10
    while div < n:
        if not (_is_prime(n % div) and _is_prime(n // div)):
            return False
        div *= 10
    return True


sieve = _make_sieve(800_000)


def generate() -> list:
    out = []
    o_app = out.append
    ln = out.__len__

    for i in count(start=23, step=2):
        if _is_prime(i) and _is_left_right_trunc(i):
            o_app(i)
            if ln() == 11:
                return out
