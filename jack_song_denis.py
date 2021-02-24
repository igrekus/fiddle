import warnings
import random
from typing import Optional, List

introduction = "This is"
snippets = {"That lay in": " the house that Jack built\n",
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
            "null": " the horse and the hound and the horn,\n"}


def song(rnd: bool = False, double: bool = False, reverse: bool = False, order: Optional[List[int]] = None) -> str:
    cases = {(False, False): _song,
             (False, True): _double_song,
             (True, False): _random_song,
             (True, True): _double_random_song}
    return "\n".join([couplet[::-1] for couplet in cases[(rnd, double)](order)]).strip() if reverse\
        else "\n".join(cases[(rnd, double)](order)).strip()


def _actions_to_order(lines, index_diff):
    actions = list(snippets.keys())
    stories = list(snippets.values())
    return [actions[stories.index(i) - index_diff] for i in lines]


def _stories_to_order(lines, order):
    return [lines[i] for i in order]


def _couplet_normalize(couplet):
    return couplet.replace("\nnull", '').replace(",\nnull", '').replace(",\n.\n", ".\n").replace("\n.\n", ".\n")


def _song(order):
    actions = list(snippets.keys())
    stories = list(snippets.values())
    order = list(range(12)) if order is None else order
    if order:
        stories = _stories_to_order(stories, order)
        actions = _actions_to_order(stories, 1)
    all_song = list()
    for rows in range(1, len(stories) + 1):
        couplet = ""
        for row in range(rows):
            if row == rows - 1:
                couplet = introduction + stories[row] + actions[row] + couplet + ".\n"
            else:
                couplet = stories[row] + actions[row] + couplet
            couplet = _couplet_normalize(couplet)
        all_song.append(couplet)
    return all_song


def double_song():
    warnings.warn("'double_song' is deprecated, use parametrized 'song' instead", DeprecationWarning)
    return "\n".join(_double_song(None)).strip()


def _double_song(order):
    actions = list(snippets.keys())
    stories = list(snippets.values())
    actions.insert(0, actions.pop())
    if order:
        stories = _stories_to_order(stories, order)
        actions = _actions_to_order(stories, 1)
    all_song = list()
    for rows in range(1, len(stories) + 1):
        couplet = ""
        for row in range(rows):
            if row == rows - 1:
                couplet = introduction + stories[row] + actions[row] + stories[row] + couplet + ".\n"
            else:
                couplet = actions[row + 1] + stories[row] + actions[row] + stories[row] + couplet
            couplet = _couplet_normalize(couplet)
        all_song.append(couplet)
    return all_song


def random_song():
    warnings.warn("'random_song' is deprecated, use parametrized 'song' instead", DeprecationWarning)
    return "\n".join(_random_song(None)).strip()


def _random_song(order):
    actions = list(snippets.keys())
    random.shuffle(actions)
    stories = [snippets[key] for key in actions]
    if order:
        stories = _stories_to_order(stories, order)
    snippets_values = list(snippets.values())
    snippets_keys = list(snippets.keys())
    shifted_snippets = {snippets_values[i]: snippets_keys[i - 1] for i in range(len(snippets_values))}
    all_song = list()
    for rows in range(1, len(stories) + 1):
        couplet = ""
        for row in range(rows):
            if row == rows - 1:
                couplet = introduction + stories[row] + shifted_snippets[stories[row]] + couplet + ".\n"
            else:
                couplet = stories[row] + shifted_snippets[stories[row]] + couplet
            couplet = _couplet_normalize(couplet)
        all_song.append(couplet)
    return all_song


def _double_random_song(order):
    actions = list(snippets.keys())
    random.shuffle(actions)
    stories = [snippets[key] for key in actions]
    if order:
        stories = _stories_to_order(stories, order)
    snippets_values = list(snippets.values())
    snippets_keys = list(snippets.keys())
    shifted_snippets = {snippets_values[i]: snippets_keys[i - 1] for i in range(len(snippets_values))}
    all_song = list()
    for rows in range(1, len(stories) + 1):
        couplet = ""
        for row in range(rows):
            if row == rows - 1:
                couplet = introduction + (stories[row] + shifted_snippets[stories[row]]) * 2 + couplet + '.\n'
            else:
                couplet = (stories[row] + shifted_snippets[stories[row]]) * 2 + couplet
            couplet = _couplet_normalize(couplet)
        all_song.append(couplet)
    return all_song
