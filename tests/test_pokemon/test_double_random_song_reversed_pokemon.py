import random

from textwrap import dedent
from pyexpect import expect

from jack_song_pokemon import song


container = [
    'the dog,\nThat worried ',
    'the farmer sowing his corn,\nThat kept ',
    'the cow with the crumpled horn,\nThat tossed ',
    'the horse and the hound and the horn,\nThat belong to ',
    'the malt\nThat lay in ',
    'the cat,\nThat killed ',
    'the priest all shaven and shorn,\nThat married ',
    "the rooster that crow'd in the morn,\nThat waked ",
    'the rat,\nThat ate ',
    'the man all tattered and torn,\nThat kissed ',
    'the maiden all forlorn,\nThat milked ',
    'the house that Jack built '
]


def sample_patched(seq, ln):
    return list(reversed(container))


def test_reversed_song():
    expected = dedent("""    .tliub kcaJ taht esuoh eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht eta tahT
    ,tar eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht eta tahT
    ,tar eht dellik tahT
    ,tac eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht eta tahT
    ,tar eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht eta tahT
    ,tar eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht eta tahT
    ,tar eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht eta tahT
    ,tar eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht eta tahT
    ,tar eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht eta tahT
    ,tar eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht eta tahT
    ,tar eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht tpek tahT
    ,nroc sih gniwos remraf eht si sihT
    
    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht eta tahT
    ,tar eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht tpek tahT
    ,nroc sih gniwos remraf eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht si sihT""")

    expect(song(reverse=True)).to_equal(expected)


def test_double_reversed_song():
    expected = dedent("""    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht eta tahT
    ,tar eht eta tahT
    ,tar eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht si sihT
    
    .tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht eta tahT
    ,tar eht eta tahT
    ,tar eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht deirrow tahT
    ,god eht deirrow tahT
    ,god eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht si sihT""")

    expect(song(double=True, reverse=True)).to_equal(expected)


def test_random_reversed_song():
    expected = dedent("""    .deirrow tahT
    ,god eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht eta tahT
    ,tar eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht si sihT
    
    .deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht tliub kcaJ taht esuoh eht si sihT""")

    smp = random.sample
    random.sample = sample_patched

    expect(song(rnd=True, reverse=True)).to_equal(expected)

    random.sample = smp


def test_random_double_reversed_song():
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
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht eta tahT
    ,tar eht eta tahT
    ,tar eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht eta tahT
    ,tar eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht eta tahT
    ,tar eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht si sihT
    
    .deirrow tahT
    ,god eht deirrow tahT
    ,god eht tpek tahT
    ,nroc sih gniwos remraf eht tpek tahT
    ,nroc sih gniwos remraf eht dessot tahT
    ,nroh delpmurc eht htiw woc eht dessot tahT
    ,nroh delpmurc eht htiw woc eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ot gnoleb tahT
    ,nroh eht dna dnuoh eht dna esroh eht ni yal tahT
    tlam eht ni yal tahT
    tlam eht dellik tahT
    ,tac eht dellik tahT
    ,tac eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht deirram tahT
    ,nrohs dna nevahs lla tseirp eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht dekaw tahT
    ,nrom eht ni d'worc taht retsoor eht eta tahT
    ,tar eht eta tahT
    ,tar eht dessik tahT
    ,nrot dna derettat lla nam eht dessik tahT
    ,nrot dna derettat lla nam eht deklim tahT
    ,nrolrof lla nediam eht deklim tahT
    ,nrolrof lla nediam eht tliub kcaJ taht esuoh eht tliub kcaJ taht esuoh eht si sihT""")

    smp = random.sample
    random.sample = sample_patched

    expect(song(rnd=True, double=True, reverse=True)).to_equal(expected)

    random.sample = smp

".dessik tahT\n,nrot dna derettat lla nam eht si sihT\n\n.dessik tahT\n,nrot dna derettat lla nam eht deklim tahT\n,nrolrof lla nediam eht si sihT\n\n.dessik tahT\n,nrot dna derettat lla nam eht deklim tahT\n,nrolrof lla nediam eht tpek tahT\n,nroc sih gniwos remraf eht si sihT\n\n.dessik tahT\n,nrot dna derettat lla nam eht deklim tahT\n,nrolrof lla nediam eht tpek tahT\n,nroc sih gniwos remraf eht dellik tahT\n,tac eht si sihT\n\n.dessik tahT\n,nrot dna derettat lla nam eht deklim tahT\n,nrolrof lla nediam eht tpek tahT\n,nroc sih gniwos remraf eht dellik tahT\n,tac eht dessot tahT\n,nroh delpmurc eht htiw woc eht si sihT\n\n.dessik tahT\n,nrot dna derettat lla nam eht deklim tahT\n,nrolrof lla nediam eht tpek tahT\n,nroc sih gniwos remraf eht dellik tahT\n,tac eht dessot tahT\n,nroh delpmurc eht htiw woc eht dekaw tahT\n,nrom eht ni d'worc taht retsoor eht si sihT\n\n.dessik tahT\n,nrot dna derettat lla nam eht deklim tahT\n,nrolrof lla nediam eht tpek tahT\n,nroc sih gniwos remraf eht dellik tahT\n,tac eht dessot tahT\n,nroh delpmurc eht htiw woc eht dekaw tahT\n,nrom eht ni d'worc taht retsoor eht eta tahT\n,tar eht si sihT\n\n.dessik tahT\n,nrot dna derettat lla nam eht deklim tahT\n,nrolrof lla nediam eht tpek tahT\n,nroc sih gniwos remraf eht dellik tahT\n,tac eht dessot tahT\n,nroh delpmurc eht htiw woc eht dekaw tahT\n,nrom eht ni d'worc taht retsoor eht eta tahT\n,tar eht ot gnoleb tahT\n,nroh eht dna dnuoh eht dna esroh eht si sihT\n\n.dessik tahT\n,nrot dna derettat lla nam eht deklim tahT\n,nrolrof lla nediam eht tpek tahT\n,nroc sih gniwos remraf eht dellik tahT\n,tac eht dessot tahT\n,nroh delpmurc eht htiw woc eht dekaw tahT\n,nrom eht ni d'worc taht retsoor eht eta tahT\n,tar eht ot gnoleb tahT\n,nroh eht dna dnuoh eht dna esroh eht deirram tahT\n,nrohs dna nevahs lla tseirp eht si sihT\n\n.dessik tahT\n,nrot dna derettat lla nam eht deklim tahT\n,nrolrof lla nediam eht tpek tahT\n,nroc sih gniwos remraf eht dellik tahT\n,tac eht dessot tahT\n,nroh delpmurc eht htiw woc eht dekaw tahT\n,nrom eht ni d'worc taht retsoor eht eta tahT\n,tar eht ot gnoleb tahT\n,nroh eht dna dnuoh eht dna esroh eht deirram tahT\n,nrohs dna nevahs lla tseirp eht deirrow tahT\n,god eht si sihT\n\n.dessik tahT\n,nrot dna derettat lla nam eht deklim tahT\n,nrolrof lla nediam eht tpek tahT\n,nroc sih gniwos remraf eht dellik tahT\n,tac eht dessot tahT\n,nroh delpmurc eht htiw woc eht dekaw tahT\n,nrom eht ni d'worc taht retsoor eht eta tahT\n,tar eht ot gnoleb tahT\n,nroh eht dna dnuoh eht dna esroh eht deirram tahT\n,nrohs dna nevahs lla tseirp eht deirrow tahT\n,god eht tliub kcaJ taht esuoh eht si sihT\n\n.dessik tahT\n,nrot dna derettat lla nam eht deklim tahT\n,nrolrof lla nediam eht tpek tahT\n,nroc sih gniwos remraf eht dellik tahT\n,tac eht dessot tahT\n,nroh delpmurc eht htiw woc eht dekaw tahT\n,nrom eht ni d'worc taht retsoor eht eta tahT\n,tar eht ot gnoleb tahT\n,nroh eht dna dnuoh eht dna esroh eht deirram tahT\n,nrohs dna nevahs lla tseirp eht deirrow tahT\n,god eht tliub kcaJ taht esuoh eht ni yal tahT\ntlam eht si sihT"
".deirrow tahT\n,god eht si sihT\n\n.deirrow tahT\n,god eht tpek tahT\n,nroc sih gniwos remraf eht si sihT\n\n.deirrow tahT\n,god eht tpek tahT\n,nroc sih gniwos remraf eht dessot tahT\n,nroh delpmurc eht htiw woc eht si sihT\n\n.deirrow tahT\n,god eht tpek tahT\n,nroc sih gniwos remraf eht dessot tahT\n,nroh delpmurc eht htiw woc eht ot gnoleb tahT\n,nroh eht dna dnuoh eht dna esroh eht si sihT\n\n.deirrow tahT\n,god eht tpek tahT\n,nroc sih gniwos remraf eht dessot tahT\n,nroh delpmurc eht htiw woc eht ot gnoleb tahT\n,nroh eht dna dnuoh eht dna esroh eht ni yal tahT\ntlam eht si sihT\n\n.deirrow tahT\n,god eht tpek tahT\n,nroc sih gniwos remraf eht dessot tahT\n,nroh delpmurc eht htiw woc eht ot gnoleb tahT\n,nroh eht dna dnuoh eht dna esroh eht ni yal tahT\ntlam eht dellik tahT\n,tac eht si sihT\n\n.deirrow tahT\n,god eht tpek tahT\n,nroc sih gniwos remraf eht dessot tahT\n,nroh delpmurc eht htiw woc eht ot gnoleb tahT\n,nroh eht dna dnuoh eht dna esroh eht ni yal tahT\ntlam eht dellik tahT\n,tac eht deirram tahT\n,nrohs dna nevahs lla tseirp eht si sihT\n\n.deirrow tahT\n,god eht tpek tahT\n,nroc sih gniwos remraf eht dessot tahT\n,nroh delpmurc eht htiw woc eht ot gnoleb tahT\n,nroh eht dna dnuoh eht dna esroh eht ni yal tahT\ntlam eht dellik tahT\n,tac eht deirram tahT\n,nrohs dna nevahs lla tseirp eht dekaw tahT\n,nrom eht ni d'worc taht retsoor eht si sihT\n\n.deirrow tahT\n,god eht tpek tahT\n,nroc sih gniwos remraf eht dessot tahT\n,nroh delpmurc eht htiw woc eht ot gnoleb tahT\n,nroh eht dna dnuoh eht dna esroh eht ni yal tahT\ntlam eht dellik tahT\n,tac eht deirram tahT\n,nrohs dna nevahs lla tseirp eht dekaw tahT\n,nrom eht ni d'worc taht retsoor eht eta tahT\n,tar eht si sihT\n\n.deirrow tahT\n,god eht tpek tahT\n,nroc sih gniwos remraf eht dessot tahT\n,nroh delpmurc eht htiw woc eht ot gnoleb tahT\n,nroh eht dna dnuoh eht dna esroh eht ni yal tahT\ntlam eht dellik tahT\n,tac eht deirram tahT\n,nrohs dna nevahs lla tseirp eht dekaw tahT\n,nrom eht ni d'worc taht retsoor eht eta tahT\n,tar eht dessik tahT\n,nrot dna derettat lla nam eht si sihT\n\n.deirrow tahT\n,god eht tpek tahT\n,nroc sih gniwos remraf eht dessot tahT\n,nroh delpmurc eht htiw woc eht ot gnoleb tahT\n,nroh eht dna dnuoh eht dna esroh eht ni yal tahT\ntlam eht dellik tahT\n,tac eht deirram tahT\n,nrohs dna nevahs lla tseirp eht dekaw tahT\n,nrom eht ni d'worc taht retsoor eht eta tahT\n,tar eht dessik tahT\n,nrot dna derettat lla nam eht deklim tahT\n,nrolrof lla nediam eht si sihT\n\n.deirrow tahT\n,god eht tpek tahT\n,nroc sih gniwos remraf eht dessot tahT\n,nroh delpmurc eht htiw woc eht ot gnoleb tahT\n,nroh eht dna dnuoh eht dna esroh eht ni yal tahT\ntlam eht dellik tahT\n,tac eht deirram tahT\n,nrohs dna nevahs lla tseirp eht dekaw tahT\n,nrom eht ni d'worc taht retsoor eht eta tahT\n,tar eht dessik tahT\n,nrot dna derettat lla nam eht deklim tahT\n,nrolrof lla nediam eht tliub kcaJ taht esuoh eht si sihT"
