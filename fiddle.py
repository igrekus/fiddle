import itertools
import random


def _random_order(data):
    return sorted(data, key=lambda x: random.randint(0, 100))


def _double_format(parts): return itertools.chain(*[[lhs, rhs] for lhs, rhs in zip(parts, parts)])


def _id(x): return x


orders = {True: _random_order, False: _id}
formats = {True: _double_format, False: _id}

data = [
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


def _parts(data, format, num):
    return format(data[-num:])


def _phrase(data, format, num):
    return ''.join(_parts(data, format, num))


def _line(data, format, num):
    return f'This is {_phrase(data, format, num).strip()}.'


order = None
format = None


class Song:
    def __init__(self, data, order, format):
        self._order = order
        self._format = format
        self.data = data

    def __str__(self):
        return '\n\n'.join(_line(self.data, format, i) for i in range(1, len(self.data) + 1))


def song(rnd=False, double=False):
    global order, format, data
    order = orders[rnd]
    format = formats[double]
    d = order(data)
    return str(Song(data=d, order=order, format=format))
