def diamond(letter: str, background: str=' ') -> str:
    letters = ''.join(map(chr, range(65, ord(letter) + 1)))

    def half_line(i, l):
        return f'{background * (len(letters) - i - 1)}{l}{background * i}'

    half = [half_line(i, l) + half_line(i, l)[-2::-1] for i, l in enumerate(letters)]
    return '\n'.join(half + half[-2::-1]) + '\n'
