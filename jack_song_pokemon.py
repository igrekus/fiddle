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


def song() -> str:
    make_verse = lambda n, v: (lambda f: "\n".join(f(v[n]) + v[n + 1:]))(lambda s: [f"This is {s[s.find('the'):]}"])
    return (lambda v: "\n\n".join(map(partial(make_verse, v=v), range(len(v))[::-1])))(verse.split("\n"))


if __name__ == '__main__':
    print(song())
