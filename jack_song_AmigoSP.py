import random
import logging
from typing import List, Optional

logging.basicConfig(format="DeprecationWarning: <%(funcName)s> is deprecated, use parametrized 'song' instead")
log = logging.getLogger(__name__)


class Song:
    def __init__(self):
        self.chunks_list = list(range(12))
        self.part_song = "This is {name}{action}"
        self.SETTINGS = [
            {'name': 'the house that Jack built', 'actions': ''},
            {'name': 'the malt', 'actions': '\nThat lay in'},
            {'name': 'the rat,', 'actions': '\nThat ate'},
            {'name': 'the cat,', 'actions': '\nThat killed'},
            {'name': 'the dog,', 'actions': '\nThat worried'},
            {'name': 'the cow with the crumpled horn,', 'actions': '\nThat tossed'},
            {'name': 'the maiden all forlorn,', 'actions': '\nThat milked'},
            {'name': 'the man all tattered and torn,', 'actions': '\nThat kissed'},
            {'name': 'the priest all shaven and shorn,', 'actions': '\nThat married'},
            {'name': "the rooster that crow'd in the morn,", 'actions': '\nThat waked'},
            {'name': "the farmer sowing his corn,", 'actions': '\nThat kept'},
            {'name': "the horse and the hound and the horn,", 'actions': '\nThat belong to'},
        ]
        self.start_couplet = 'This is'
        self.song = None

    def _get_path_song(self):
        for chunk in self.chunks_list:
            path_song = self.SETTINGS[chunk]
            yield path_song['name'], path_song['actions']

    def set_reverse(self):
        return '\n\n'.join(list(map(lambda x: x[::-1], self.set_song().split('\n\n'))))

    @property
    def get_song(self):
        self.song = self.set_song()
        return self.song

    def set_song(self):
        _text: List[str] = []
        prev_text = '.'
        for name, action in self._get_path_song():
            couplet = self.part_song.format(name=name, action=action)
            _text.append(couplet + prev_text)
            prev_text = _text[-1].replace(self.start_couplet, '')
        return '\n\n'.join(_text)


class BuilderJack(Song):
    def __init__(self, rnd, double, reverse, order):
        super().__init__()
        set_order = list(filter(lambda x: isinstance(x, List), [order, list(range(12))]))[0]
        self.dict_default = {
            'rnd': {
                True: random.sample(set_order, len(set_order)),
                False: set_order},
            'double': {
                True: "This is {name}{action} {name}{action}",
                False: "This is {name}{action}"},
            'reverse': {
                True: self.set_reverse,
                False: self.set_song},
            }
        self.chunks_list = self.dict_default['rnd'][rnd]
        self.part_song = self.dict_default['double'][double]
        self.song_revers = self.dict_default['reverse'][reverse]

    @property
    def get_song(self):
        self.song = self.song_revers()
        return self.song


def double_song():
    log.warning("")
    return song(False, True, False)


def random_song():
    log.warning("")
    return song(True, False, False)


def song(rnd=False, double=False, reverse=False, order: Optional[List[int]] = None):
    return BuilderJack(rnd=rnd, double=double, reverse=reverse, order=order).get_song


if __name__ == '__main__':
    # print(double_song())
    print(song(True, False, True, order=[0, 1, 2, 3, 4, 5]))
