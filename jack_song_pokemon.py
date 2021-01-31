import random

verse = """This is the horse and the hound and the horn,
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
That lay in the house that Jack built """

_make_story = lambda v, n: (lambda f: v[n][f(v[n]):] + (f"\n{v[n + 1][:f(v[n + 1])]}" if n < len(v) - 1 else ""))(
    lambda c: c.find("the"))
_decompose_verse = lambda v: list(map(lambda n: _make_story(v, n), range(len(v))))
_decor = lambda v, n: "This is " + "".join(v[n:]).strip() + "."
_make_song = lambda f, s: (lambda v: "\n\n".join(map(lambda n: _decor(v, n), range(len(v))[::-1])))(
    f(_decompose_verse(s.split("\n"))))

song = lambda v=verse: _make_song(
    lambda s: s,
    v)
double_song = lambda v=verse: _make_song(
    lambda s: list(map(lambda r: 2 * r, s)),
    v)
random_song = lambda v=verse: _make_song(
    lambda s: random.sample(s, len(s)),
    v)
