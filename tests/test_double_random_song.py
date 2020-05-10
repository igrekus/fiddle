import random

from textwrap import dedent
from pyexpect import expect

from fiddle import song


rs = [64, 96, 33, 40, 26, 18, 70, 99, 53, 28, 63, 8]
index = 0


def randint(a, b):
    global index
    ret = rs[index]
    index += 1
    return ret


def test_echo_random_song():
    expected = dedent("""    This is the dog,
    That worried the dog,
    That worried.

    This is the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.

    This is the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.

    This is the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.

    This is the malt
    That lay in the malt
    That lay in the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.

    This is the cat,
    That killed the cat,
    That killed the malt
    That lay in the malt
    That lay in the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.

    This is the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the cat,
    That killed the cat,
    That killed the malt
    That lay in the malt
    That lay in the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.

    This is the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the cat,
    That killed the cat,
    That killed the malt
    That lay in the malt
    That lay in the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.

    This is the rat,
    That ate the rat,
    That ate the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the cat,
    That killed the cat,
    That killed the malt
    That lay in the malt
    That lay in the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.

    This is the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the rat,
    That ate the rat,
    That ate the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the cat,
    That killed the cat,
    That killed the malt
    That lay in the malt
    That lay in the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.

    This is the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the rat,
    That ate the rat,
    That ate the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the cat,
    That killed the cat,
    That killed the malt
    That lay in the malt
    That lay in the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.

    This is the house that Jack built the house that Jack built the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the rat,
    That ate the rat,
    That ate the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the cat,
    That killed the cat,
    That killed the malt
    That lay in the malt
    That lay in the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.""")
    rnd = random.randint
    random.randint = randint
    expect(song(rnd=True, double=True)).to_equal(expected)
    random.randint = rnd
