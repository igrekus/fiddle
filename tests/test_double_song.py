import warnings

from pyexpect import expect
from textwrap import dedent

from solutions_old.jack_song_oop import double_song   # pass
# from solutions_old.jack_song_func import double_song   # pass
# from jack_song_AmigoSP import double_song   # pass
# from jack_song_denis import double_song   # pass
# from jack_song_perf0mance_artist import double_song   # pass
# from jack_song_pokemon import double_song   # pass
# from jack_song_soldrag import double_song   # pass
# from jack_song_ikrill import double_song   # pass
# from jack_song_Ramzes229 import double_song
# from jack_song_Natocko import double_song


def test_whole_double_song():
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
    expect(double_song()).to_equal(expected)
