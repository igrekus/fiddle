import itertools
import random
import warnings

__all__ = ['song', 'double_song', 'random_song']


class DefaultOrder:
    def __init__(self, order=None):
        self._order = order
    def order(self, data):
        return data


class RandomOrder(DefaultOrder):
    def order(self, data):
        d = list(data)
        random.shuffle(d)
        return d


class NumberedOrder(DefaultOrder):
    def order(self, data):
        return [data[i] for i in self._order]


class DefaultLine:
    def format(self, parts):
        return parts


class DoubleLine:
    def format(self, parts):
        return itertools.chain(*[[l, r] for l, r in zip(parts, parts)])


class DefaultVerse:
    def format(self, string):
        return string


class ReversedVerse:
    def format(self, string):
        return string[::-1]


class Song:
    random_orderers = {True: RandomOrder, False: DefaultOrder}
    numbered_orderers = {True: NumberedOrder, False: DefaultOrder}
    line_formatters = {True: DoubleLine, False: DefaultLine}
    verse_formatters = {True: ReversedVerse, False: DefaultVerse}
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

    def __init__(self, random_orderer, line_formatter, verse_formatter, numbered_orderer):
        self._line_formatter = line_formatter
        self._data = numbered_orderer.order(random_orderer.order(self._data))
        self._verse_formatter = verse_formatter

    def __str__(self):
        return '\n\n'.join(self._verse(i) for i in range(1, len(self) + 1))

    def _verse(self, num):
        return self._verse_formatter.format(f'This is {self._phrase(num).strip()}.')

    def _phrase(self, num):
        return ''.join(self._parts(num))

    def _parts(self, num):
        return self._line_formatter.format(self._data[-num:])

    def __len__(self):
        return self._data.__len__()


def song(rnd=False, double=False, reverse=False, order=None):
    return str(
        Song(
            random_orderer=Song.random_orderers[rnd](),
            line_formatter=Song.line_formatters[double](),
            verse_formatter=Song.verse_formatters[reverse](),
            numbered_orderer=Song.numbered_orderers[bool(order)](order)
        )
    )


def double_song():
    warnings.warn("'double_song' is deprecated, use parametrized 'song' instead", DeprecationWarning)
    return song(rnd=False, double=True)


def random_song():
    warnings.warn("'random_song' is deprecated, use parametrized 'song' instead", DeprecationWarning)
    return song(rnd=True, double=False)
