from pyexpect import expect
from textwrap import dedent

# from jack_song_oop import song   # pass
# from jack_song_func import song   # pass
# from jack_song_AmigoSP import song   # pass
# from jack_song_denis import song   # pass
# from jack_song_perf0mance_artist import song   # pass
from jack_song_pokemon import song   # pass
# from jack_song_ikrill import song   # pass
# from jack_song_soldrag import song   # pass
# from jack_song_Ramzes229 import song
# from jack_song_Natocko import song


def test_whole_song():
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
