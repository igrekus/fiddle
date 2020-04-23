class Bottles:
    actions = {0: 'Сходи в магазин, купи ещё'}
    quantities = {0: 'нет', -1: '99'}
    pronouns = {1: 'её'}
    containers = {
        **dict.fromkeys([1] + list(range(21, 92, 10)), 'бутылка'),
        **dict.fromkeys(
            [o + 10*int(d) for o, d in zip(
                [2, 3, 4]*10,
                [i for i in '023456789' for _ in 'rep'])],
            'бутылки'
        )
    }

    def verse(self, num):
        return (
            f'{self.quantity(num).capitalize()} {self.container(num)} пива на стене, '
            f'{self.quantity(num)} {self.container(num)} пива!\n'
            f'{self.action(num)}, '
            f'{self.quantity(num - 1)} {self.container(num - 1)} пива на стене\n'
        )

    def action(self, num):
        return self.actions.get(num, f'Возьми {self.pronoun(num)}, передай мне')

    def quantity(self, num):
        return self.quantities.get(num, f'{num}')

    def pronoun(self, num):
        return self.pronouns.get(num, 'одну')

    def container(self, num):
        return self.containers.get(num, 'бутылок')

    def verses(self, upper, lower):
        return '\n'.join(filter(bool, [self.verse(num) for num in reversed(range(lower, upper + 1))]))

    @property
    def song(self):
        return self.verses(99, 0)
