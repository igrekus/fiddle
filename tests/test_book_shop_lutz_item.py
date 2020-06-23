from pyexpect import expect
from fiddle import BookShop, Item


def test_lutz_item_day():
    shop = BookShop([Item('Марк Лутц, Изучаем Python, 3й том', sell_in=50, quality=80)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Марк Лутц, Изучаем Python, 3й том', sell_in=50, quality=80)])


def test_lutz_item_zero_sell_in():
    shop = BookShop([Item('Марк Лутц, Изучаем Python, 3й том', sell_in=0, quality=80)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Марк Лутц, Изучаем Python, 3й том', sell_in=0, quality=80)])


def test_lutz_item_negative_sell_in():
    shop = BookShop([Item('Марк Лутц, Изучаем Python, 3й том', sell_in=-1, quality=80)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Марк Лутц, Изучаем Python, 3й том', sell_in=-1, quality=80)])
