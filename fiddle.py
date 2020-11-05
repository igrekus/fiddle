# # 5, cells
# from functools import partial
#
# raw = [
#     [1, 1, 3, 4, 7, 15],
#     [1, 1, 3, 4, 7, 16],
#     [1, 1, 3, 4, 7, 17],
#     [1, 1, 3, 8, 9, 17],
#     [1, 2, 2, 4, 8, 15],
#     [1, 1, 3, 4],
# ]
#
# res = [
#     [0, 0, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 1, 1, 1],
#     [0, 1, 1, 1, 1, 1]
# ]
#
# grow = lambda p, fs: p[1] > fs[0][1] if len(fs) == 1 else \
#     (lambda head, *tail: grow((p[0], p[1] + head[1]) if p[1] > head[1] and p[0] != head[0] else p, tail))(*fs)
#
# can_win = lambda pls: list((lambda ps: map(int, map(partial(grow, fs=ps), ps)))(list(enumerate(pls))))
#
#
# for rw, rs in zip(raw, res):
#     cw = can_win(rw)
#     assert cw == rs, f'{cw} {rs}'
#     print(rw, cw)

# # 1, sveta
# k = 600
# n = 2000
# from itertools import count
# sveta = lambda k, n: next(min(k * i - n, abs(k * i - k - n)) for i in count() if k * i > n)
# print(sveta(k, n))

# # 2. pirogi
# a = 4
# b = 5
# pack = lambda a, b:\
#     -1 if abs(a - b) != 1 else (lambda com: (com + 1, com) if a - b > 0 else (com, com + 1))(max(a // 3, b // 3))
# print(pack(a, b))

# # 3. chess
# n = 5
# raw = [4, 2, 3, 5, 1]
# res = [1, 4, 3, 5, 2]
# result = lambda r: [row.index(1) + 1 for row in list(zip(*[[int(i == (v - 1)) for i in range(n)] for v in r][::-1]))]
# print(result(raw))

import math


def num_coords(x):
    n_square = math.ceil(math.sqrt(x))
    direction = n_square % 2 == 0   # True - down-left, False - right-up
    starting_n = (n_square - 1) ** 2 + 1

    row = 0
    col = 0

    # first = lambda
    # row, col = \
    #     [(idx + 1, n_square) if direction else (n_square, idx + 1) for idx, v in enumerate(range(starting_n, starting_n + n_square)) if v == x]

    for idx, v in enumerate(range(starting_n, starting_n + n_square)):
        if v == x:
            row, col = (idx + 1, n_square) if direction else (n_square, idx + 1)

    for idx, v in enumerate(range(starting_n + n_square, n_square ** 2 + 1)):
        if v == x:
            row, col = (n_square, n_square - idx - 1) if direction else (n_square - idx - 1, n_square)

    # if direction:
    #     for idx, v in enumerate(range(starting_n, starting_n + n_square)):
    #         if v == x:
    #             row = idx + 1
    #             col = n_square
    #             break
    #     else:
    #         for idx, v in enumerate(range(starting_n + n_square - 1, n_square ** 2 + 1)):
    #             if v == x:
    #                 row = n_square
    #                 col = n_square - idx
    # else:
    #     for idx, v in enumerate(range(starting_n, starting_n + n_square)):
    #         if v == x:
    #             col = idx + 1
    #             row = n_square
    #             break
    #     else:
    #         for idx, v in enumerate(range(starting_n + n_square - 1, n_square ** 2 + 1)):
    #             if v == x:
    #                 col = n_square
    #                 row = n_square - idx

    return row, col


coords = [(i, num_coords(i)) for i in range(37)]
res = [(0, (0, 0)), (1, (1, 1)), (2, (1, 2)), (3, (2, 2)), (4, (2, 1)), (5, (3, 1)), (6, (3, 2)), (7, (3, 3)), (8, (2, 3)), (9, (1, 3)), (10, (1, 4)), (11, (2, 4)), (12, (3, 4)), (13, (4, 4)), (14, (4, 3)), (15, (4, 2)), (16, (4, 1)), (17, (5, 1)), (18, (5, 2)), (19, (5, 3)), (20, (5, 4)), (21, (5, 5)), (22, (4, 5)), (23, (3, 5)), (24, (2, 5)), (25, (1, 5)), (26, (1, 6)), (27, (2, 6)), (28, (3, 6)), (29, (4, 6)), (30, (5, 6)), (31, (6, 6)), (32, (6, 5)), (33, (6, 4)), (34, (6, 3)), (35, (6, 2)), (36, (6, 1))]

print(coords)
assert coords == res, 'should be equal'

