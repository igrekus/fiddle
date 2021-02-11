import random
import inspect


def who_called(func):
    def wrapper():
        value = inspect.stack()[1][3]
        warning_string = f"DeprecationWarning: <{func.__name__}> is deprecated, use parametrized 'song' instead"
        if value == "<module>":
            print(warning_string)
        return func()

    return wrapper


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


def _get_path_song(chunk: int):
    path_song = SETTINGS[chunk]
    return path_song['name'], path_song['actions']


@who_called
def random_song():
    chunk_list = list(range(0, 12))
    counter_cuplet = 12
    _text = []
    prev_text = ''
    for _ in range(1, counter_cuplet + 1):
        chunk_random = random.choice(chunk_list)
        chunk_list.remove(chunk_random)
        name, actions = _get_path_song(chunk_random)
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


def song(rnd=False, double=False):
    if rnd and double:
        setattr(song, '_is_random', True)
        text_song = double_song()
        delattr(song, '_is_random')
        return text_song
    elif rnd is True and double is False:
        return random_song()
    elif rnd is False and double is True:
        return double_song()
    else:
        return ORIGINAL_SONG


def _random_and_double(text_song: str) -> str:
    new_text = []
    check_chunk = 'the house that Jack built'
    new_chunk = 'the house that Jack built the house that Jack built'
    for chunk in text_song.split('\n'):
        new_text.append(chunk.replace(check_chunk, new_chunk))
    return '\n'.join(new_text)


def _adapting_to_4_task(container: list) -> str:
    if container[-1] != '.':
        text = ''.join(container).replace('.', '') + ' ' + container[-1] + '\n\n'
    else:
        text = ''.join(container).replace(' .', '.') + '\n\n'
    return text


@who_called
def double_song():
    _is_random = hasattr(song, '_is_random')
    if not _is_random:
        song_text = song().split('\n')
    else:
        song_text = random_song().split('\n')
    double_song_text = ''
    container = []
    for text_string in song_text:
        part_one = text_string.find('the')
        if not text_string:
            double_song_text += _adapting_to_4_task(container)
            container = []
        elif not container:
            container = [text_string[:part_one], text_string[part_one:]]
        else:
            double_song_text += ''.join(container).replace('.', '') + '\n'
            if part_one >= 0:
                container[0], next_value = text_string[:part_one], text_string[part_one:]
            else:
                container[0], next_value = f'{text_string[:part_one]} ', text_string[part_one:]
            double_song_text += ''.join(container).replace('.', '') + '\n'
            container[1] = next_value
    double_song_text += _adapting_to_4_task(container)
    double_song_text = double_song_text.strip()
    return double_song_text if not _is_random else _random_and_double(double_song_text)


if __name__ == '__main__':
    print(random_song())
