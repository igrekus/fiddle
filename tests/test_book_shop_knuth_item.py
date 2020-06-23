from pyexpect import expect
from fiddle import BookShop, Item


def test_knuth_item_day():
    shop = BookShop([Item('Д. Кнут, Искусство программирования', sell_in=50, quality=48)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Д. Кнут, Искусство программирования', sell_in=49, quality=49)])


def test_knuth_item_max_quality_day():
    shop = BookShop([Item('Д. Кнут, Искусство программирования', sell_in=1, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Д. Кнут, Искусство программирования', sell_in=0, quality=50)])


def test_knuth_item_zero_quality():
    shop = BookShop([Item('Д. Кнут, Искусство программирования', sell_in=10, quality=0)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Д. Кнут, Искусство программирования', sell_in=9, quality=1)])


def test_knuth_item_zero_sell_in():
    shop = BookShop([Item('Д. Кнут, Искусство программирования', sell_in=0, quality=10)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Д. Кнут, Искусство программирования', sell_in=-1, quality=12)])


def test_knuth_item_zero_sell_in_up_to_max_quality():
    shop = BookShop([Item('Д. Кнут, Искусство программирования', sell_in=0, quality=48)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Д. Кнут, Искусство программирования', sell_in=-1, quality=50)])


def test_knuth_item_zero_sell_in_max_quality():
    shop = BookShop([Item('Д. Кнут, Искусство программирования', sell_in=0, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Д. Кнут, Искусство программирования', sell_in=-1, quality=50)])


def test_knuth_item_zero_sell_in_zero_quality():
    shop = BookShop([Item('Д. Кнут, Искусство программирования', sell_in=0, quality=0)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Д. Кнут, Искусство программирования', sell_in=-1, quality=2)])
