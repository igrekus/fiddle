import random

from textwrap import dedent
from pyexpect import expect

from solutions_old.jack_song_func import song


container = [64, 96, 33, 40, 26, 18, 70, 99, 53, 28, 63, 8]
index = 0


def random_patched(a, b):
    global index
    ret = container[index]
    index += 1
    return ret


order = [0, 1, 9, 8, 7, 6, 4, 5, 2, 3, 10, 11]


def test_ordered_song():
    expected = dedent("""    This is the house that Jack built.
    
    This is the malt
    That lay in the house that Jack built.
    
    This is the priest all shaven and shorn,
    That married the malt
    That lay in the house that Jack built.
    
    This is the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the malt
    That lay in the house that Jack built.
    
    This is the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the malt
    That lay in the house that Jack built.
    
    This is the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the malt
    That lay in the house that Jack built.
    
    This is the cow with the crumpled horn,
    That tossed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the malt
    That lay in the house that Jack built.
    
    This is the dog,
    That worried the cow with the crumpled horn,
    That tossed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the malt
    That lay in the house that Jack built.
    
    This is the cat,
    That killed the dog,
    That worried the cow with the crumpled horn,
    That tossed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the malt
    That lay in the house that Jack built.
    
    This is the rat,
    That ate the cat,
    That killed the dog,
    That worried the cow with the crumpled horn,
    That tossed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the malt
    That lay in the house that Jack built.
    
    This is the farmer sowing his corn,
    That kept the rat,
    That ate the cat,
    That killed the dog,
    That worried the cow with the crumpled horn,
    That tossed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the malt
    That lay in the house that Jack built.
    
    This is the horse and the hound and the horn,
    That belong to the farmer sowing his corn,
    That kept the rat,
    That ate the cat,
    That killed the dog,
    That worried the cow with the crumpled horn,
    That tossed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the malt
    That lay in the house that Jack built.""")

    expect(song(order=order)).to_equal(expected)


def test_double_ordered_song():
    expected = dedent("""    This is the house that Jack built the house that Jack built.
    
    This is the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the dog,
    That worried the dog,
    That worried the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the cat,
    That killed the cat,
    That killed the dog,
    That worried the dog,
    That worried the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the rat,
    That ate the rat,
    That ate the cat,
    That killed the cat,
    That killed the dog,
    That worried the dog,
    That worried the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the rat,
    That ate the rat,
    That ate the cat,
    That killed the cat,
    That killed the dog,
    That worried the dog,
    That worried the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.
    
    This is the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the rat,
    That ate the rat,
    That ate the cat,
    That killed the cat,
    That killed the dog,
    That worried the dog,
    That worried the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.""")

    expect(song(double=True, order=order)).to_equal(expected)


def test_reversed_ordered_song():
    expected = dedent("""    .tliub kcaJ taht esuoh eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessot tahT
    ,nroh delpmurc eht htiw woc eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deirrow tahT
    ,god eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deirrow tahT
    ,god eht dellik tahT
    ,tac eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deirrow tahT
    ,god eht dellik tahT
    ,tac eht eta tahT
    ,tar eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deirrow tahT
    ,god eht dellik tahT
    ,tac eht eta tahT
    ,tar eht tpek tahT
    ,nroc sih gniwos remraf eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deirrow tahT
    ,god eht dellik tahT
    ,tac eht eta tahT
    ,tar eht tpek tahT
    ,nroc sih gniwos remraf eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht si sihT""")

    expect(song(reverse=True, order=order)).to_equal(expected)


def test_random_ordered_song():
    expected = dedent("""    This is the dog,
    That worried.
    
    This is the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the rat,
    That ate the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the man all tattered and torn,
    That kissed the rat,
    That ate the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the rat,
    That ate the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the rat,
    That ate the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the cat,
    That killed the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the rat,
    That ate the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the malt
    That lay in the cat,
    That killed the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the rat,
    That ate the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the horse and the hound and the horn,
    That belong to the malt
    That lay in the cat,
    That killed the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the rat,
    That ate the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the cow with the crumpled horn,
    That tossed the horse and the hound and the horn,
    That belong to the malt
    That lay in the cat,
    That killed the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the rat,
    That ate the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the horse and the hound and the horn,
    That belong to the malt
    That lay in the cat,
    That killed the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the rat,
    That ate the farmer sowing his corn,
    That kept the dog,
    That worried.
    
    This is the house that Jack built the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the horse and the hound and the horn,
    That belong to the malt
    That lay in the cat,
    That killed the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the rat,
    That ate the farmer sowing his corn,
    That kept the dog,
    That worried.""")

    global index
    index = 0
    tmp = random.randint
    random.randint = random_patched

    expect(song(rnd=True, order=order)).to_equal(expected)

    random.randint = tmp


def test_double_reversed_ordered_song():
    expected = dedent("""    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht eta tahT
    ,tar eht eta tahT
    ,tar eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht eta tahT
    ,tar eht eta tahT
    ,tar eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht eta tahT
    ,tar eht eta tahT
    ,tar eht tpek tahT
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
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dellik tahT
    ,tac eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dellik tahT
    ,tac eht ni yal tahT
    tlam eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dellik tahT
    ,tac eht ni yal tahT
    tlam eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dellik tahT
    ,tac eht ni yal tahT
    tlam eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht dessot tahT
    ,nroh delpmurc eht htiw woc eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dellik tahT
    ,tac eht ni yal tahT
    tlam eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dellik tahT
    ,tac eht ni yal tahT
    tlam eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht tliub kcaJ taht esuoh eht si sihT""")

    global index
    index = 0
    tmp = random.randint
    random.randint = random_patched

    expect(song(rnd=True, reverse=True, order=order)).to_equal(expected)

    random.randint = tmp


def test_random_double_ordered_song():
    expected = dedent("""    This is the dog,
    That worried the dog,
    That worried.
    
    This is the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the rat,
    That ate the rat,
    That ate the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the rat,
    That ate the rat,
    That ate the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the rat,
    That ate the rat,
    That ate the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the rat,
    That ate the rat,
    That ate the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the cat,
    That killed the cat,
    That killed the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the rat,
    That ate the rat,
    That ate the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the malt
    That lay in the malt
    That lay in the cat,
    That killed the cat,
    That killed the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the rat,
    That ate the rat,
    That ate the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the malt
    That lay in the malt
    That lay in the cat,
    That killed the cat,
    That killed the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the rat,
    That ate the rat,
    That ate the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the malt
    That lay in the malt
    That lay in the cat,
    That killed the cat,
    That killed the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the rat,
    That ate the rat,
    That ate the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the malt
    That lay in the malt
    That lay in the cat,
    That killed the cat,
    That killed the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the rat,
    That ate the rat,
    That ate the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.
    
    This is the house that Jack built the house that Jack built the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked the cow with the crumpled horn,
    That tossed the cow with the crumpled horn,
    That tossed the horse and the hound and the horn,
    That belong to the horse and the hound and the horn,
    That belong to the malt
    That lay in the malt
    That lay in the cat,
    That killed the cat,
    That killed the rooster that crow'd in the morn,
    That waked the rooster that crow'd in the morn,
    That waked the priest all shaven and shorn,
    That married the priest all shaven and shorn,
    That married the man all tattered and torn,
    That kissed the man all tattered and torn,
    That kissed the rat,
    That ate the rat,
    That ate the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the dog,
    That worried the dog,
    That worried.""")

    global index
    index = 0
    tmp = random.randint
    random.randint = random_patched

    expect(song(rnd=True, double=True, order=order)).to_equal(expected)

    random.randint = tmp


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
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht eta tahT
    ,tar eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht eta tahT
    ,tar eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht si sihT""")

    global index
    index = 0
    tmp = random.randint
    random.randint = random_patched

    expect(song(rnd=True, double=True, reverse=True, order=order)).to_equal(expected)

    random.randint = tmp
