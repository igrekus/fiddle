original_song = """
This is the house that Jack built.

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

This is the horse and the hound and the horn 
that belong to the farmer sowing his corn,
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
"""

refactor_song = """
This is the house that Jack built.

This is the malt that lay in
The house that Jack built.

This is the rat that ate
The malt that lay in
The house that Jack built.

This is the cat that killed
The rat that ate
The malt that lay in
The house that Jack built.

This is the dog that worried
The cat that killed
The rat that ate
The malt that lay in
The house that Jack built.

This is the cow with the crumpled horn that tossed
The dog that worried
The cat that killed
The rat that ate
The malt that lay in
The house that Jack built.

This is the maiden all forlorn that milked
The cow with the crumpled horn that tossed
The dog that worried
The cat that killed
The rat that ate
The malt that lay in
The house that Jack built.

This is the man all tattered and torn that kissed
The maiden all forlorn that milked
The cow with the crumpled horn that tossed
The dog that worried
The cat that killed
The rat that ate
The malt That lay in
The house that Jack built.

This is the priest all shaven and shorn that married
The man all tattered and torn that kissed
The maiden all forlorn that milked
The cow with the crumpled horn that tossed
The dog that worried
The cat that killed
The rat that ate
The malt that lay in
Yhe house that Jack built.

This is the rooster that crowed in the morn that woke
The judge all shaven and shorn that married
The man all tattered and torn That kissed
The maiden all forlorn that milked
The cow with the crumpled horn that tossed
The dog that worried
The cat that killed
The rat that ate
The malt that lay in
The house that Jack built.

This is the farmer sowing his corn that kept
The rooster that crowed in the morn that woke
The judge all shaven and shorn that married
The man all tattered and torn that kissed
The maiden all forlorn that milked
The cow with the crumpled horn that tossed
The dog that worried
The cat that killed
The rat that ate
The malt that lay in
The house that Jack built.

This is the horse and the hound and the horn that belonged to
The farmer sowing his corn that kept
The rooster that crowed in
The morn that woke
The judge all shaven and shorn that married
The man all tattered and torn that kissed
The maiden all forlorn that milked
The cow with the crumpled horn that tossed
The dog that worried
The cat that killed
The rat that ate
The malt that lay in
The house that Jack built.
"""

from pyexpect import expect
from fiddle import song


def test_whole_song():
    expect(song()).to_equal(original_song)
