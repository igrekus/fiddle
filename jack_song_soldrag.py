from string import Template

DOUBLE_SONG = """This is the house that Jack built the house that Jack built.

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
That lay in the house that Jack built the house that Jack built."""


class SongGenerator:
    def __init__(self):
        self.song = (Template("$action the house that Jack built."),
                     Template("$action the malt"),
                     Template("$action the rat,"),
                     Template("$action the cat,"),
                     Template("$action the dog,"),
                     Template("$action the cow with the crumpled horn,"),
                     Template("$action the maiden all forlorn,"),
                     Template("$action the man all tattered and torn,"),
                     Template("$action the priest all shaven and shorn,"),
                     Template("$action the rooster that crow'd in the morn,"),
                     Template("$action the farmer sowing his corn,"),
                     Template("$action the horse and the hound and the horn,"),)
        self.action = ("That lay in",
                       "That ate",
                       "That killed",
                       "That worried",
                       "That tossed",
                       "That milked",
                       "That kissed",
                       "That married",
                       "That waked",
                       "That kept",
                       "That belong to",
                       "This is")

    def couplet_generator(self, couplet_number) -> str:
        if couplet_number == 0:
            return self.song[couplet_number].substitute(action=self.action[-1])
        else:
            ret_song = []
            count = 0
            while count < couplet_number:
                ret_song.append(self.song[count].substitute(action=self.action[count]))
                count += 1
            else:
                ret_song.append(self.song[count].substitute(action=self.action[-1]))
            return '\n'.join(ret_song[::-1])


def song() -> str:
    jacks_song = SongGenerator()
    completed_song = []
    for i in range(len(jacks_song.song)):
        completed_song.append(jacks_song.couplet_generator(i))
    return '\n\n'.join(completed_song)


def double_song() -> str:
    return DOUBLE_SONG


if __name__ == '__main__':
    print(double_song())
