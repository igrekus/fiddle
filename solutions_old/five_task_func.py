import math

from functools import partial


nearest_bus_stop = lambda k, n: min(abs(k * (n // k) - n), abs(k * (n // k) - n + k))


pack_pastry = lambda a, b:\
    (a // 3, b // 3) if a - b == 0 else \
        None if abs(a - b) != 1 else \
            (lambda com: (com + int(a - b > 0), com + int(a - b < 0)))(max(a // 3, b // 3))


rotate_board = lambda before: \
    [row.index(1) + 1 for row in list(zip(*reversed([[int(i == (v - 1)) for i in range(len(before))] for v in before])))]


locate_number = lambda x: \
    (lambda side:
     (lambda dir, start:
      ((x - start + 1, side) if dir else (side, x - start + 1))
      if x <= start + (side ** 2 - start + 1) // 2 else
      ((side, start + 2 * side - x - 1) if dir else (start + 2 * side - x - 1, side)))
     (side % 2 == 0, (side - 1) ** 2 + 1))(math.ceil(math.sqrt(x)))


find_winners = lambda players: list((lambda ps: map(int, map(partial((lambda f: f(f))(
    lambda h: lambda p, fs: p[1] > fs[0][1] if len(fs) == 1 else (
        lambda head, *tail: (lambda f: f(f))(h)((p[0], p[1] + head[1]) if p[1] > head[1] and p[0] != head[0] else p,
                                                tail))(*fs)), fs=ps), ps)))(list(enumerate(players))))
