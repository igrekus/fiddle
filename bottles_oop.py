class Bottles:
    def verse(self, num):
        return (
            f'{self.quantity(num).capitalize()} {self.container(num)} пива на стене, '
            f'{self.quantity(num)} {self.container(num)} пива!\n'
            f'{self.action(num)}, '
            f'{self.quantity(num - 1)} {self.container(num - 1)} пива на стене.\n')

    def action(self, num):
        if num == 0:
            return 'Сходи в магазин, купи ещё'
        return f'Возьми {self.pronoun(num)}, передай мне'

    def quantity(self, num):
        if num == 0:
            return 'нет'
        elif num == 1:
            return 'последняя'
        elif num == -1:
            return '99'
        return f'{num}'

    def pronoun(self, num):
        if num == 1:
            return 'её'
        return 'одну'

    def container(self, num):
        if num in (1, 21, 31, 41, 51, 61, 71, 81, 91):
            return 'бутылка'
        elif num in (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53,
                     54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94):
            return 'бутылки'
        return 'бутылок'

    def verses(self, upper, lower):
        return '\n'.join(self.verse(num) for num in reversed(range(lower, upper + 1))).strip()

    @property
    def song(self):
        return self.verses(99, 0)


bottles = Bottles()


def song() -> str:
    return bottles.song


def verses(upper: int, lower: int) -> str:
    return bottles.verses(upper, lower)
