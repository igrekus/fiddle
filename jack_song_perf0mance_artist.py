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

def double_song():
    song = []

    for i in range(12):
        song.append(generate_double_couplet(i))
        
    return '\n\n'.join(song)

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

def song():
    song = []

    for i in range(12):
        song.append(generate_couplet(i))
        
    return '\n\n'.join(song)

print(song())