import random

from textwrap import dedent
from pyexpect import expect

from jack_song_denis import song


container = [
    "That tossed",
    "That belong to",
    "That milked",
    "null",
    "That ate",
    "That worried",
    "That waked",
    "That kept",
    "That killed",
    "That married",
    "That kissed",
    "That lay in"
]


def shuffle_patched(cnt):
    global container
    for i in range(len(container)):
        cnt[i] = container[i]


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

    shf = random.shuffle
    random.shuffle = shuffle_patched

    expect(song(rnd=True, reverse=True)).to_equal(expected)

    random.shuffle = shf


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

    shf = random.shuffle
    random.shuffle = shuffle_patched

    expect(song(rnd=True, double=True, reverse=True)).to_equal(expected)

    random.shuffle = shf

