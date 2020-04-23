from pyexpect import expect
from fiddle import Bottles


def test_1_verse():
    b = Bottles()
    verse = 99
    expect(b.verse(verse)).to_equal('''99 бутылок пива на стене
99 бутылок пива!
Возьми одну, передай мне
98 бутылок пива на стене
''')


def test_2_verse():
    b = Bottles()
    verse = 98
    expect(b.verse(verse)).to_equal('''98 бутылок пива на стене
98 бутылок пива!
Возьми одну, передай мне
97 бутылок пива на стене
''')


def test_3_verse():
    b = Bottles()
    verse = 97
    expect(b.verse(verse)).to_equal('''97 бутылок пива на стене
97 бутылок пива!
Возьми одну, передай мне
96 бутылок пива на стене
''')


def test_4_verse():
    b = Bottles()
    verse = 96
    expect(b.verse(verse)).to_equal('''96 бутылок пива на стене
96 бутылок пива!
Возьми одну, передай мне
95 бутылок пива на стене
''')


def test_5_verse():
    b = Bottles()
    verse = 95
    expect(b.verse(verse)).to_equal('''95 бутылок пива на стене
95 бутылок пива!
Возьми одну, передай мне
94 бутылки пива на стене
''')


def test_6_verse():
    b = Bottles()
    verse = 94
    expect(b.verse(verse)).to_equal('''94 бутылки пива на стене
94 бутылки пива!
Возьми одну, передай мне
93 бутылки пива на стене
''')


def test_7_verse():
    b = Bottles()
    verse = 93
    expect(b.verse(verse)).to_equal('''93 бутылки пива на стене
93 бутылки пива!
Возьми одну, передай мне
92 бутылки пива на стене
''')


def test_8_verse():
    b = Bottles()
    verse = 92
    expect(b.verse(verse)).to_equal('''92 бутылки пива на стене
92 бутылки пива!
Возьми одну, передай мне
91 бутылка пива на стене
''')


def test_9_verse():
    b = Bottles()
    verse = 91
    expect(b.verse(verse)).to_equal('''91 бутылка пива на стене
91 бутылка пива!
Возьми одну, передай мне
90 бутылок пива на стене
''')


def test_10_verse():
    b = Bottles()
    verse = 90
    expect(b.verse(verse)).to_equal('''90 бутылок пива на стене
90 бутылок пива!
Возьми одну, передай мне
89 бутылок пива на стене
''')


def test_11_verse():
    b = Bottles()
    verse = 89
    expect(b.verse(verse)).to_equal('''89 бутылок пива на стене
89 бутылок пива!
Возьми одну, передай мне
88 бутылок пива на стене
''')


def test_12_verse():
    b = Bottles()
    verse = 88
    expect(b.verse(verse)).to_equal('''88 бутылок пива на стене
88 бутылок пива!
Возьми одну, передай мне
87 бутылок пива на стене
''')


def test_13_verse():
    b = Bottles()
    verse = 87
    expect(b.verse(verse)).to_equal('''87 бутылок пива на стене
87 бутылок пива!
Возьми одну, передай мне
86 бутылок пива на стене
''')


def test_14_verse():
    b = Bottles()
    verse = 86
    expect(b.verse(verse)).to_equal('''86 бутылок пива на стене
86 бутылок пива!
Возьми одну, передай мне
85 бутылок пива на стене
''')


def test_15_verse():
    b = Bottles()
    verse = 85
    expect(b.verse(verse)).to_equal('''85 бутылок пива на стене
85 бутылок пива!
Возьми одну, передай мне
84 бутылки пива на стене
''')


def test_16_verse():
    b = Bottles()
    verse = 84
    expect(b.verse(verse)).to_equal('''84 бутылки пива на стене
84 бутылки пива!
Возьми одну, передай мне
83 бутылки пива на стене
''')


def test_17_verse():
    b = Bottles()
    verse = 83
    expect(b.verse(verse)).to_equal('''83 бутылки пива на стене
83 бутылки пива!
Возьми одну, передай мне
82 бутылки пива на стене
''')


def test_18_verse():
    b = Bottles()
    verse = 82
    expect(b.verse(verse)).to_equal('''82 бутылки пива на стене
82 бутылки пива!
Возьми одну, передай мне
81 бутылка пива на стене
''')


def test_19_verse():
    b = Bottles()
    verse = 81
    expect(b.verse(verse)).to_equal('''81 бутылка пива на стене
81 бутылка пива!
Возьми одну, передай мне
80 бутылок пива на стене
''')


def test_20_verse():
    b = Bottles()
    verse = 80
    expect(b.verse(verse)).to_equal('''80 бутылок пива на стене
80 бутылок пива!
Возьми одну, передай мне
79 бутылок пива на стене
''')


def test_21_verse():
    b = Bottles()
    verse = 79
    expect(b.verse(verse)).to_equal('''79 бутылок пива на стене
79 бутылок пива!
Возьми одну, передай мне
78 бутылок пива на стене
''')


def test_22_verse():
    b = Bottles()
    verse = 78
    expect(b.verse(verse)).to_equal('''78 бутылок пива на стене
78 бутылок пива!
Возьми одну, передай мне
77 бутылок пива на стене
''')


def test_23_verse():
    b = Bottles()
    verse = 77
    expect(b.verse(verse)).to_equal('''77 бутылок пива на стене
77 бутылок пива!
Возьми одну, передай мне
76 бутылок пива на стене
''')


def test_24_verse():
    b = Bottles()
    verse = 76
    expect(b.verse(verse)).to_equal('''76 бутылок пива на стене
76 бутылок пива!
Возьми одну, передай мне
75 бутылок пива на стене
''')


def test_25_verse():
    b = Bottles()
    verse = 75
    expect(b.verse(verse)).to_equal('''75 бутылок пива на стене
75 бутылок пива!
Возьми одну, передай мне
74 бутылки пива на стене
''')


def test_26_verse():
    b = Bottles()
    verse = 74
    expect(b.verse(verse)).to_equal('''74 бутылки пива на стене
74 бутылки пива!
Возьми одну, передай мне
73 бутылки пива на стене
''')


def test_27_verse():
    b = Bottles()
    verse = 73
    expect(b.verse(verse)).to_equal('''73 бутылки пива на стене
73 бутылки пива!
Возьми одну, передай мне
72 бутылки пива на стене
''')


def test_28_verse():
    b = Bottles()
    verse = 72
    expect(b.verse(verse)).to_equal('''72 бутылки пива на стене
72 бутылки пива!
Возьми одну, передай мне
71 бутылка пива на стене
''')


def test_29_verse():
    b = Bottles()
    verse = 71
    expect(b.verse(verse)).to_equal('''71 бутылка пива на стене
71 бутылка пива!
Возьми одну, передай мне
70 бутылок пива на стене
''')


def test_30_verse():
    b = Bottles()
    verse = 70
    expect(b.verse(verse)).to_equal('''70 бутылок пива на стене
70 бутылок пива!
Возьми одну, передай мне
69 бутылок пива на стене
''')


def test_31_verse():
    b = Bottles()
    verse = 69
    expect(b.verse(verse)).to_equal('''69 бутылок пива на стене
69 бутылок пива!
Возьми одну, передай мне
68 бутылок пива на стене
''')


def test_32_verse():
    b = Bottles()
    verse = 68
    expect(b.verse(verse)).to_equal('''68 бутылок пива на стене
68 бутылок пива!
Возьми одну, передай мне
67 бутылок пива на стене
''')


def test_33_verse():
    b = Bottles()
    verse = 67
    expect(b.verse(verse)).to_equal('''67 бутылок пива на стене
67 бутылок пива!
Возьми одну, передай мне
66 бутылок пива на стене
''')


def test_34_verse():
    b = Bottles()
    verse = 66
    expect(b.verse(verse)).to_equal('''66 бутылок пива на стене
66 бутылок пива!
Возьми одну, передай мне
65 бутылок пива на стене
''')


def test_35_verse():
    b = Bottles()
    verse = 65
    expect(b.verse(verse)).to_equal('''65 бутылок пива на стене
65 бутылок пива!
Возьми одну, передай мне
64 бутылки пива на стене
''')


def test_36_verse():
    b = Bottles()
    verse = 64
    expect(b.verse(verse)).to_equal('''64 бутылки пива на стене
64 бутылки пива!
Возьми одну, передай мне
63 бутылки пива на стене
''')


def test_37_verse():
    b = Bottles()
    verse = 63
    expect(b.verse(verse)).to_equal('''63 бутылки пива на стене
63 бутылки пива!
Возьми одну, передай мне
62 бутылки пива на стене
''')


def test_38_verse():
    b = Bottles()
    verse = 62
    expect(b.verse(verse)).to_equal('''62 бутылки пива на стене
62 бутылки пива!
Возьми одну, передай мне
61 бутылка пива на стене
''')


def test_39_verse():
    b = Bottles()
    verse = 61
    expect(b.verse(verse)).to_equal('''61 бутылка пива на стене
61 бутылка пива!
Возьми одну, передай мне
60 бутылок пива на стене
''')


def test_40_verse():
    b = Bottles()
    verse = 60
    expect(b.verse(verse)).to_equal('''60 бутылок пива на стене
60 бутылок пива!
Возьми одну, передай мне
59 бутылок пива на стене
''')


def test_41_verse():
    b = Bottles()
    verse = 59
    expect(b.verse(verse)).to_equal('''59 бутылок пива на стене
59 бутылок пива!
Возьми одну, передай мне
58 бутылок пива на стене
''')


def test_42_verse():
    b = Bottles()
    verse = 58
    expect(b.verse(verse)).to_equal('''58 бутылок пива на стене
58 бутылок пива!
Возьми одну, передай мне
57 бутылок пива на стене
''')


def test_43_verse():
    b = Bottles()
    verse = 57
    expect(b.verse(verse)).to_equal('''57 бутылок пива на стене
57 бутылок пива!
Возьми одну, передай мне
56 бутылок пива на стене
''')


def test_44_verse():
    b = Bottles()
    verse = 56
    expect(b.verse(verse)).to_equal('''56 бутылок пива на стене
56 бутылок пива!
Возьми одну, передай мне
55 бутылок пива на стене
''')


def test_45_verse():
    b = Bottles()
    verse = 55
    expect(b.verse(verse)).to_equal('''55 бутылок пива на стене
55 бутылок пива!
Возьми одну, передай мне
54 бутылки пива на стене
''')


def test_46_verse():
    b = Bottles()
    verse = 54
    expect(b.verse(verse)).to_equal('''54 бутылки пива на стене
54 бутылки пива!
Возьми одну, передай мне
53 бутылки пива на стене
''')


def test_47_verse():
    b = Bottles()
    verse = 53
    expect(b.verse(verse)).to_equal('''53 бутылки пива на стене
53 бутылки пива!
Возьми одну, передай мне
52 бутылки пива на стене
''')


def test_48_verse():
    b = Bottles()
    verse = 52
    expect(b.verse(verse)).to_equal('''52 бутылки пива на стене
52 бутылки пива!
Возьми одну, передай мне
51 бутылка пива на стене
''')


def test_49_verse():
    b = Bottles()
    verse = 51
    expect(b.verse(verse)).to_equal('''51 бутылка пива на стене
51 бутылка пива!
Возьми одну, передай мне
50 бутылок пива на стене
''')


def test_50_verse():
    b = Bottles()
    verse = 50
    expect(b.verse(verse)).to_equal('''50 бутылок пива на стене
50 бутылок пива!
Возьми одну, передай мне
49 бутылок пива на стене
''')


def test_51_verse():
    b = Bottles()
    verse = 49
    expect(b.verse(verse)).to_equal('''49 бутылок пива на стене
49 бутылок пива!
Возьми одну, передай мне
48 бутылок пива на стене
''')


def test_52_verse():
    b = Bottles()
    verse = 48
    expect(b.verse(verse)).to_equal('''48 бутылок пива на стене
48 бутылок пива!
Возьми одну, передай мне
47 бутылок пива на стене
''')


def test_53_verse():
    b = Bottles()
    verse = 47
    expect(b.verse(verse)).to_equal('''47 бутылок пива на стене
47 бутылок пива!
Возьми одну, передай мне
46 бутылок пива на стене
''')


def test_54_verse():
    b = Bottles()
    verse = 46
    expect(b.verse(verse)).to_equal('''46 бутылок пива на стене
46 бутылок пива!
Возьми одну, передай мне
45 бутылок пива на стене
''')


def test_55_verse():
    b = Bottles()
    verse = 45
    expect(b.verse(verse)).to_equal('''45 бутылок пива на стене
45 бутылок пива!
Возьми одну, передай мне
44 бутылки пива на стене
''')


def test_56_verse():
    b = Bottles()
    verse = 44
    expect(b.verse(verse)).to_equal('''44 бутылки пива на стене
44 бутылки пива!
Возьми одну, передай мне
43 бутылки пива на стене
''')


def test_57_verse():
    b = Bottles()
    verse = 43
    expect(b.verse(verse)).to_equal('''43 бутылки пива на стене
43 бутылки пива!
Возьми одну, передай мне
42 бутылки пива на стене
''')


def test_58_verse():
    b = Bottles()
    verse = 42
    expect(b.verse(verse)).to_equal('''42 бутылки пива на стене
42 бутылки пива!
Возьми одну, передай мне
41 бутылка пива на стене
''')


def test_59_verse():
    b = Bottles()
    verse = 41
    expect(b.verse(verse)).to_equal('''41 бутылка пива на стене
41 бутылка пива!
Возьми одну, передай мне
40 бутылок пива на стене
''')


def test_60_verse():
    b = Bottles()
    verse = 40
    expect(b.verse(verse)).to_equal('''40 бутылок пива на стене
40 бутылок пива!
Возьми одну, передай мне
39 бутылок пива на стене
''')


def test_61_verse():
    b = Bottles()
    verse = 39
    expect(b.verse(verse)).to_equal('''39 бутылок пива на стене
39 бутылок пива!
Возьми одну, передай мне
38 бутылок пива на стене
''')


def test_62_verse():
    b = Bottles()
    verse = 38
    expect(b.verse(verse)).to_equal('''38 бутылок пива на стене
38 бутылок пива!
Возьми одну, передай мне
37 бутылок пива на стене
''')


def test_63_verse():
    b = Bottles()
    verse = 37
    expect(b.verse(verse)).to_equal('''37 бутылок пива на стене
37 бутылок пива!
Возьми одну, передай мне
36 бутылок пива на стене
''')


def test_64_verse():
    b = Bottles()
    verse = 36
    expect(b.verse(verse)).to_equal('''36 бутылок пива на стене
36 бутылок пива!
Возьми одну, передай мне
35 бутылок пива на стене
''')


def test_65_verse():
    b = Bottles()
    verse = 35
    expect(b.verse(verse)).to_equal('''35 бутылок пива на стене
35 бутылок пива!
Возьми одну, передай мне
34 бутылки пива на стене
''')


def test_66_verse():
    b = Bottles()
    verse = 34
    expect(b.verse(verse)).to_equal('''34 бутылки пива на стене
34 бутылки пива!
Возьми одну, передай мне
33 бутылки пива на стене
''')


def test_67_verse():
    b = Bottles()
    verse = 33
    expect(b.verse(verse)).to_equal('''33 бутылки пива на стене
33 бутылки пива!
Возьми одну, передай мне
32 бутылки пива на стене
''')


def test_68_verse():
    b = Bottles()
    verse = 32
    expect(b.verse(verse)).to_equal('''32 бутылки пива на стене
32 бутылки пива!
Возьми одну, передай мне
31 бутылка пива на стене
''')


def test_69_verse():
    b = Bottles()
    verse = 31
    expect(b.verse(verse)).to_equal('''31 бутылка пива на стене
31 бутылка пива!
Возьми одну, передай мне
30 бутылок пива на стене
''')


def test_70_verse():
    b = Bottles()
    verse = 30
    expect(b.verse(verse)).to_equal('''30 бутылок пива на стене
30 бутылок пива!
Возьми одну, передай мне
29 бутылок пива на стене
''')


def test_71_verse():
    b = Bottles()
    verse = 29
    expect(b.verse(verse)).to_equal('''29 бутылок пива на стене
29 бутылок пива!
Возьми одну, передай мне
28 бутылок пива на стене
''')


def test_72_verse():
    b = Bottles()
    verse = 28
    expect(b.verse(verse)).to_equal('''28 бутылок пива на стене
28 бутылок пива!
Возьми одну, передай мне
27 бутылок пива на стене
''')


def test_73_verse():
    b = Bottles()
    verse = 27
    expect(b.verse(verse)).to_equal('''27 бутылок пива на стене
27 бутылок пива!
Возьми одну, передай мне
26 бутылок пива на стене
''')


def test_74_verse():
    b = Bottles()
    verse = 26
    expect(b.verse(verse)).to_equal('''26 бутылок пива на стене
26 бутылок пива!
Возьми одну, передай мне
25 бутылок пива на стене
''')


def test_75_verse():
    b = Bottles()
    verse = 25
    expect(b.verse(verse)).to_equal('''25 бутылок пива на стене
25 бутылок пива!
Возьми одну, передай мне
24 бутылки пива на стене
''')


def test_76_verse():
    b = Bottles()
    verse = 24
    expect(b.verse(verse)).to_equal('''24 бутылки пива на стене
24 бутылки пива!
Возьми одну, передай мне
23 бутылки пива на стене
''')


def test_77_verse():
    b = Bottles()
    verse = 23
    expect(b.verse(verse)).to_equal('''23 бутылки пива на стене
23 бутылки пива!
Возьми одну, передай мне
22 бутылки пива на стене
''')


def test_78_verse():
    b = Bottles()
    verse = 22
    expect(b.verse(verse)).to_equal('''22 бутылки пива на стене
22 бутылки пива!
Возьми одну, передай мне
21 бутылка пива на стене
''')


def test_79_verse():
    b = Bottles()
    verse = 21
    expect(b.verse(verse)).to_equal('''21 бутылка пива на стене
21 бутылка пива!
Возьми одну, передай мне
20 бутылок пива на стене
''')


def test_80_verse():
    b = Bottles()
    verse = 20
    expect(b.verse(verse)).to_equal('''20 бутылок пива на стене
20 бутылок пива!
Возьми одну, передай мне
19 бутылок пива на стене
''')


def test_81_verse():
    b = Bottles()
    verse = 19
    expect(b.verse(verse)).to_equal('''19 бутылок пива на стене
19 бутылок пива!
Возьми одну, передай мне
18 бутылок пива на стене
''')


def test_82_verse():
    b = Bottles()
    verse = 18
    expect(b.verse(verse)).to_equal('''18 бутылок пива на стене
18 бутылок пива!
Возьми одну, передай мне
17 бутылок пива на стене
''')


def test_83_verse():
    b = Bottles()
    verse = 17
    expect(b.verse(verse)).to_equal('''17 бутылок пива на стене
17 бутылок пива!
Возьми одну, передай мне
16 бутылок пива на стене
''')


def test_84_verse():
    b = Bottles()
    verse = 16
    expect(b.verse(verse)).to_equal('''16 бутылок пива на стене
16 бутылок пива!
Возьми одну, передай мне
15 бутылок пива на стене
''')


def test_85_verse():
    b = Bottles()
    verse = 15
    expect(b.verse(verse)).to_equal('''15 бутылок пива на стене
15 бутылок пива!
Возьми одну, передай мне
14 бутылок пива на стене
''')


def test_86_verse():
    b = Bottles()
    verse = 14
    expect(b.verse(verse)).to_equal('''14 бутылок пива на стене
14 бутылок пива!
Возьми одну, передай мне
13 бутылок пива на стене
''')


def test_87_verse():
    b = Bottles()
    verse = 13
    expect(b.verse(verse)).to_equal('''13 бутылок пива на стене
13 бутылок пива!
Возьми одну, передай мне
12 бутылок пива на стене
''')


def test_88_verse():
    b = Bottles()
    verse = 12
    expect(b.verse(verse)).to_equal('''12 бутылок пива на стене
12 бутылок пива!
Возьми одну, передай мне
11 бутылок пива на стене
''')


def test_89_verse():
    b = Bottles()
    verse = 11
    expect(b.verse(verse)).to_equal('''11 бутылок пива на стене
11 бутылок пива!
Возьми одну, передай мне
10 бутылок пива на стене
''')


def test_90_verse():
    b = Bottles()
    verse = 10
    expect(b.verse(verse)).to_equal('''10 бутылок пива на стене
10 бутылок пива!
Возьми одну, передай мне
9 бутылок пива на стене
''')


def test_91_verse():
    b = Bottles()
    verse = 9
    expect(b.verse(verse)).to_equal('''9 бутылок пива на стене
9 бутылок пива!
Возьми одну, передай мне
8 бутылок пива на стене
''')


def test_92_verse():
    b = Bottles()
    verse = 8
    expect(b.verse(verse)).to_equal('''8 бутылок пива на стене
8 бутылок пива!
Возьми одну, передай мне
7 бутылок пива на стене
''')


def test_93_verse():
    b = Bottles()
    verse = 7
    expect(b.verse(verse)).to_equal('''7 бутылок пива на стене
7 бутылок пива!
Возьми одну, передай мне
6 бутылок пива на стене
''')


def test_94_verse():
    b = Bottles()
    verse = 6
    expect(b.verse(verse)).to_equal('''6 бутылок пива на стене
6 бутылок пива!
Возьми одну, передай мне
5 бутылок пива на стене
''')


def test_95_verse():
    b = Bottles()
    verse = 5
    expect(b.verse(verse)).to_equal('''5 бутылок пива на стене
5 бутылок пива!
Возьми одну, передай мне
4 бутылки пива на стене
''')


def test_96_verse():
    b = Bottles()
    verse = 4
    expect(b.verse(verse)).to_equal('''4 бутылки пива на стене
4 бутылки пива!
Возьми одну, передай мне
3 бутылки пива на стене
''')


def test_97_verse():
    b = Bottles()
    verse = 3
    expect(b.verse(verse)).to_equal('''3 бутылки пива на стене
3 бутылки пива!
Возьми одну, передай мне
2 бутылки пива на стене
''')


def test_98_verse():
    b = Bottles()
    verse = 2
    expect(b.verse(verse)).to_equal('''2 бутылки пива на стене
2 бутылки пива!
Возьми одну, передай мне
1 бутылка пива на стене
''')


def test_99_verse():
    b = Bottles()
    verse = 1
    expect(b.verse(verse)).to_equal('''1 бутылка пива на стене
1 бутылка пива!
Возьми одну, передай мне
Нет бутылок пива на стене
''')
