import random


class Song:
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
        'the house that Jack built'
    ]

    def recite(self):
        return '\n'.join(self.line(i) for i in range(1, len(self.data) + 1))

    def line(self, num):
        return f'This is {self._phrase(num).strip()}.\n'

    def _parts(self, num):
        return self.data[-num:]

    def _phrase(self, num):
        return ''.join(self._parts(num))


class RandomSong(Song):
    def __init__(self):
        random.shuffle(self.data)


def song(rnd=False):
    return Song().recite() if not rnd else RandomSong().recite()


def line(num):
    return Song().line(num)


print(song(rnd=True))
