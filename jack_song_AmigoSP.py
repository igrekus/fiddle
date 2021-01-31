import random

ORIGINAL_SONG = """This is the house that Jack built.

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
That lay in the house that Jack built."""

SETTINGS = [
    {'name': 'house that Jack built', 'actions': ''},
    {'name': 'malt', 'actions': 'lay in'},
    {'name': 'rat,', 'actions': 'ate'},
    {'name': 'cat,', 'actions': 'killed'},
    {'name': 'dog,', 'actions': 'worried'},
    {'name': 'cow with the crumpled horn,', 'actions': 'tossed'},
    {'name': 'maiden all forlorn,', 'actions': 'milked'},
    {'name': 'man all tattered and torn,', 'actions': 'kissed'},
    {'name': 'priest all shaven and shorn,', 'actions': 'married'},
    {'name': "rooster that crow'd in the morn,", 'actions': 'waked'},
    {'name': "farmer sowing his corn,", 'actions': 'kept'},
    {'name': "horse and the hound and the horn,", 'actions': 'belong to'},
]


def _get_path_song():
    path_song = random.choice(SETTINGS)
    SETTINGS.remove(path_song)
    return path_song['name'], path_song['actions']


def random_song():
    counter_cuplet = 12
    _text = []
    prev_text = ''
    for _ in range(1, counter_cuplet + 1):
        name, actions = _get_path_song()
        if _ == 1 and not actions:
            _text.append(f"This is the {name}.")
        elif _ == 1 and actions:
            _text.append(f"This is the {name}\nThat {actions}.")
        else:
            if actions:
                _text.append(f"This is the {name}\nThat {actions} the {prev_text}")
            else:
                _text.append(f"This is the {name} the {prev_text}")
        prev_text = _text[-1].replace('This is the ', '')
    return '\n\n'.join(_text)


def song():
    return ORIGINAL_SONG


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
    print(random_song())
