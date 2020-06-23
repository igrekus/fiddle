import pytest

from pyexpect import expect
from fiddle import BookShop, Item


@pytest.mark.xfail(reason='not implemented')
def test_framework_item_before_sell_date():
    shop = BookShop([Item('Фреймворк Django', sell_in=50, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Фреймворк Django', sell_in=49, quality=48)])


@pytest.mark.xfail(reason='not implemented')
def test_framework_item_before_sell_date_min_quality():
    shop = BookShop([Item('Фреймворк Django', sell_in=50, quality=0)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Фреймворк Django', sell_in=49, quality=0)])


@pytest.mark.xfail(reason='not implemented')
def test_framework_item_on_sell_date():
    shop = BookShop([Item('Фреймворк Django', sell_in=0, quality=10)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Фреймворк Django', sell_in=-1, quality=6)])


@pytest.mark.xfail(reason='not implemented')
def test_framework_item_on_sell_date_min_quality():
    shop = BookShop([Item('Фреймворк Django', sell_in=0, quality=0)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Фреймворк Django', sell_in=-1, quality=0)])


@pytest.mark.xfail(reason='not implemented')
def test_framework_item_after_sell_date():
    shop = BookShop([Item('Фреймворк Django', sell_in=-1, quality=10)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Фреймворк Django', sell_in=-2, quality=6)])


@pytest.mark.xfail(reason='not implemented')
def test_framework_item_after_sell_date_min_quality():
    shop = BookShop([Item('Фреймворк Django', sell_in=-1, quality=0)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Фреймворк Django', sell_in=-2, quality=0)])
