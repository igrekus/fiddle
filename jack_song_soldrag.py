import random
from warnings import warn
from typing import Optional, List


class SongGenerator:
    def __init__(self, rnd: bool = False, count_mod: int = 1, reverse: bool = False, order: Optional[List[int]] = None):
        self.count_mod = count_mod
        self.rnd = rnd
        self.reverse = reverse
        self.order = order
        self.song = [
            {"action": " the house that Jack built", "object": ""},
            {"action": " lay in", "object": " the malt"},
            {"action": " ate", "object": " the rat,"},
            {"action": " killed", "object": " the cat,"},
            {"action": " worried", "object": " the dog,"},
            {"action": " tossed", "object": " the cow with the crumpled horn,"},
            {"action": " milked", "object": " the maiden all forlorn,"},
            {"action": " kissed", "object": " the man all tattered and torn,"},
            {"action": " married", "object": " the priest all shaven and shorn,"},
            {"action": " waked", "object": " the rooster that crow'd in the morn,"},
            {"action": " kept", "object": " the farmer sowing his corn,"},
            {"action": " belong to", "object": " the horse and the hound and the horn,"},
        ]
        if self.rnd:
            random.shuffle(self.song)
        if self.order:
            self.song = [self.song[i] for i in self.order]

    def couplet_generator(self, song_length: int) -> str:
        couplet = f"This is"
        for item in self.song[song_length::-1]:
            article = "\nThat" if item['object'] else ""
            couplet += f"{item['object']}{article}{item['action']}" * self.count_mod
        couplet = couplet.rstrip(",") + "."
        if self.reverse:
            couplet = couplet[::-1]
        return couplet


def song(rnd: bool = False, double: bool = False, reverse: bool = False, order: Optional[List[int]] = None) -> str:
    count_mod = 2 if double else 1
    jacks_song = SongGenerator(rnd=rnd, count_mod=count_mod, reverse=reverse, order=order).couplet_generator
    return '\n\n'.join([jacks_song(i) for i in range(12)])


def double_song() -> str:
    warn("'double_song' is deprecated, use parametrized 'song' instead", DeprecationWarning)
    return song(double=True)


def random_song() -> str:
    warn("'random_song' is deprecated, use parametrized 'song' instead", DeprecationWarning)
    return song(rnd=True)


if __name__ == '__main__':
    print(song(double=False, rnd=False, reverse=False, order=[11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
