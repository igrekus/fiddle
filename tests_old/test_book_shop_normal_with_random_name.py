from pyexpect import expect
from book_shop_func_full_lambda import BookShop, Item


def test_normal_item_before_sell_data():
    shop = BookShop([Item('sdfgasg', sell_in=50, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('sdfgasg', sell_in=49, quality=49)])


def test_normal_on_sell_date():
    shop = BookShop([Item('am6y5e', sell_in=0, quality=10)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('am6y5e', sell_in=-1, quality=8)])


def test_normal_item_after_sell_date():
    shop = BookShop([Item('r,568m', sell_in=-1, quality=10)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('r,568m', sell_in=-2, quality=8)])


def test_normal_item_of_zero_quality():
    shop = BookShop([
        Item('2345uyjhgfd', sell_in=10, quality=0),
        Item('2345uyjhgfd', sell_in=0, quality=0),
        Item('2345uyjhgfd', sell_in=-1, quality=0),
    ])

    shop.update_quality()

    expect(shop.items).to_equal([
        Item('2345uyjhgfd', sell_in=9, quality=0),
        Item('2345uyjhgfd', sell_in=-1, quality=0),
        Item('2345uyjhgfd', sell_in=-2, quality=0),
    ])
