from functools import partial

raw = [
    [1, 1, 3, 4, 7, 15],
    [1, 1, 3, 4, 7, 16],
    [1, 1, 3, 4, 7, 17],
    [1, 1, 3, 8, 9, 17],
    [1, 2, 2, 4, 8, 15],
    [1, 1, 3, 4],
]

res = [
    [0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 1]
]

grow = lambda p, fs: p[1] > fs[0][1] if len(fs) == 1 else \
    (lambda head, *tail: grow((p[0], p[1] + head[1]) if p[1] > head[1] and p[0] != head[0] else p, tail))(*fs)


can_win = lambda pls: list((lambda ps: map(int, map(partial(grow, fs=ps), ps)))(list(enumerate(pls))))


for rw, rs in zip(raw, res):
    cw = can_win(rw)
    assert cw == rs, f'{cw} {rs}'
    print(rw, cw)
