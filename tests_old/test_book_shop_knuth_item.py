from pyexpect import expect
from book_shop_func_full_lambda import BookShop, Item


def test_knuth_item_before_sell_date():
    shop = BookShop([Item('Д. Кнут, Искусство программирования', sell_in=50, quality=48)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Д. Кнут, Искусство программирования', sell_in=49, quality=49)])


def test_knuth_item_before_sell_date_and_max_quality():
    shop = BookShop([Item('Д. Кнут, Искусство программирования', sell_in=50, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Д. Кнут, Искусство программирования', sell_in=49, quality=50)])


def test_knuth_item_on_sell_date():
    shop = BookShop([Item('Д. Кнут, Искусство программирования', sell_in=0, quality=8)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Д. Кнут, Искусство программирования', sell_in=-1, quality=10)])


def test_knuth_item_on_sell_date_and_near_max_quality():
    shop = BookShop([Item('Д. Кнут, Искусство программирования', sell_in=0, quality=49)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Д. Кнут, Искусство программирования', sell_in=-1, quality=50)])


def test_knuth_item_on_sell_date_and_max_quality():
    shop = BookShop([Item('Д. Кнут, Искусство программирования', sell_in=0, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Д. Кнут, Искусство программирования', sell_in=-1, quality=50)])


def test_knuth_item_after_sell_date():
    shop = BookShop([Item('Д. Кнут, Искусство программирования', sell_in=-1, quality=10)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Д. Кнут, Искусство программирования', sell_in=-2, quality=12)])


def test_knuth_item_after_sell_date_and_near_max_quality():
    shop = BookShop([Item('Д. Кнут, Искусство программирования', sell_in=-1, quality=49)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Д. Кнут, Искусство программирования', sell_in=-2, quality=50)])


def test_knuth_item_after_sell_date_and_max_quality():
    shop = BookShop([Item('Д. Кнут, Искусство программирования', sell_in=-1, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Д. Кнут, Искусство программирования', sell_in=-2, quality=50)])
