import random

from textwrap import dedent
from pyexpect import expect

from jack_song_denis import song


container = [
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


def shuffle_patched(cnt):
    global container
    for i in range(len(container)):
        cnt[i] = container[i]


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

    shf = random.shuffle
    random.shuffle = shuffle_patched

    expect(song(rnd=True)).to_equal(expected)

    random.shuffle = shf


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
    shf = random.shuffle

    random.shuffle = shuffle_patched

    expect(song(rnd=True, double=True)).to_equal(expected)
    random.shuffle = shf
