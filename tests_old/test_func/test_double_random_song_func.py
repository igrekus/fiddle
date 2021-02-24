import random

from textwrap import dedent
from pyexpect import expect

from solutions_old.jack_song_func import song

rs = [64, 96, 33, 40, 26, 18, 70, 99, 53, 28, 63, 8]
index = 0


def randint_patched(a, b):
    global index
    ret = rs[index]
    index += 1
    return ret


def test_song():
    expected = dedent("""    This is the house that Jack built.
    
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
    That lay in the house that Jack built.""")

    expect(song()).to_equal(expected)


def test_double_song():
    expected = dedent("""    This is the house that Jack built the house that Jack built.

    This is the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.

    This is the rat,
    That ate the rat,
    That ate the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.

    This is the cat,
    That killed the cat,
    That killed the rat,
    That ate the rat,
    That ate the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.

    This is the dog,
    That worried the dog,
    That worried the cat,
    That killed the cat,
    That killed the rat,
    That ate the rat,
    That ate the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.

    This is the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the dog,
    That worried the dog,
    That worried the cat,
    That killed the cat,
    That killed the rat,
    That ate the rat,
    That ate the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.

    This is the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the dog,
    That worried the dog,
    That worried the cat,
    That killed the cat,
    That killed the rat,
    That ate the rat,
    That ate the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.

    This is the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the dog,
    That worried the dog,
    That worried the cat,
    That killed the cat,
    That killed the rat,
    That ate the rat,
    That ate the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.

    This is the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the dog,
    That worried the dog,
    That worried the cat,
    That killed the cat,
    That killed the rat,
    That ate the rat,
    That ate the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.

    This is the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the dog,
    That worried the dog,
    That worried the cat,
    That killed the cat,
    That killed the rat,
    That ate the rat,
    That ate the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.

    This is the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the dog,
    That worried the dog,
    That worried the cat,
    That killed the cat,
    That killed the rat,
    That ate the rat,
    That ate the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.

    This is the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the dog,
    That worried the dog,
    That worried the cat,
    That killed the cat,
    That killed the rat,
    That ate the rat,
    That ate the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.""")

    expect(song(double=True)).to_equal(expected)


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

    global index
    index = 0

    rint = random.randint
    random.randint = randint_patched

    expect(song(rnd=True)).to_equal(expected)

    random.randint = rint


def test_double_random_song():
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

    global index
    index = 0

    rint = random.randint
    random.randint = randint_patched

    expect(song(rnd=True, double=True)).to_equal(expected)

    random.randint = rint
