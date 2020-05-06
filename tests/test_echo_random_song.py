import random

from textwrap import dedent
from pyexpect import expect

from fiddle import song

new = [
    'the cat,\nThat killed ', 'the cow with the crumpled horn,\nThat tossed ', 'the rat,\nThat ate ',
    'the priest all shaven and shorn,\nThat married ',
    "the rooster that crow'd in the morn,\nThat waked ", 'the house that Jack built ',
    'the man all tattered and torn,\nThat kissed ',
    'the horse and the hound and the horn,\nThat belong to ', 'the dog,\nThat worried ',
    'the malt\nThat lay in ', 'the maiden all forlorn,\nThat milked ',
    'the farmer sowing his corn,\nThat kept '
]


def shuffle(it):
    for i in range(len(it)):
        it[i] = new[i]


def test_random_song():
    expected = dedent("""This is the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married.

    This is the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married.

    This is the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married.

    This is the malt
    That lay in the malt
    That lay in the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married.

    This is the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married.

    This is the dog,
    That worried the dog,
    That worried the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married.

    This is the house that Jack built the house that Jack built the dog,
    That worried the dog,
    That worried the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married.

    This is the cat,
    That killed the cat,
    That killed the house that Jack built the house that Jack built the dog,
    That worried the dog,
    That worried the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married.

    This is the rat,
    That ate the rat,
    That ate the cat,
    That killed the cat,
    That killed the house that Jack built the house that Jack built the dog,
    That worried the dog,
    That worried the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married.

    This is the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the rat,
    That ate the rat,
    That ate the cat,
    That killed the cat,
    That killed the house that Jack built the house that Jack built the dog,
    That worried the dog,
    That worried the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married.

    This is the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the rat,
    That ate the rat,
    That ate the cat,
    That killed the cat,
    That killed the house that Jack built the house that Jack built the dog,
    That worried the dog,
    That worried the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married.

    This is the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the rat,
    That ate the rat,
    That ate the cat,
    That killed the cat,
    That killed the house that Jack built the house that Jack built the dog,
    That worried the dog,
    That worried the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married.\n""")
    sf = random.shuffle
    random.shuffle = shuffle
    res = song(rnd=True, echo=True)
    expect(res).to_equal(expected)
    random.shuffle = sf

    print(res)
