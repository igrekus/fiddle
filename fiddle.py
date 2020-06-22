# -*- coding: utf-8 -*-
"""
ТЗ:

Фрилансеру Василию пришёл заказ от книжного магазина "Хорнс-н-Хуверс" на доработку их системы складского учёта. Суть такова...

    - товары теряют актуальность по мере приближения срока годности
    - у всех позиций есть свойство sell_in, описывающее, сколько дней отсталось до истечения срока годности
    - у всех позиций есть свойство quality, описывающее ценность товара
    - по истечению суток, система производит автоматический переучёт срока годности и показателя качества товара для всех позиций на складе

Система достаточно простая, но есть пара ньюансов:

    - по истечению срока годности, параметр quality уменьшается вдвое быстрее
    - quality может быть нулевым, но не может быть отрицательным
    - "Н. Вирт, Алгооитмы и Структуры Данных" с возрастом только хорошеет
    - quality не может превышать 50
    - "Марк Лутц, Изучаем Python, 3й том" - легендартный артефакт, не терят в качестве и продавать его нельзя
    - quality 3го тома лутца равно 80 и никогда не меняется
    - "Скидочный купон на Курс", также, как книга Вирта набирает ценность по мере истечения срока годности:
        - на 1, если осталось больше 10 дней
        - за 10 и менее дней до истечения срока ценность увеличивается на 2 в день
        - за 5 и менее дней до истечения срока ценность увеличивается на 3 в день
        - по истечению срока, ценность падает до нуля

Поставщик впарил нам серию книг по фреймворкам, задачей Василия будет внесение доработок в систему:

    - любоая литература со словом "фреймворк" в названии устаревает в 2 раза быстрее

Василий может вносить любые изменения в код метода update_quality(), главное, чтобы существующий контракт не менялся.
Класс Item трогать нельзя, так как его код писал психопат, который знает, где Василий живёт.
"""


class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Н. Вирт, Алгооитмы и Структуры Данных" and item.name != "Скидочный купон на Курс":
                if item.quality > 0:
                    if item.name != "Марк Лутц, Изучаем Python, 3й том":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Скидочный купон на Курс":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Марк Лутц, Изучаем Python, 3й том":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Н. Вирт, Алгооитмы и Структуры Данных":
                    if item.name != "Скидочный купон на Курс":
                        if item.quality > 0:
                            if item.name != "Марк Лутц, Изучаем Python, 3й том":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f'{self.name}, {self.sell_in}, {self.quality}'
