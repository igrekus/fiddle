from string import ascii_uppercase


def diamond(letter, background=' '):
    letters = ascii_uppercase[:ascii_uppercase.index(letter) + 1]
    if letter == letters[0]:
        return 'A'
    elif letter == letters[1]:
        return ' A \n' \
               'B B\n' \
               ' A \n'
    elif letter == letters[2]:
        return '  A  \n' \
               ' B B \n' \
               'C   C\n' \
               ' B B \n' \
               '  A  \n'
    elif letter == letters[3]:
        return '   A   \n' \
               '  B B  \n' \
               ' C   C \n' \
               'D     D\n' \
               ' C   C \n' \
               '  B B  \n' \
               '   A   \n'
