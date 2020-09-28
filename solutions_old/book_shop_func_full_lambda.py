# -*- coding: utf-8 -*-
from dataclasses import dataclass
from functools import reduce


__all__ = [
    'BookShop',
    'Item'
]


@dataclass()
class Item:
    name: str = ''
    sell_in: int = 0
    quality: int = 0


def _tick_normal(item):
    item.sell_in -= 1
    if item.quality == 0:
        return
    item.quality -= 1
    if item.sell_in <= 0:
        item.quality -= 1


def _tick_knuth(item):
    item.sell_in -= 1
    if item.quality >= 50:
        return
    item.quality += 1
    if item.sell_in <= 0 and item.quality < 50:
        item.quality += 1


def _tick_coupon(item):
    item.sell_in -= 1
    if item.quality >= 50:
        return
    if item.sell_in < 0:
        item.quality = 0
        return
    item.quality += 1
    if item.sell_in < 10:
        item.quality += 1
    if item.sell_in < 5:
        item.quality += 1


def _tick_framework(item):
    item.sell_in -= 1
    if item.quality == 0:
        return
    item.quality -= 2
    if item.sell_in <= 0:
        item.quality -= 2


_id = lambda x: x
_rpartial = lambda f, *args: lambda *a: f(*(a + args))
_compose = lambda *fs: reduce(lambda f, g: lambda *args: f(g(*args)), fs, _id)

_select = lambda item: 'фреймворк' if 'фреймворк' in item.name.lower() else item.name
_get = {
    'Д. Кнут, Искусство программирования': _tick_knuth,
    'Марк Лутц, Изучаем Python, 3й том': _id,
    'Скидочный купон на курс': _tick_coupon,
    'фреймворк': _tick_framework
}.get

_update = _compose(
    _rpartial(_get, _tick_normal),
    _select
)


class BookShop:
    def __init__(self, items: list):
        self.items: list = items

    def update_quality(self):
        for item in self.items:
            _update(item)(item)
