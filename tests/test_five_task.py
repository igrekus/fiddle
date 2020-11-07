from pyexpect import expect

from fiddle import nearest_bus_stop, pack_pastry, rotate_board, locate_number, find_winners


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


def test_table_pattern():
    res = [(1, (1, 1)), (2, (1, 2)), (3, (2, 2)), (4, (2, 1)), (5, (3, 1)), (6, (3, 2)), (7, (3, 3)), (8, (2, 3)),
           (9, (1, 3)), (10, (1, 4)), (11, (2, 4)), (12, (3, 4)), (13, (4, 4)), (14, (4, 3)), (15, (4, 2)),
           (16, (4, 1)), (17, (5, 1)), (18, (5, 2)), (19, (5, 3)), (20, (5, 4)), (21, (5, 5)), (22, (4, 5)),
           (23, (3, 5)), (24, (2, 5)), (25, (1, 5)), (26, (1, 6)), (27, (2, 6)), (28, (3, 6)), (29, (4, 6)),
           (30, (5, 6)), (31, (6, 6)), (32, (6, 5)), (33, (6, 4)), (34, (6, 3)), (35, (6, 2)), (36, (6, 1)),
           (37, (7, 1))]
    for i, e in res:
        expect(locate_number(i)).to_equal(e)


def test_agar():
    raw = [
        [1, 1, 3, 4, 7, 15],
        [1, 1, 3, 4, 7, 16],
        [1, 1, 3, 4, 7, 17],
        [1, 1, 3, 8, 9, 17],
        [1, 2, 2, 4, 8, 15],
        [1, 1, 3, 4],
    ]

    res = [
        [0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1]
    ]

    for rw, rs in zip(raw, res):
        cw = find_winners(rw)
        assert cw == rs, f'{cw} {rs}'
