# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass()
class Item:
    name: str = ''
    sell_in: int = 0
    quality: int = 0


@dataclass()
class Tick:
    item: Item

    def tick(self): pass


class NormalTick(Tick):
    def tick(self):
        self.item.sell_in -= 1
        if self.item.quality == 0:
            return
        self.item.quality -= 1
        if self.item.sell_in <= 0:
            self.item.quality -= 1


class KnuthTick(Tick):
    def tick(self):
        self.item.sell_in -= 1
        if self.item.quality >= 50:
            return
        self.item.quality += 1
        if self.item.sell_in <= 0 and self.item.quality < 50:
            self.item.quality += 1


class CouponTick(Tick):
    def tick(self):
        self.item.sell_in -= 1
        if self.item.quality >= 50:
            return
        if self.item.sell_in < 0:
            self.item.quality = 0
            return
        self.item.quality += 1
        if self.item.sell_in < 10:
            self.item.quality += 1
        if self.item.sell_in < 5:
            self.item.quality += 1
        return


class FrameworkTick(Tick):
    def tick(self):
        self.item.sell_in -= 1
        if self.item.quality == 0:
            return
        self.item.quality -= 2
        if self.item.sell_in <= 0:
            self.item.quality -= 2


class BookShop:
    tick_handlers = {
        'Д. Кнут, Искусство программирования': KnuthTick,
        'Марк Лутц, Изучаем Python, 3й том': Tick,
        'Скидочный купон на курс': CouponTick,
        'фреймворк': FrameworkTick
    }

    def __init__(self, items: list):
        self.items: list = items

    def update_quality(self):
        for item in self.items:
            self.tick_handlers.get(
                'фреймворк'
                if 'фреймворк' in item.name.lower()
                else item.name,
                NormalTick
            )(item).tick()
