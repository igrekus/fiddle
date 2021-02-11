import itertools
import random
import warnings

__all__ = ['song', 'double_song', 'random_song']


class DefaultOrder:
    def order(self, data):
        return data


class RandomOrder:
    def order(self, data):
        d = list(data)
        random.shuffle(d)
        return d


class DefaultFormat:
    def format(self, parts):
        return parts


class DoubleFormat:
    def format(self, parts):
        return itertools.chain(*[[l, r] for l, r in zip(parts, parts)])


class Song:
    orderers = {True: RandomOrder, False: DefaultOrder}
    formatters = {True: DoubleFormat, False: DefaultFormat}
    _data = [
        'the horse and the hound and the horn,\nThat belong to ',
        'the farmer sowing his corn,\nThat kept ',
        'the rooster that crow\'d in the morn,\nThat waked ',
        'the priest all shaven and shorn,\nThat married ',
        'the man all tattered and torn,\nThat kissed ',
        'the maiden all forlorn,\nThat milked ',
        'the cow with the crumpled horn,\nThat tossed ',
        'the dog,\nThat worried ',
        'the cat,\nThat killed ',
        'the rat,\nThat ate ',
        'the malt\nThat lay in ',
        'the house that Jack built '
    ]

    def __init__(self, orderer, formatter):
        self._formatter = formatter
        self._data = orderer.order(self._data)

    def __str__(self):
        return '\n\n'.join(self._line(i) for i in range(1, len(self) + 1))

    def _line(self, num):
        return f'This is {self._phrase(num).strip()}.'

    def _phrase(self, num):
        return ''.join(self._parts(num))

    def _parts(self, num):
        return self._formatter.format(self._data[-num:])

    def __len__(self):
        return self._data.__len__()


def song(rnd=False, double=False):
    return str(Song(orderer=Song.orderers[rnd](), formatter=Song.formatters[double]()))


def double_song():
    warnings.warn("'double_song' is deprecated, use parametrized 'song' instead", DeprecationWarning)
    return song(rnd=False, double=True)


def random_song():
    warnings.warn("'random_song' is deprecated, use parametrized 'song' instead", DeprecationWarning)
    return song(rnd=True, double=False)
