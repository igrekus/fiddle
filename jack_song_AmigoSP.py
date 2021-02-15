import random
import inspect
import logging

logging.basicConfig(format='%(message)s')
log = logging.getLogger(__name__)


def who_called(func):
    def wrapper():
        value = inspect.stack()[1][3]
        warning_string = f"DeprecationWarning: <{func.__name__}> is deprecated, use parametrized 'song' instead"
        if value == "<module>":
            log.warning(warning_string)
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
def double_song():
    chunk_list = list(range(0, 12))
    counter_cuplet = 12
    _text = []
    prev_text = ''
    double_random = hasattr(song, '_is_random')
    for _ in range(1, counter_cuplet + 1):
        if not double_random:
            name, actions = _get_path_song(_ - 1)
        else:
            chunk_random = random.choice(chunk_list)
            chunk_list.remove(chunk_random)
            name, actions = _get_path_song(chunk_random)
        if _ == 1 and not actions:
            _text.append(f"This is the {name} the {name}.")
        elif _ == 1 and actions:
            _text.append(f"This is the {name}\nThat {actions} the {name}\nThat {actions}.")
        elif actions:
            _text.append(f"This is the {name}\nThat {actions} the {name}\nThat {actions} the {prev_text}")
        else:
            _text.append(f"This is the {name} the {name} the {prev_text}")
        prev_text = _text[-1].replace('This is the ', '')
    return '\n\n'.join(_text)


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


if __name__ == '__main__':
    print(song(True, True))
    print(double_song())