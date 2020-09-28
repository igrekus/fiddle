"""
Fizz Buzz, DRY taken too far edition
"""

from functools import partial


def map_fb(fz, bz, n):
    test = lambda d, s, f: (lambda *args: s + f('')) if n % d == 0 else f
    fizz, buzz = [partial(test, a, b) for a, b in zip([fz, bz], ['Fizz', 'Buzz'])]
    return fizz(buzz(str))(n)


def fizz_buzz(fizz=3, buzz=5, seq=None):
    return '\n'.join(map(partial(map_fb, fizz, buzz), seq if seq else range(1, 16)))


if __name__ == '__main__':
    print(fizz_buzz(3, 5, range(1, 31)))
