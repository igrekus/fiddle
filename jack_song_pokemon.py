from functools import partial

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
That lay in the house that Jack built."""


def song(verse=verse) -> str:
    make_verse = lambda n, v: "This is " + (lambda s: s[s.find("the"):])("\n".join(v[n:]))
    return (lambda v: "\n\n".join(map(partial(make_verse, v=v), range(len(v))[::-1])))(verse.split("\n"))


def double_song(verse=verse) -> str:
    _last_row = "the house that Jack built the house that Jack built."
    _conc = lambda s, n: (lambda f: f"{s[n][f(s[n]):]}\n{s[n + 1][:f(s[n + 1])]}")(lambda c: c.find("the"))
    make_verse = lambda n, v: n == len(v) - 1 and _last_row or 2 * (_conc(v, n)) + make_verse(n + 1, v)
    return (
        lambda v: "\n\n".join(map(lambda *args: "This is " + partial(make_verse, v=v)(*args), range(len(v))[::-1])))(
        verse.split("\n"))


def double_song_(verse=verse) -> str:
    # без хардкодинга последней строки, но тогда в ней пролезает лишняя точка
    _conc = lambda s, n: (lambda f: s[n][f(s[n]):] + (f"\n{s[n + 1][:f(s[n + 1])]}" if n < len(s) - 1 else ""))(
        lambda c: c.find("the"))
    make_verse = lambda n, v: "" if n == len(v) else 2 * (_conc(v, n)) + make_verse(n + 1, v)
    return (
        lambda v: "\n\n".join(map(lambda *args: "This is " + partial(make_verse, v=v)(*args), range(len(v))[::-1])))(
        verse.split("\n"))
