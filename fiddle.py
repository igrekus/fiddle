from functools import partial

raw = [1, 1, 3, 4, 7, 20]

grow = lambda player, foods: player > foods[0] if len(foods) == 1 else (
    lambda head, *tail: grow(player + head if player > head else player, tail))(*foods)
walk = lambda f, seq: (lambda head, *tail: [f(seq[-1])] if len(seq) == 1 else [f(head)] + walk(f, tail))(*seq)
can_win = lambda foods: walk(int, walk(partial(grow, foods=foods), foods))

print(can_win(raw))
