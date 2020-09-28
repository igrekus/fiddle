import math


def _make_sieve(n):
    out = [1, 1, 0] + [0, 1] * n
    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if out[i] == 0:
            for j in range(i ** 2, n + 1, i + i):
                out[j] = 1
    return out


def _is_prime(n):
    return sieve[n] == 0


def _is_left_trunc(p):
    div = 10
    while div < p:
        if not _is_prime(p % div):
            return False
        div *= 10
    return True


sieve = _make_sieve(800_000)


def generate():
    primes = [2, 3, 5, 7]
    digits = [1, 3, 7, 9]
    out = []

    while True:
        prime = primes.pop(0)
        for digit in digits:
            test = prime * 10 + digit
            if not _is_prime(test):
                continue
            primes.append(test)
            if not _is_left_trunc(test):
                continue
            out.append(test)
            if len(out) == 11:
                return out

