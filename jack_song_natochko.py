body = ('the horse and the hound and the horn,\n'
        'That belong to the farmer sowing his corn,\n'
        'That kept &the rooster that crow\'d in the morn,\n'
        'That waked &the priest all shaven and shorn,\n'
        'That married &the man all tattered and torn,\n'
        'That kissed &the maiden all forlorn,\n'
        'That milked &the cow with the crumpled horn,\n'
        'That tossed &the dog,\n'
        'That worried &the cat,\n'
        'That killed &the rat,\n'
        'That ate &the malt\n'
        'That lay in ').split('&')


def song(n):
    inside = '' if n == 0 else ''.join(body[-n:])
    return 'This is {}the house that Jack built.'.format(inside)


def sing():
    result = '\n\n'.join(song(n) for n in range(len(body)))
    return result


print(sing())
