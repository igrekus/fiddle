from string import Template


class SongGenerator:
    def __init__(self):
        self.first_couplet = "This is the house that Jack built."
        self.song = (Template("$action in the house that Jack built."),
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
        self.action = ("That lay",
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
            return self.first_couplet
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


if __name__ == '__main__':
    print(song())
