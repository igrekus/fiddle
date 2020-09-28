class Diamond:
    def __init__(self, letter='A', background=' '):
        self._letters = ''.join(map(chr, range(65, ord(letter) + 1)))
        self._bg = background

    def __str__(self):
        return '\n'.join(self._half_diamond() + self._half_diamond()[-2::-1]) + '\n'

    def _half_diamond(self):
        return [self._half_line(i, l) + self._half_line(i, l)[-2::-1] for i, l in enumerate(self._letters)]

    def _half_line(self, i, l):
        return f'{self._bg * (len(self._letters) - i - 1)}{l}{self._bg * i}'


def diamond(letter: str, background: str=' ') -> str:
    return f'{Diamond(letter, background)}'
