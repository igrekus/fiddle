def song():
    return '''This is the house that Jack built.

This is the malt
That lay in the house that Jack built.

This is the rat,
That ate the malt
That lay in the house that Jack built.

This is the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.

This is the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.

This is the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.

This is the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.

This is the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.

This is the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.

This is the rooster that crow'd in the morn,
That waked the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.

This is the farmer sowing his corn,
That kept the rooster that crow'd in the morn,
That waked the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.

This is the horse and the hound and the horn,
That belong to the farmer sowing his corn,
That kept the rooster that crow'd in the morn,
That waked the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.'''


def double_song():
    song_text = song().split('\n')
    double_song_text = ''
    container = []
    for text_string in song_text:
        part_one = text_string.find('the')
        if not text_string:
            double_song_text += ''.join(container).replace('.', '') + ' ' + container[-1] + '\n\n'
            container = []
        elif not container:
            container = [text_string[:part_one], text_string[part_one:]]
        else:
            double_song_text += ''.join(container).replace('.', '') + '\n'
            container[0], next_value = text_string[:part_one], text_string[part_one:]
            double_song_text += ''.join(container).replace('.', '') + '\n'
            container[1] = next_value
    double_song_text += ''.join(container).replace('.', '') + ' ' + container[-1]
    return double_song_text


if __name__ == '__main__':
    with open('double_song.txt', 'r', encoding='utf-8') as rd_file:
        test_double = rd_file.read()
    assert double_song() == test_double, 'Не совпадает'
    print('Good job, freelancer Vasiliy')
