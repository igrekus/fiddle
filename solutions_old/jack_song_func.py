import itertools
import random

_random = lambda it: sorted(it, key=lambda _: random.randint(0, 100))
_double = lambda it: itertools.chain(*[[lhs, rhs] for lhs, rhs in zip(it, it)])
_id = lambda it: it

_order = {True: _random, False: _id}
_format = {True: _double, False: _id}

_recite = lambda data, fmt: \
    '\n\n'.join(
        'This is {}.'.format(
            ''.join(
                fmt(data[-i:])
            ).strip()
        )
        for i in range(1, len(data) + 1)
    )

song = lambda rnd=False, double=False:\
    _recite(
        data=_order[rnd]([
            "the horse and the hound and the horn,\nThat belong to ",
            "the farmer sowing his corn,\nThat kept ",
            "the rooster that crow'd in the morn,\nThat waked ",
            "the priest all shaven and shorn,\nThat married ",
            "the man all tattered and torn,\nThat kissed ",
            "the maiden all forlorn,\nThat milked ",
            "the cow with the crumpled horn,\nThat tossed ",
            "the dog,\nThat worried ",
            "the cat,\nThat killed ",
            "the rat,\nThat ate ",
            "the malt\nThat lay in ",
            "the house that Jack built "
        ]),
        fmt=_format[double]
    )
