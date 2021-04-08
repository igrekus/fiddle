import random
import warnings

from textwrap import dedent
from pyexpect import expect

from solutions_old.jack_song_oop import random_song


container = list(reversed([
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


def shuffle_partched(cnt):
    global container
    for i in range(len(container)):
        cnt[i] = container[i]


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

    shf = random.shuffle
    random.shuffle = shuffle_partched

    with warnings.catch_warnings(record=True) as wns:
        expect(random_song()).to_equal(expected)
        wn = wns[-1]
        expect(wn.category).to_be(DeprecationWarning)
        expect(wn.message.args[0]).to_equal("'random_song' is deprecated, use parametrized 'song' instead")

    random.shuffle = shf
