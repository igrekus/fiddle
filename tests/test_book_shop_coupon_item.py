from pyexpect import expect
from book_shop_func import BookShop, Item


def test_coupon_item_item_long_before_sell_date():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=50, quality=48)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=49, quality=49)])


def test_coupon_item_medium_close_to_sell_date_upper_bound():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=10, quality=8)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=9, quality=10)])


def test_coupon_item_medium_close_to_sell_date_upper_bound_and_max_quality():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=10, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=9, quality=50)])


def test_coupon_item_medium_close_to_sell_date_lower_bound():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=6, quality=8)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=5, quality=10)])


def test_coupon_item_medium_close_to_sell_date_lower_bound_and_max_quality():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=6, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=5, quality=50)])


def test_coupon_item_very_close_to_sell_date_upper_bound():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=5, quality=7)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=4, quality=10)])


def test_coupon_item_very_close_to_sell_date_upper_bound_and_max_quality():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=5, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=4, quality=50)])


def test_coupon_item_very_close_to_sell_date_lower_bound():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=1, quality=7)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=0, quality=10)])


def test_coupon_item_very_close_to_sell_date_lower_bound_and_max_quality():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=1, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=0, quality=50)])


def test_coupon_item_on_sell_date():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=0, quality=10)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=-1, quality=0)])


def test_coupon_item_after_sell_date():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=-1, quality=10)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=-2, quality=0)])
