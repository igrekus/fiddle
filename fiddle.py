def diamond(letter: str, background: str=' '):
    ls = ''.join(chr(c) for c in range(ord('A'), ord(letter) + 1))

    def _quarter(i, l):
        return f'{background * (len(ls) - i - 1)}{l}{background * i}'

    half = [_quarter(i, l) + _mirror(_quarter(i, l)) for i, l in enumerate(ls)]
    return '\n'.join(half + _mirror(half)) + '\n'


def _mirror(seq):
    return seq[-2::-1]
