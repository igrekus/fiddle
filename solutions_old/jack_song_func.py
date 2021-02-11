import itertools
import random
import warnings

__all__ = ['song', 'double_song', 'random_song']

_random = lambda it: sorted(it, key=lambda _: random.randint(0, 100))
_double = lambda it: itertools.chain(*[[lhs, rhs] for lhs, rhs in zip(it, it)])
_reverse = lambda it: it[::-1]
_id = lambda it: it

_order = {True: _random, False: _id}
_line_format = {True: _double, False: _id}
_verse_format = {True: _reverse, False: _id}

_recite = lambda data, fmt, rev: \
    '\n\n'.join(
        rev(
            'This is {}.'.format(
                ''.join(
                    fmt(data[-i:])
                ).strip()
            )
        )
        for i in range(1, len(data) + 1)
    )

song = lambda rnd=False, double=False, reverse=False:\
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
        fmt=_line_format[double],
        rev=_verse_format[reverse]
    )

double_song = lambda: \
    warnings.warn("'double_song' is deprecated, use parametrized 'song' instead", DeprecationWarning) or \
    song(rnd=False, double=True)
random_song = lambda: \
    warnings.warn("'random_song' is deprecated, use parametrized 'song' instead", DeprecationWarning) or \
    song(rnd=True, double=False)
