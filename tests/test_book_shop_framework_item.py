from pyexpect import expect
from fiddle import BookShop, Item


def test_framework_item_day():
    shop = BookShop([Item('Фреймворк Django', sell_in=50, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Фреймворк Django', sell_in=49, quality=48)])


def test_framework_item_zero_quality():
    shop = BookShop([Item('Фреймворк Django', sell_in=50, quality=0)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Фреймворк Django', sell_in=49, quality=0)])


def test_framework_item_zero_sell_in():
    shop = BookShop([Item('Фреймворк Django', sell_in=0, quality=10)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Фреймворк Django', sell_in=-1, quality=6)])


def test_framework_item_zero_sell_in_zero_quality():
    shop = BookShop([Item('Фреймворк Django', sell_in=0, quality=0)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Фреймворк Django', sell_in=-1, quality=0)])
