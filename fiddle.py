import itertools
import random


def _random_order(data):
    d = list(data)
    random.shuffle(d)
    return d


def _double_format(parts): return itertools.chain(*[[lhs, rhs] for lhs, rhs in zip(parts, parts)])


def _id(x): return x


orders = {True: _random_order, False: _id}
formats = {True: _double_format, False: _id}


class Song:

    def __init__(self, order, format):
        self.data = [
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
        self._order = order
        self._format = format
        self.data = self._order(self.data)

    def __str__(self):
        return '\n\n'.join(self._line(i) for i in range(1, len(self) + 1))

    def _line(self, num):
        return f'This is {self._phrase(num).strip()}.'

    def _parts(self, num):
        return self._format(self.data[-num:])

    def _phrase(self, num):
        return ''.join(self._parts(num))

    def __len__(self):
        return self.data.__len__()


def song(rnd=False, double=False):
    return str(Song(order=orders[rnd], format=formats[double]))
