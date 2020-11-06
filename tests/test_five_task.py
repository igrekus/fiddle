from pyexpect import expect

from fiddle import nearest_bus_stop, pack_pastry, rotate_board


def test_bus_stop():
    expect(nearest_bus_stop(500, 2000)).exact.node.to_equal(0)
    expect(nearest_bus_stop(500, 2100)).prev.closer.to_equal(100)
    expect(nearest_bus_stop(500, 2300)).next.closer.to_equal(200)
    expect(nearest_bus_stop(500, 2250)).midpoint.to_equal(250)


def test_pack_pastry():
    expect(pack_pastry(6, 6)).zero.diff.to_equal((2, 2))
    expect(pack_pastry(4, 5)).one.diff.to_equal((1, 2))
    expect(pack_pastry(5, 4)).one.diff.to_equal((2, 1))
    expect(pack_pastry(3, 5)).two.diff.to_equal(None)
    expect(pack_pastry(5, 3)).two.diff.to_equal(None)
    expect(pack_pastry(2, 5)).three.diff.to_equal(None)
    expect(pack_pastry(5, 2)).three.diff.to_equal(None)
    expect(pack_pastry(2, 7)).big.diff.to_equal(None)
    expect(pack_pastry(7, 2)).big.diff.to_equal(None)


def test_rotate_board():
    expect(rotate_board([4, 2, 3, 5, 1])).to_equal([1, 4, 3, 5, 2])

