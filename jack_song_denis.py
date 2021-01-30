# from random import shuffle
import random

introduction = "This is"
snippets = {"That lay in": " the house that Jack built.\n",
            "That ate": " the malt\n",
            "That killed": " the rat,\n",
            "That worried": " the cat,\n",
            "That tossed": " the dog,\n",
            "That milked": " the cow with the crumpled horn,\n",
            "That kissed": " the maiden all forlorn,\n",
            "That married": " the man all tattered and torn,\n",
            "That waked": " the priest all shaven and shorn,\n",
            "That kept": " the rooster that crow'd in the morn,\n",
            "That belong to": " the farmer sowing his corn,\n",
            "This is": " the horse and the hound and the horn,\n"}


def song():
    actions = list(snippets.keys())
    stories = list(snippets.values())
    all_song = ""
    for rows in range(1, len(stories) + 1):
        couplet = ""
        for row in range(rows):
            if row == rows - 1:
                couplet = introduction + stories[row] + couplet
            else:
                couplet = actions[row] + stories[row] + couplet
        all_song += couplet + ("\n" if rows != len(stories) else "")
    return all_song.strip()


def double_song():
    actions = [""] + list(snippets.keys())
    stories = list(snippets.values())
    stories[0] = " the house that Jack built"
    all_song = ""
    for rows in range(1, len(stories) + 1):
        couplet = ""
        for row in range(rows):
            if row == rows - 1:
                couplet = introduction + stories[row] + actions[row] + stories[row] + couplet
            else:
                couplet = actions[row + 1] + stories[row] + actions[row] + stories[row] + couplet
            if row == rows - 1:
                couplet += ".\n"
        all_song += couplet + ("\n" if rows != len(stories) else "")
    return all_song.strip()


def random_song():
    actions = list(snippets.keys())
    random.shuffle(actions)
    stories = [snippets[key] for key in actions]
    snippets_values = list(snippets.values())
    snippets_keys = list(snippets.keys())
    local_snippets = {snippets_values[i]: snippets_keys[i - 1] for i in range(len(snippets_values))}
    all_song = ""
    for rows in range(1, len(stories) + 1):
        couplet = ""
        for row in range(rows):
            if row == 0:
                couplet = (introduction if rows == 1 else actions[row]) \
                          + stories[row] + local_snippets[stories[row]] + ".\n"
            elif row == rows - 1:
                couplet = introduction + stories[row] + couplet
            else:
                couplet = actions[row] + stories[row] + couplet
        all_song += couplet + ("\n" if rows != len(stories) else "")
    return all_song.strip()
