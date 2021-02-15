import random
from warnings import warn

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

_depr = lambda f: lambda: (lambda g: ((lambda h: warn(
    f"'{__import__('inspect').getsource(h).split('=')[0].strip()[2:]}' is deprecated, use parametrized 'song' instead",
    DeprecationWarning))(g) or g)())(f)

__double_song = lambda v=verse: _make_song(
    lambda s: list(map(lambda r: 2 * r, s)),
    v)
__random_song = lambda v=verse: _make_song(
    lambda s: random.sample(s, len(s)),
    v)

double_song = _depr(__double_song)
random_song = _depr(__random_song)


def song(rnd: bool = False, double: bool = False) -> str:
    functions = {"rnd": lambda s: random.sample(s, len(s)),
                 "double": lambda s: list(map(lambda r: 2 * r, s))}

    _p = lambda arg, fs: _p(fs[0](arg), fs[1:]) if len(fs) > 1 else fs[0](arg)

    return (lambda locs, fs: _make_song(lambda v: _p(v, [fs.get(k) for k in fs.keys() if locs.get(k)]
                                                     or (lambda s: s,)), verse))(locals(), functions)
