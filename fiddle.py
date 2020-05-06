import itertools
import random


class DefaultOrder:
    def order(self, data):
        return data


class RandomOrder:
    def order(self, data):
        d = list(data)
        random.shuffle(d)
        return d


class Song:
    def __init__(self, orderer=None):
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
        self._orderer = DefaultOrder() if orderer is None else orderer
        self.data = self._orderer.order(self.data)

    def recite(self):
        return '\n'.join(self.line(i) for i in range(1, len(self.data) + 1))

    def line(self, num):
        return f'This is {self._phrase(num).strip()}.\n'

    def _parts(self, num):
        return self.data[-num:]

    def _phrase(self, num):
        return ''.join(self._parts(num))


class EchoSong(Song):
    def __init__(self):
        super().__init__()

    def _parts(self, num):
        return itertools.chain(*[[l, r] for l, r in zip(super()._parts(num), super()._parts(num))])


class EchoRandomSong(Song):
    def __init__(self):
        super().__init__(orderer=RandomOrder())
    def _parts(self, num):
        return itertools.chain(*[[l, r] for l, r in zip(super()._parts(num), super()._parts(num))])


def song(rnd=False, echo=False):
    if rnd and not echo:
        return Song(orderer=RandomOrder()).recite()
    elif not rnd and echo:
        return EchoSong().recite()
    elif rnd and echo:
        return EchoRandomSong().recite()
    else:
        return Song().recite()


def line(num):
    return Song().line(num)


print(song(echo=True))
