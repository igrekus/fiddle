from functools import partial

raw = [1, 1, 3, 4, 7, 20]


grow = lambda size, foods: \
    size > foods[0] \
        if len(foods) == 1 \
        else (
            lambda head, *tail:
                grow(
                    size + head if size > head else size,
                    tail
                )
        )(*foods)


can_win = lambda foods: \
    list(map(
        int,
        map(
            partial(grow, foods=foods),
            foods)
    ))

print(can_win(raw))
