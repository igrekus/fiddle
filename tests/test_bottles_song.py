from pyexpect import expect
# from bottles_oop import song
from bottles_func import song


def test_the_whole_song():
    expected = '''99 бутылок пива на стене, 99 бутылок пива!
Возьми одну, передай мне, 98 бутылок пива на стене.

98 бутылок пива на стене, 98 бутылок пива!
Возьми одну, передай мне, 97 бутылок пива на стене.

97 бутылок пива на стене, 97 бутылок пива!
Возьми одну, передай мне, 96 бутылок пива на стене.

96 бутылок пива на стене, 96 бутылок пива!
Возьми одну, передай мне, 95 бутылок пива на стене.

95 бутылок пива на стене, 95 бутылок пива!
Возьми одну, передай мне, 94 бутылки пива на стене.

94 бутылки пива на стене, 94 бутылки пива!
Возьми одну, передай мне, 93 бутылки пива на стене.

93 бутылки пива на стене, 93 бутылки пива!
Возьми одну, передай мне, 92 бутылки пива на стене.

92 бутылки пива на стене, 92 бутылки пива!
Возьми одну, передай мне, 91 бутылка пива на стене.

91 бутылка пива на стене, 91 бутылка пива!
Возьми одну, передай мне, 90 бутылок пива на стене.

90 бутылок пива на стене, 90 бутылок пива!
Возьми одну, передай мне, 89 бутылок пива на стене.

89 бутылок пива на стене, 89 бутылок пива!
Возьми одну, передай мне, 88 бутылок пива на стене.

88 бутылок пива на стене, 88 бутылок пива!
Возьми одну, передай мне, 87 бутылок пива на стене.

87 бутылок пива на стене, 87 бутылок пива!
Возьми одну, передай мне, 86 бутылок пива на стене.

86 бутылок пива на стене, 86 бутылок пива!
Возьми одну, передай мне, 85 бутылок пива на стене.

85 бутылок пива на стене, 85 бутылок пива!
Возьми одну, передай мне, 84 бутылки пива на стене.

84 бутылки пива на стене, 84 бутылки пива!
Возьми одну, передай мне, 83 бутылки пива на стене.

83 бутылки пива на стене, 83 бутылки пива!
Возьми одну, передай мне, 82 бутылки пива на стене.

82 бутылки пива на стене, 82 бутылки пива!
Возьми одну, передай мне, 81 бутылка пива на стене.

81 бутылка пива на стене, 81 бутылка пива!
Возьми одну, передай мне, 80 бутылок пива на стене.

80 бутылок пива на стене, 80 бутылок пива!
Возьми одну, передай мне, 79 бутылок пива на стене.

79 бутылок пива на стене, 79 бутылок пива!
Возьми одну, передай мне, 78 бутылок пива на стене.

78 бутылок пива на стене, 78 бутылок пива!
Возьми одну, передай мне, 77 бутылок пива на стене.

77 бутылок пива на стене, 77 бутылок пива!
Возьми одну, передай мне, 76 бутылок пива на стене.

76 бутылок пива на стене, 76 бутылок пива!
Возьми одну, передай мне, 75 бутылок пива на стене.

75 бутылок пива на стене, 75 бутылок пива!
Возьми одну, передай мне, 74 бутылки пива на стене.

74 бутылки пива на стене, 74 бутылки пива!
Возьми одну, передай мне, 73 бутылки пива на стене.

73 бутылки пива на стене, 73 бутылки пива!
Возьми одну, передай мне, 72 бутылки пива на стене.

72 бутылки пива на стене, 72 бутылки пива!
Возьми одну, передай мне, 71 бутылка пива на стене.

71 бутылка пива на стене, 71 бутылка пива!
Возьми одну, передай мне, 70 бутылок пива на стене.

70 бутылок пива на стене, 70 бутылок пива!
Возьми одну, передай мне, 69 бутылок пива на стене.

69 бутылок пива на стене, 69 бутылок пива!
Возьми одну, передай мне, 68 бутылок пива на стене.

68 бутылок пива на стене, 68 бутылок пива!
Возьми одну, передай мне, 67 бутылок пива на стене.

67 бутылок пива на стене, 67 бутылок пива!
Возьми одну, передай мне, 66 бутылок пива на стене.

66 бутылок пива на стене, 66 бутылок пива!
Возьми одну, передай мне, 65 бутылок пива на стене.

65 бутылок пива на стене, 65 бутылок пива!
Возьми одну, передай мне, 64 бутылки пива на стене.

64 бутылки пива на стене, 64 бутылки пива!
Возьми одну, передай мне, 63 бутылки пива на стене.

63 бутылки пива на стене, 63 бутылки пива!
Возьми одну, передай мне, 62 бутылки пива на стене.

62 бутылки пива на стене, 62 бутылки пива!
Возьми одну, передай мне, 61 бутылка пива на стене.

61 бутылка пива на стене, 61 бутылка пива!
Возьми одну, передай мне, 60 бутылок пива на стене.

60 бутылок пива на стене, 60 бутылок пива!
Возьми одну, передай мне, 59 бутылок пива на стене.

59 бутылок пива на стене, 59 бутылок пива!
Возьми одну, передай мне, 58 бутылок пива на стене.

58 бутылок пива на стене, 58 бутылок пива!
Возьми одну, передай мне, 57 бутылок пива на стене.

57 бутылок пива на стене, 57 бутылок пива!
Возьми одну, передай мне, 56 бутылок пива на стене.

56 бутылок пива на стене, 56 бутылок пива!
Возьми одну, передай мне, 55 бутылок пива на стене.

55 бутылок пива на стене, 55 бутылок пива!
Возьми одну, передай мне, 54 бутылки пива на стене.

54 бутылки пива на стене, 54 бутылки пива!
Возьми одну, передай мне, 53 бутылки пива на стене.

53 бутылки пива на стене, 53 бутылки пива!
Возьми одну, передай мне, 52 бутылки пива на стене.

52 бутылки пива на стене, 52 бутылки пива!
Возьми одну, передай мне, 51 бутылка пива на стене.

51 бутылка пива на стене, 51 бутылка пива!
Возьми одну, передай мне, 50 бутылок пива на стене.

50 бутылок пива на стене, 50 бутылок пива!
Возьми одну, передай мне, 49 бутылок пива на стене.

49 бутылок пива на стене, 49 бутылок пива!
Возьми одну, передай мне, 48 бутылок пива на стене.

48 бутылок пива на стене, 48 бутылок пива!
Возьми одну, передай мне, 47 бутылок пива на стене.

47 бутылок пива на стене, 47 бутылок пива!
Возьми одну, передай мне, 46 бутылок пива на стене.

46 бутылок пива на стене, 46 бутылок пива!
Возьми одну, передай мне, 45 бутылок пива на стене.

45 бутылок пива на стене, 45 бутылок пива!
Возьми одну, передай мне, 44 бутылки пива на стене.

44 бутылки пива на стене, 44 бутылки пива!
Возьми одну, передай мне, 43 бутылки пива на стене.

43 бутылки пива на стене, 43 бутылки пива!
Возьми одну, передай мне, 42 бутылки пива на стене.

42 бутылки пива на стене, 42 бутылки пива!
Возьми одну, передай мне, 41 бутылка пива на стене.

41 бутылка пива на стене, 41 бутылка пива!
Возьми одну, передай мне, 40 бутылок пива на стене.

40 бутылок пива на стене, 40 бутылок пива!
Возьми одну, передай мне, 39 бутылок пива на стене.

39 бутылок пива на стене, 39 бутылок пива!
Возьми одну, передай мне, 38 бутылок пива на стене.

38 бутылок пива на стене, 38 бутылок пива!
Возьми одну, передай мне, 37 бутылок пива на стене.

37 бутылок пива на стене, 37 бутылок пива!
Возьми одну, передай мне, 36 бутылок пива на стене.

36 бутылок пива на стене, 36 бутылок пива!
Возьми одну, передай мне, 35 бутылок пива на стене.

35 бутылок пива на стене, 35 бутылок пива!
Возьми одну, передай мне, 34 бутылки пива на стене.

34 бутылки пива на стене, 34 бутылки пива!
Возьми одну, передай мне, 33 бутылки пива на стене.

33 бутылки пива на стене, 33 бутылки пива!
Возьми одну, передай мне, 32 бутылки пива на стене.

32 бутылки пива на стене, 32 бутылки пива!
Возьми одну, передай мне, 31 бутылка пива на стене.

31 бутылка пива на стене, 31 бутылка пива!
Возьми одну, передай мне, 30 бутылок пива на стене.

30 бутылок пива на стене, 30 бутылок пива!
Возьми одну, передай мне, 29 бутылок пива на стене.

29 бутылок пива на стене, 29 бутылок пива!
Возьми одну, передай мне, 28 бутылок пива на стене.

28 бутылок пива на стене, 28 бутылок пива!
Возьми одну, передай мне, 27 бутылок пива на стене.

27 бутылок пива на стене, 27 бутылок пива!
Возьми одну, передай мне, 26 бутылок пива на стене.

26 бутылок пива на стене, 26 бутылок пива!
Возьми одну, передай мне, 25 бутылок пива на стене.

25 бутылок пива на стене, 25 бутылок пива!
Возьми одну, передай мне, 24 бутылки пива на стене.

24 бутылки пива на стене, 24 бутылки пива!
Возьми одну, передай мне, 23 бутылки пива на стене.

23 бутылки пива на стене, 23 бутылки пива!
Возьми одну, передай мне, 22 бутылки пива на стене.

22 бутылки пива на стене, 22 бутылки пива!
Возьми одну, передай мне, 21 бутылка пива на стене.

21 бутылка пива на стене, 21 бутылка пива!
Возьми одну, передай мне, 20 бутылок пива на стене.

20 бутылок пива на стене, 20 бутылок пива!
Возьми одну, передай мне, 19 бутылок пива на стене.

19 бутылок пива на стене, 19 бутылок пива!
Возьми одну, передай мне, 18 бутылок пива на стене.

18 бутылок пива на стене, 18 бутылок пива!
Возьми одну, передай мне, 17 бутылок пива на стене.

17 бутылок пива на стене, 17 бутылок пива!
Возьми одну, передай мне, 16 бутылок пива на стене.

16 бутылок пива на стене, 16 бутылок пива!
Возьми одну, передай мне, 15 бутылок пива на стене.

15 бутылок пива на стене, 15 бутылок пива!
Возьми одну, передай мне, 14 бутылок пива на стене.

14 бутылок пива на стене, 14 бутылок пива!
Возьми одну, передай мне, 13 бутылок пива на стене.

13 бутылок пива на стене, 13 бутылок пива!
Возьми одну, передай мне, 12 бутылок пива на стене.

12 бутылок пива на стене, 12 бутылок пива!
Возьми одну, передай мне, 11 бутылок пива на стене.

11 бутылок пива на стене, 11 бутылок пива!
Возьми одну, передай мне, 10 бутылок пива на стене.

10 бутылок пива на стене, 10 бутылок пива!
Возьми одну, передай мне, 9 бутылок пива на стене.

9 бутылок пива на стене, 9 бутылок пива!
Возьми одну, передай мне, 8 бутылок пива на стене.

8 бутылок пива на стене, 8 бутылок пива!
Возьми одну, передай мне, 7 бутылок пива на стене.

7 бутылок пива на стене, 7 бутылок пива!
Возьми одну, передай мне, 6 бутылок пива на стене.

6 бутылок пива на стене, 6 бутылок пива!
Возьми одну, передай мне, 5 бутылок пива на стене.

5 бутылок пива на стене, 5 бутылок пива!
Возьми одну, передай мне, 4 бутылки пива на стене.

4 бутылки пива на стене, 4 бутылки пива!
Возьми одну, передай мне, 3 бутылки пива на стене.

3 бутылки пива на стене, 3 бутылки пива!
Возьми одну, передай мне, 2 бутылки пива на стене.

2 бутылки пива на стене, 2 бутылки пива!
Возьми одну, передай мне, последняя бутылка пива на стене.

Последняя бутылка пива на стене, последняя бутылка пива!
Возьми её, передай мне, нет бутылок пива на стене.

Нет бутылок пива на стене, нет бутылок пива!
Сходи в магазин, купи ещё, 99 бутылок пива на стене.
'''
    expect(song()).to_equal(expected)
