from pyexpect import expect
from fiddle import BookShop, Item


def test_lutz_before_sell_date():
    shop = BookShop([Item('Марк Лутц, Изучаем Python, 3й том', sell_in=50, quality=80)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Марк Лутц, Изучаем Python, 3й том', sell_in=50, quality=80)])


def test_lutz_item_on_sell_date():
    shop = BookShop([Item('Марк Лутц, Изучаем Python, 3й том', sell_in=0, quality=80)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Марк Лутц, Изучаем Python, 3й том', sell_in=0, quality=80)])


def test_lutz_item_after_sell_date():
    shop = BookShop([Item('Марк Лутц, Изучаем Python, 3й том', sell_in=-1, quality=80)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Марк Лутц, Изучаем Python, 3й том', sell_in=-1, quality=80)])
