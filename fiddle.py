from collections import namedtuple
from functools import partial

raw = [
    [1, 1, 3, 4, 7, 15],
    [1, 1, 3, 4, 7, 16],
    [1, 1, 3, 4, 7, 17],
    [1, 1, 3, 8, 9, 17],
    [1, 2, 2, 4, 8, 15],
    [1, 1, 3, 4],
]


Player = namedtuple('Player', ['id', 'size'])


def grow(player, foods):
    if len(foods) == 1:
        return player.size > foods[0].size
    else:
        head, *tail = foods
        new_player = Player(player.id, player.size + head.size if (player.size > head.size and player.id != head.id) else player.size)
        return grow(new_player, tail)


def can_win(ps):
    ps = [Player(*args) for args in enumerate(ps)]
    return [int(e) for e in [grow(p, ps) for p in ps]]


for r in raw:
    print(r, can_win(r))
