import random

def random_couplet(n, l):  
    couplet = f'This is {l[n][0]}'

    for k in range(n, 0, -1):
        if l[k][0] == 'the house that Jack built':
            couplet = f'{couplet} {l[k-1][0]}'
        else:
            couplet = f'{couplet}\n{l[k][1]} {l[k-1][0]}'

    return f'{couplet}\n{l[0][1]}.'

def generate_double_couplet(n):
    plot = ['That lay in', 'That ate', 'That killed', 'That worried',
    'That tossed', 'That milked', 'That kissed', 'That married',
    'That waked', 'That kept', 'That belong to']

    actors = ['the house that Jack built', 'the malt', 'the rat,',
    'the cat,', 'the dog,', 'the cow with the crumpled horn,',
    'the maiden all forlorn,', 'the man all tattered and torn,', 'the priest all shaven and shorn,',
    'the rooster that crow\'d in the morn,', 'the farmer sowing his corn,', 'the horse and the hound and the horn,']

    couplet = f'This is {actors[n]}'

    if n == 0:
        couplet = f'This is {actors[n]} {actors[n]}'

    if n+1 > 1:
        for k in range(n-1, 0, -1):
            couplet = f'{couplet}\n{plot[k]} {actors[k+1]}\n{plot[k]} {actors[k]}'

        couplet = f'{couplet}\n{plot[0]} {actors[1]}\n{plot[0]} {actors[0]} {actors[0]}'

    return f'{couplet}.'

def generate_couplet(n):
    plot = ['That lay in', 'That ate', 'That killed', 'That worried',
    'That tossed', 'That milked', 'That kissed', 'That married',
    'That waked', 'That kept', 'That belong to']

    actors = ['the house that Jack built', 'the malt', 'the rat,',
    'the cat,', 'the dog,', 'the cow with the crumpled horn,',
    'the maiden all forlorn,', 'the man all tattered and torn,', 'the priest all shaven and shorn,',
    'the rooster that crow\'d in the morn,', 'the farmer sowing his corn,', 'the horse and the hound and the horn,']

    couplet = f'This is {actors[n]}'

    for k in range(n, 0, -1):
        couplet = f'{couplet}\n{plot[k-1]} {actors[k-1]}'

    return f'{couplet}.'

def random_song():
    parts = [['the house that Jack built'], ['the malt', 'That lay in'], ['the rat,', 'That ate'], ['the cat,', 'That killed'],
    ['the dog,', 'That worried'], ['the cow with the crumpled horn,', 'That tossed'], ['the maiden all forlorn,', 'That milked'],
    ['the man all tattered and torn,', 'That kissed'], ['the priest all shaven and shorn,', 'That married'], ['the rooster that crow\'d in the morn,', 'That waked'],
    ['the farmer sowing his corn,', 'That kept'], ['the horse and the hound and the horn,', 'That belong to']]

    random.shuffle(parts)

    song = []

    for i in range(12):
        song.append(random_couplet(i, parts))
        
    return '\n\n'.join(song)

def song():
    song = []

    for i in range(12):
        song.append(generate_couplet(i))
        
    return '\n\n'.join(song)

def double_song():
    song = []

    for i in range(12):
        song.append(generate_double_couplet(i))
        
    return '\n\n'.join(song)