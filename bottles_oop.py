from dataclasses import dataclass, field
from functools import singledispatchmethod


def _default_field(obj):
    return field(default_factory=lambda: obj)


@dataclass
class Pronoun:
    num: int
    values: dict = _default_field({1: 'её'})
    def __str__(self): return self.values.get(self.num, 'одну')


@dataclass
class Action:
    num: int
    values: dict = _default_field({0: 'Сходи в магазин, купи ещё'})
    def __str__(self): return self.values.get(self.num, f'Возьми {Pronoun(self.num)}, передай мне')


@dataclass
class Quantity:
    num: int
    values: dict = _default_field({0: 'нет', 1: 'последняя', -1: '99'})
    def __str__(self): return self.values.get(self.num, f'{self.num}')


@dataclass
class Container:
    num: int
    values: dict = _default_field({
        **dict.fromkeys([1] + list(range(21, 92, 10)), 'бутылка'),
        **dict.fromkeys([o + 10 * int(d)
                         for o, d in
                         zip([2, 3, 4] * 9, [i for i in '023456789' for _ in 'rep'])],
                        'бутылки')
    })
    def __str__(self): return self.values.get(self.num, f'бутылок')


class Song:
    @singledispatchmethod
    def __getitem__(self, item: slice):
        return '\n'.join(self[n] for n in range(item.start, item.stop - 1, -1)).strip()

    @__getitem__.register
    def _(self, item: int):
        return (f'{f"{Quantity(item)}".capitalize()} {Container(item)} пива на стене, '
                f'{Quantity(item)} {Container(item)} пива!\n'
                f'{Action(item)}, '
                f'{Quantity(item - 1)} {Container(item - 1)} пива на стене.\n')

    def __str__(self):
        return self[99:0]


def song() -> str:
    return str(Song())


def verses(upper: int, lower: int) -> str:
    return Song()[upper:lower]
