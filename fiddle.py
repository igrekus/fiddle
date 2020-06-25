# -*- coding: utf-8 -*-
"""ТЗ:

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

Василий, будучи опытным фрилансером, прекрасно понимает, что ТЗ заказчик пишет всегда через задницу, поэтому __поведение системы придётся уточнять через анализ существующего кода__.
Василий может вносить __любые__ изменения в код метода update_quality(), главное, чтобы существующий контракт не менялся.
Класс Item __трогать нельзя__, так как его писал психопат, который знает, где Василий живёт. С дргой стороны, психопат код писать всё-такие умел и Item из БД приходит всегда валидный.
"""
from dataclasses import dataclass


@dataclass()
class Item:
    name: str = ''
    sell_in: int = 0
    quality: int = 0


def _normal_tick(item):
    new_item = Item(item.name, item.sell_in - 1, item.quality)
    if new_item.quality > 0:
        new_item.quality = item.quality - 1 if item.sell_in > 0 else item.quality - 2
    return new_item


def _knuth_tick(item):
    new_item = Item(item.name, item.sell_in - 1, item.quality)
    if new_item.quality < 50:
        new_item.quality += 1
    if new_item.sell_in <= 0 and new_item.quality < 50:
        new_item.quality += 1
    return new_item


def _coupon_tick(item):
    new_item = Item(item.name, item.sell_in - 1, item.quality)
    if new_item.quality < 50:
        new_item.quality += 1
        if new_item.sell_in < 10:
            new_item.quality += 1
        if new_item.sell_in < 5:
            new_item.quality += 1

    if new_item.sell_in < 0:
        new_item.quality = 0
    return new_item


def _framework_tick(item):
    new_item = Item(item.name, item.sell_in - 1, item.quality)
    if new_item.quality > 0:
        new_item.quality = item.quality - 2 if new_item.sell_in > 0 else item.quality - 4
    return new_item


def _pick(item):
    return 'фреймворк' if 'фреймворк' in item.name.lower() else item.name


tick_handlers = {
    'Д. Кнут, Искусство программирования': _knuth_tick,
    'Марк Лутц, Изучаем Python, 3й том': lambda _: _,
    'Скидочный купон на курс': _coupon_tick,
    'фреймворк': _framework_tick
}


class BookShop:
    def __init__(self, items: list):
        self.items: list = items

    def update_quality(self):
        self.items = [tick_handlers.get(_pick(item), _normal_tick)(item) for item in self.items]
