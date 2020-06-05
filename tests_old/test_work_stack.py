from pyexpect import expect

from fiddle import work


def test_work_1():
    expect(work([2.9, 2.1])).to_be(True)


def test_work_2():
    expect(work([5.6, 9.0, 2.0])).to_be(False)


def test_work_3():
    expect(work([9.0, 5.6, 2.0])).to_be(True)


def test_work_4():
    expect(work([2.0, 5.6, 9.0])).to_be(True)


def test_work_5():
    expect(work([5.6])).to_be(True)


def test_work_6():
    expect(work([])).to_be(True)


def test_work_7():
    expect(work([4, 2, 1, 3, 1])).to_be(False)


def test_work_8():
    expect(work([2, 3, 5, 6, 4, 1, 2, 2, 4])).to_be(False)


def test_work_9():
    expect(work([6, 5, 4, 3, 2, 1, 1])).to_be(True)


def test_work_10():
    expect(work([3, 2, 1, 1, 2, 2, 4])).to_be(True)


def test_work_11():
    expect(work([3, 2, 1, 1, 2, 1, 4])).to_be(True)


def test_work_12():
    expect(work([2, 2, 1, 5, 4, 3])).to_be(True)
