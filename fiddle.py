# -*- coding: utf-8 -*-
"""
ТЗ:

Фрилансер Василий получил от книжного магазина "Зелёный змий" заказ на доработку системы складского учёта. Суть такова...

    - товары теряют ценность по мере приближения указанноего срока реализации товара
    - у всех товаров есть свойство sell_in, показывающее количество дней, оставшееся до окончания срока реализации
    - у всех товаров есть свойство quality, описывающее ценность товара
    - в конце каждого дня, система производит автоматический перерасчёт срока годности и показателя качества для всех товаров на складе

Система достаточно простая, но есть пара ньюансов:

    - по истечению срока продажи, параметр quality уменьшается вдвое быстрее
    - quality не может быть отрицательным, но может быть равным нулю
    - quality не может превышать 50
    - "Д. Кнут, Искусство программирования" с возрастом только хорошеет
    - "Марк Лутц, Изучаем Python, 3й том" - легендартный артефакт, не терят в качестве и продавать его нельзя
    - quality 3го тома Лутца равно 80 и никогда не меняется
    - "Скидочный купон на курс", также как книга Вирта, набирает ценность по мере истечения срока годности:
        - на 1, если осталось больше 10 дней
        - за 10 и менее дней до истечения срока ценность увеличивается на 2 в день
        - за 5 и менее дней до истечения срока ценность увеличивается на 3 в день
        - по истечению срока, ценность падает до нуля

Далее, поставщик впарил магазину серию книг по фреймворкам, и задачей Василия будет внесение следующей доработки в систему:

    - любоая литература со словом "фреймворк" в названии устаревает в 2 раза быстрее

Василий, несмотря на то, что фрилансер, калач уже тёрнтый и поэтому прекрасно понимает, что заказчик обычно не технарь и ТЗ пишет через задницу, поэтому __поведение системы придётся уточнять через анализ существующего кода__.
Василий может вносить __любые__ изменения в код метода update_quality(), главное, чтобы существующий контракт не менялся.
Класс Item __трогать нельзя__, так как его писал психопат, который знает, где Василий живёт.
"""
from dataclasses import dataclass


@dataclass()
class Item:
    name: str = ''
    sell_in: int = 0
    quality: int = 0


class Tick:
    def __init__(self, item: Item):
        self.item: Item = item

    def tick(self):
        pass


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


class LutzTick(Tick):
    pass


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


class BookShop:
    tick_handlers ={
        'Д. Кнут, Искусство программирования': KnuthTick,
        'Марк Лутц, Изучаем Python, 3й том': LutzTick,
        'Скидочный купон на курс': CouponTick
    }

    def __init__(self, items: list):
        self.items: list = items

    def update_quality(self):
        for item in self.items:
            self.tick_handlers.get(item.name, NormalTick)(item).tick()
