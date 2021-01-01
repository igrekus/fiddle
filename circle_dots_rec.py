count_dots = lambda radius: _loop(radius, -int(radius), int(radius))

_loop = \
    lambda r, i, t: \
        2 * int((r ** 2 - i ** 2) ** 0.5) + 1 + _loop(r, i + 1, t) if i <= t else 0
