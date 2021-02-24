import random

from textwrap import dedent
from pyexpect import expect

from solutions_old.jack_song_oop import song


container = list(reversed([
    "the dog,\nThat worried ",
    "the farmer sowing his corn,\nThat kept ",
    "the cow with the crumpled horn,\nThat tossed ",
    "the horse and the hound and the horn,\nThat belong to ",
    "the malt\nThat lay in ",
    "the cat,\nThat killed ",
    "the priest all shaven and shorn,\nThat married ",
    "the rooster that crow'd in the morn,\nThat waked ",
    "the rat,\nThat ate ",
    "the man all tattered and torn,\nThat kissed ",
    "the maiden all forlorn,\nThat milked ",
    "the house that Jack built "
]))


def random_patched(cnt):
    global container
    for i in range(len(container)):
        cnt[i] = container[i]


order = [0, 1, 9, 8, 7, 6, 4, 5, 2, 3, 10, 11]


def test_ordered_song():
    expected = dedent("""    This is the house that Jack built.
    
    This is the malt
    That lay in the house that Jack built.
    
    This is the rooster that crow'd in the morn,
    That waked the malt
    That lay in the house that Jack built.
    
    This is the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the malt
    That lay in the house that Jack built.
    
    This is the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the malt
    That lay in the house that Jack built.
    
    This is the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the malt
    That lay in the house that Jack built.
    
    This is the dog,
    That worried the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the malt
    That lay in the house that Jack built.
    
    This is the cow with the crumpled horn,
    That tossed the dog,
    That worried the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the malt
    That lay in the house that Jack built.
    
    This is the rat,
    That ate the cow with the crumpled horn,
    That tossed the dog,
    That worried the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the malt
    That lay in the house that Jack built.
    
    This is the cat,
    That killed the rat,
    That ate the cow with the crumpled horn,
    That tossed the dog,
    That worried the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the malt
    That lay in the house that Jack built.
    
    This is the farmer sowing his corn,
    That kept the cat,
    That killed the rat,
    That ate the cow with the crumpled horn,
    That tossed the dog,
    That worried the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the malt
    That lay in the house that Jack built.
    
    This is the horse and the hound and the horn,
    That belong to the farmer sowing his corn,
    That kept the cat,
    That killed the rat,
    That ate the cow with the crumpled horn,
    That tossed the dog,
    That worried the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the malt
    That lay in the house that Jack built.""")

    expect(song(order=order)).to_equal(expected)


def test_double_ordered_song():
    expected = dedent("""    This is the house that Jack built the house that Jack built.
    
    This is the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the dog,
    That worried the dog,
    That worried the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the dog,
    That worried the dog,
    That worried the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the rat,
    That ate the rat,
    That ate the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the dog,
    That worried the dog,
    That worried the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the cat,
    That killed the cat,
    That killed the rat,
    That ate the rat,
    That ate the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the dog,
    That worried the dog,
    That worried the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the cat,
    That killed the cat,
    That killed the rat,
    That ate the rat,
    That ate the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the dog,
    That worried the dog,
    That worried the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the cat,
    That killed the cat,
    That killed the rat,
    That ate the rat,
    That ate the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the dog,
    That worried the dog,
    That worried the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.""")

    expect(song(double=True, order=order)).to_equal(expected)


def test_reversed_ordered_song():
    expected = dedent("""    .tliub kcaJ taht esuoh eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht deirrow tahT
    ,god eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht eta tahT
    ,tar eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht eta tahT
    ,tar eht dellik tahT
    ,tac eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht eta tahT
    ,tar eht dellik tahT
    ,tac eht tpek tahT
    ,nroc sih gniwos remraf eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht eta tahT
    ,tar eht dellik tahT
    ,tac eht tpek tahT
    ,nroc sih gniwos remraf eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht si sihT""")

    expect(song(reverse=True, order=order)).to_equal(expected)


def test_random_ordered_song():
    expected = dedent("""    This is the dog,
    That worried.
    
    This is the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the rat,
    That ate the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the rooster that crow'd in the morn,
    That waked the rat,
    That ate the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rat,
    That ate the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the malt
    That lay in the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rat,
    That ate the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the cat,
    That killed the malt
    That lay in the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rat,
    That ate the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the cow with the crumpled horn,
    That tossed the cat,
    That killed the malt
    That lay in the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rat,
    That ate the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the cat,
    That killed the malt
    That lay in the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rat,
    That ate the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the maiden all forlorn,
    That milked the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the cat,
    That killed the malt
    That lay in the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rat,
    That ate the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the house that Jack built the maiden all forlorn,
    That milked the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the cat,
    That killed the malt
    That lay in the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rat,
    That ate the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the dog,
    That worried.""")

    tmp = random.shuffle
    random.shuffle = random_patched

    expect(song(rnd=True, order=order)).to_equal(expected)

    random.shuffle = tmp


def test_double_reversed_ordered_song():
    expected = dedent("""    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht eta tahT
    ,tar eht eta tahT
    ,tar eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht eta tahT
    ,tar eht eta tahT
    ,tar eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht eta tahT
    ,tar eht eta tahT
    ,tar eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht eta tahT
    ,tar eht eta tahT
    ,tar eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht si sihT""")

    expect(song(double=True, reverse=True, order=order)).to_equal(expected)


def test_random_reversed_ordered_song():
    expected = dedent("""    .deirrow tahT
    ,god eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht ni yal tahT
    tlam eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dessot tahT
    ,nroh delpmurc eht htiw woc eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht deklim tahT
    ,nrolrof lla nediam eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht deklim tahT
    ,nrolrof lla nediam eht tliub kcaJ taht esuoh eht si sihT""")

    tmp = random.shuffle
    random.shuffle = random_patched

    expect(song(rnd=True, reverse=True, order=order)).to_equal(expected)

    random.shuffle = tmp


def test_random_double_ordered_song():
    expected = dedent("""    This is the dog,
    That worried the dog,
    That worried.
    
    This is the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the rat,
    That ate the rat,
    That ate the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the rat,
    That ate the rat,
    That ate the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the rat,
    That ate the rat,
    That ate the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the malt
    That lay in the malt
    That lay in the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the rat,
    That ate the rat,
    That ate the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the cat,
    That killed the cat,
    That killed the malt
    That lay in the malt
    That lay in the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the rat,
    That ate the rat,
    That ate the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the cat,
    That killed the cat,
    That killed the malt
    That lay in the malt
    That lay in the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the rat,
    That ate the rat,
    That ate the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the cat,
    That killed the cat,
    That killed the malt
    That lay in the malt
    That lay in the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the rat,
    That ate the rat,
    That ate the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the cat,
    That killed the cat,
    That killed the malt
    That lay in the malt
    That lay in the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the rat,
    That ate the rat,
    That ate the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the house that Jack built the house that Jack built the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the cat,
    That killed the cat,
    That killed the malt
    That lay in the malt
    That lay in the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the rat,
    That ate the rat,
    That ate the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.""")

    tmp = random.shuffle
    random.shuffle = random_patched

    expect(song(rnd=True, double=True, order=order)).to_equal(expected)

    random.shuffle = tmp


def test_random_double_reverse_ordered_song():
    expected = dedent("""    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht eta tahT
    ,tar eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht si sihT""")

    tmp = random.shuffle
    random.shuffle = random_patched

    expect(song(rnd=True, double=True, reverse=True, order=order)).to_equal(expected)

    random.shuffle = tmp
