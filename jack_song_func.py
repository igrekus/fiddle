import itertools
import random


def _random(it): return sorted(it, key=lambda x: random.randint(0, 100))
def _double(it): return itertools.chain(*[[lhs, rhs] for lhs, rhs in zip(it, it)])
def _id(it): return it


order = {True: _random, False: _id}
format = {True: _double, False: _id}


def _recite(data, fmt):
    return '\n\n'.join(
        'This is {}.'.format(
            ''.join(
                fmt(data[-i:])
            ).strip()
        )
        for i in range(1, len(data) + 1)
    )


def song(rnd=False, double=False):
    return _recite(
        data=order[rnd]([
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
        fmt=format[double]
    )