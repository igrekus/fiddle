import random

from unittest import mock

from textwrap import dedent
from pyexpect import expect

# from jack_song_oop import random_song
# from jack_song_func import song
# from jack_song_AmigoSP import song
from jack_song_denis import random_song

# from jack_song_perf0mance_artist import song
# from jack_song_pokemon import song
# from jack_song_ikrill import song
# from jack_song_soldrag import song
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
    random.randint = randint
    random.shuffle = shuffle_denis

    # with mock.patch('random.shuffle', shuffle):
    #     expect(random_song()).to_equal(expected)
    expect(random_song()).to_equal(expected)

    random.randint = rnd
    random.shuffle = shf
