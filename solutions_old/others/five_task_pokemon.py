from typing import List, Optional, Tuple
from math import ceil


def nearest_bus_stop(k: int, n: int) -> int:
    return min(coef * n % k for coef in (-1, 1))


def pack_pastry(a: int, b: int) -> Optional[Tuple[int]]:
    return None if (a + b) % 3 or 2 * a < b or 2 * b < a else ((2 * a - b) // 3, (2 * b - a) // 3)


def rotate_board(before: List[int]) -> List[int]:
    return (lambda lst: [len(lst) - idx for idx, val in sorted(enumerate(lst), key=lambda x: x[1])])(before)


def locate_number(n: int) -> Tuple[int, int]:
    _inv = lambda lst: lst[::-1]
    _get_sqrt = lambda x: ceil(x ** 0.5)
    _get_corner = lambda x: (lambda sqrt: (sqrt - 1) ** 2 + sqrt)(_get_sqrt(x))
    _nf = lambda f, k, arg: arg if k <= 0 else _nf(f, k - 1, f(arg))
    return (
        lambda x, sqrt, corn: _nf(_inv,
                                  int(not sqrt % 2) + int(x > corn),
                                  (sqrt, sqrt - abs(corn - x)))) \
        (n, _get_sqrt(n), _get_corner(n))


def find_winners(players: List[int]) -> List[int]:
    _is_winner = lambda val, lst: int(len(lst) == 0 or val > lst[0] and _is_winner(val + lst[0], lst[1:]))
    return (
        lambda lst: list(map(_is_winner,
                             lst,
                             map(lambda idx: sorted(lst[:idx] + lst[idx + 1:]), range(len(lst)))))) \
        (players)
