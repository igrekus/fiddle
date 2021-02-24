import random
import warnings
from typing import Optional

def double_couplet(n, l, rnd = False):
    couplet = f'This is {l[n][0]}'

    for k in range(n, -1, -1):
        if l[k][0] == 'the house that Jack built' and rnd:
            couplet = f'{couplet} {l[k][0]} {l[k-1][0]}'
        elif l[k][0] == 'the house that Jack built':
            couplet = f'{couplet} {l[k][0]}'
        else:
            if k == 0:
                couplet = f'{couplet}\n{l[k][1]} {l[k][0]}\n{l[k][1]}'
            else:
                couplet = f'{couplet}\n{l[k][1]} {l[k][0]}\n{l[k][1]} {l[k-1][0]}'


    return f'{couplet}.'

def couplet(n, l, rnd = False):
    couplet = f'This is {l[n][0]}'

    for k in range(n, 0, -1):
        if l[k][0] == 'the house that Jack built':
            couplet = f'{couplet} {l[k-1][0]}'
        else:
            couplet = f'{couplet}\n{l[k][1]} {l[k-1][0]}'

    return f'{couplet}\n{l[0][1]}.' if rnd and not l[0][0] == 'the house that Jack built' else f'{couplet}.'


def song(rnd: bool=False, double: bool=False, reverse: bool=False, order: Optional[list]=None):
    parts = [['the house that Jack built'], ['the malt', 'That lay in'], ['the rat,', 'That ate'], ['the cat,', 'That killed'],
    ['the dog,', 'That worried'], ['the cow with the crumpled horn,', 'That tossed'], ['the maiden all forlorn,', 'That milked'],
    ['the man all tattered and torn,', 'That kissed'], ['the priest all shaven and shorn,', 'That married'], ['the rooster that crow\'d in the morn,', 'That waked'],
    ['the farmer sowing his corn,', 'That kept'], ['the horse and the hound and the horn,', 'That belong to']]

    song = []

    if rnd:
        random.shuffle(parts)


    if order:
        tmp = []
        for i in range(12):
            tmp.append(parts[order[i]])
        parts = tmp


    if not rnd and not double:
        for i in range(12):
            song.append(couplet(i, parts))

    elif rnd and not double:
        for i in range(12):
            song.append(couplet(i, parts, True))

    elif double and not rnd:
        for i in range(12):
            song.append(double_couplet(i, parts))

    elif rnd and double:
        for i in range(12):
            song.append(double_couplet(i, parts, True))


    if reverse:
        for j in range(12):
            song[j] = song[j].split('\n')
            song[j] = song[j][::-1]

            for n in range(len(song[j])):
                song[j][n] = song[j][n][::-1]

            song[j] = '\n'.join(song[j])

    return '\n\n'.join(song)

def double_song():
    warnings.warn('\'double_song\' is deprecated, use parametrized \'song\' instead', DeprecationWarning)

    parts = [['the house that Jack built'], ['the malt', 'That lay in'], ['the rat,', 'That ate'], ['the cat,', 'That killed'],
    ['the dog,', 'That worried'], ['the cow with the crumpled horn,', 'That tossed'], ['the maiden all forlorn,', 'That milked'],
    ['the man all tattered and torn,', 'That kissed'], ['the priest all shaven and shorn,', 'That married'], ['the rooster that crow\'d in the morn,', 'That waked'],
    ['the farmer sowing his corn,', 'That kept'], ['the horse and the hound and the horn,', 'That belong to']]

    song = []

    for i in range(12):
        song.append(double_couplet(i, parts))

    return '\n\n'.join(song)


def random_song():
    warnings.warn('\'random_song\' is deprecated, use parametrized \'song\' instead', DeprecationWarning)

    parts = [['the house that Jack built'], ['the malt', 'That lay in'], ['the rat,', 'That ate'], ['the cat,', 'That killed'],
    ['the dog,', 'That worried'], ['the cow with the crumpled horn,', 'That tossed'], ['the maiden all forlorn,', 'That milked'],
    ['the man all tattered and torn,', 'That kissed'], ['the priest all shaven and shorn,', 'That married'], ['the rooster that crow\'d in the morn,', 'That waked'],
    ['the farmer sowing his corn,', 'That kept'], ['the horse and the hound and the horn,', 'That belong to']]

    song = []

    random.shuffle(parts)

    for i in range(12):
        song.append(couplet(i, parts, True))

    return '\n\n'.join(song)
