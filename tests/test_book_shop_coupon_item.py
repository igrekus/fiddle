from pyexpect import expect
from fiddle import BookShop, Item


def test_coupon_item_normal_day():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=50, quality=48)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=49, quality=49)])


def test_coupon_item_max_quality():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=50, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=49, quality=50)])


def test_coupon_item_ten_days_to_sell_in():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=10, quality=40)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=9, quality=42)])


def test_coupon_item_ten_days_to_sell_in_almost_max_quality():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=10, quality=49)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=9, quality=50)])


def test_coupon_item_ten_days_to_sell_in_max_quality():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=10, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=9, quality=50)])


def test_coupon_item_five_days_to_sell_in():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=5, quality=40)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=4, quality=43)])


def test_coupon_item_five_days_to_sell_in_almost_max_quality():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=5, quality=49)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=4, quality=50)])


def test_coupon_item_five_days_to_sell_in_max_quality():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=5, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=4, quality=50)])


def test_coupon_item_zero_days_to_sell_in_quality_stays():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=1, quality=47)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=0, quality=50)])


def test_coupon_item_past_sell_in_drop_quality_drops_to_zero():
    shop = BookShop([Item('Скидочный купон на курс', sell_in=0, quality=50)])

    shop.update_quality()

    expect(shop.items).to_equal([Item('Скидочный купон на курс', sell_in=-1, quality=0)])
