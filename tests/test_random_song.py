import random

from textwrap import dedent
from pyexpect import expect

from solutions_old.jack_song_oop import random_song
# from solutions_old.jack_song_func import random_song
# from jack_song_AmigoSP import random_song   # pass
# from jack_song_denis import random_song   # pass
# from jack_song_perf0mance_artist import random_song   # pass
# from jack_song_pokemon import random_song   # pass
# from jack_song_soldrag import song
# from jack_song_ikrill import song
# from jack_song_Ramzes229 import song
# from jack_song_Natocko import song


rs = [64, 96, 33, 40, 26, 18, 70, 99, 53, 28, 63, 8]
index = 0


def randint(a, b):
    global index
    ret = rs[index]
    index += 1
    return ret


container_denis = [
    "That tossed",
    "That belong to",
    "That milked",
    "",
    "That ate",
    "That worried",
    "That waked",
    "That kept",
    "That killed",
    "That married",
    "That kissed",
    "That lay in"
]


def shuffle_denis(cnt):
    global container_denis
    for i in range(len(container_denis)):
        cnt[i] = container_denis[i]


container_oop = list(reversed([
    "the dog,\nThat worried ",
    "the farmer sowing his corn,\nThat kept ",
    "the cow with the crumpled horn,\nThat tossed ",
    "the horse and the hound and the horn,\nThat belong to ",
    "the malt\nThat lay in ",
    "the cat,\nThat killed ",
    "the priest all shaven and shorn,\nThat married ",
    "the rooster that crow'd in the morn,\nThat waked ",
    "the rat,\nThat ate ",
    "the man all tattered and torn,\nThat kissed ",
    "the maiden all forlorn,\nThat milked ",
    "the house that Jack built "
]))


def shuffle_oop(cnt):
    global container_oop
    for i in range(len(container_oop)):
        cnt[i] = container_oop[i]


container_performancearist = [
    ['the dog,', 'That worried'],
    ['the farmer sowing his corn,', 'That kept'],
    ['the cow with the crumpled horn,', 'That tossed'],
    ['the horse and the hound and the horn,', 'That belong to'],
    ['the malt', 'That lay in'],
    ['the cat,', 'That killed'],
    ['the priest all shaven and shorn,', 'That married'],
    ['the rooster that crow\'d in the morn,', 'That waked'],
    ['the rat,', 'That ate'],
    ['the man all tattered and torn,', 'That kissed'],
    ['the maiden all forlorn,', 'That milked'],
    ['the house that Jack built'],
]


def shuffle_performanceartist(cnt):
    global container_performancearist
    for i in range(len(container_performancearist)):
        cnt[i] = container_performancearist[i]


container_amigo = [
    {'name': 'dog,', 'actions': 'worried'},
    {'name': "farmer sowing his corn,", 'actions': 'kept'},
    {'name': 'cow with the crumpled horn,', 'actions': 'tossed'},
    {'name': "horse and the hound and the horn,", 'actions': 'belong to'},
    {'name': 'malt', 'actions': 'lay in'},
    {'name': 'cat,', 'actions': 'killed'},
    {'name': 'priest all shaven and shorn,', 'actions': 'married'},
    {'name': "rooster that crow'd in the morn,", 'actions': 'waked'},
    {'name': 'rat,', 'actions': 'ate'},
    {'name': 'man all tattered and torn,', 'actions': 'kissed'},
    {'name': 'maiden all forlorn,', 'actions': 'milked'},
    {'name': 'house that Jack built', 'actions': ''},
]


def choice_amigo(seq):
    global index
    ret = container_amigo[index]
    index += 1
    return ret


container_pokemon = [
    'the dog,\nThat worried ',
    'the farmer sowing his corn,\nThat kept ',
    'the cow with the crumpled horn,\nThat tossed ',
    'the horse and the hound and the horn,\nThat belong to ',
    'the malt\nThat lay in ',
    'the cat,\nThat killed ',
    'the priest all shaven and shorn,\nThat married ',
    "the rooster that crow'd in the morn,\nThat waked ",
    'the rat,\nThat ate ',
    'the man all tattered and torn,\nThat kissed ',
    'the maiden all forlorn,\nThat milked ',
    'the house that Jack built '
]


def sample_pokemon(seq, ln):
    return list(reversed(container_pokemon))


def test_random_song():
    expected = dedent("""    This is the dog,
    That worried.

    This is the farmer sowing his corn,
    That kept the dog,
    That worried.

    This is the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the dog,
    That worried.

    This is the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the dog,
    That worried.

    This is the malt
    That lay in the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the dog,
    That worried.

    This is the cat,
    That killed the malt
    That lay in the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the dog,
    That worried.

    This is the priest all shaven and shorn,
    That married the cat,
    That killed the malt
    That lay in the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the dog,
    That worried.

    This is the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the cat,
    That killed the malt
    That lay in the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the dog,
    That worried.

    This is the rat,
    That ate the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the cat,
    That killed the malt
    That lay in the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the dog,
    That worried.

    This is the man all tattered and torn,
    That kissed the rat,
    That ate the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the cat,
    That killed the malt
    That lay in the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the dog,
    That worried.

    This is the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the rat,
    That ate the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the cat,
    That killed the malt
    That lay in the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the dog,
    That worried.

    This is the house that Jack built the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the rat,
    That ate the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the cat,
    That killed the malt
    That lay in the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the dog,
    That worried.""")
    rnd = random.randint
    shf = random.shuffle
    chs = random.choice
    smp = random.sample

    random.randint = randint
    # random.shuffle = shuffle_denis
    random.shuffle = shuffle_oop
    # random.shuffle = shuffle_performanceartist
    random.choice = choice_amigo
    random.sample = sample_pokemon

    expect(random_song()).to_equal(expected)

    random.randint = rnd
    random.shuffle = shf
    random.choice = chs
    random.sample = smp
