from fiddle import Vendor, _exec
from pyexpect import expect


def test_run_should_display_ui_on_start():
    expected = """Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 0"""

    expect(str(Vendor())).to_equal(expected)


def test_run_command_should_display_help_on_help():
    expected = """Доступные команды: ('помощь', 'взять', 'внести', 'сдача', 'выход')"""

    expect(_exec(Vendor(), 'помощь')).to_equal(expected)


def test_run_command_should_return_false_on_exit():
    expected = False

    expect(_exec(Vendor(), 'выход')).to_be(expected)


def test_run_command_should_nop_on_unknown_command():
    expected = True

    expect(_exec(Vendor(), 'lolcommand')).to_equal(expected)


def test_run_command_should_nop_on_empty_command():
    expected = True

    expect(_exec(Vendor(), '')).to_equal(expected)


def test_run_command_should_nop_on_wrong_update_balance_command1():
    expected = True

    expect(_exec(Vendor(), 'внести 1.1')).to_equal(expected)


def test_run_command_should_nop_on_wrong_update_balance_command2():
    expected = True

    expect(_exec(Vendor(), 'внести text')).to_equal(expected)


def test_run_command_should_nop_on_wrong_update_balance_command3():
    expected = True

    expect(_exec(Vendor(), 'внести text ext')).to_equal(expected)


def test_run_command_should_nop_on_wrong_update_balance_command4():
    expected = True

    expect(_exec(Vendor(), 'внести -1')).to_equal(expected)


def test_run_command_should_nop_on_wrong_update_balance_command5():
    expected = True

    expect(_exec(Vendor(), 'внести 0')).to_equal(expected)


def test_run_command_should_update_balance():
    expected = 100

    v = Vendor()
    _exec(v, 'внести 100')

    expect(v._balance).to_equal(expected)


def test_run_command_should_withdraw1():
    expected = """Возвращено:0"""

    expect(_exec(Vendor(), 'сдача')).to_equal(expected)


def test_run_command_should_withdraw2():
    expected = """Возвращено:50"""

    v = Vendor()
    _exec(v, 'внести 50')
    expect(_exec(v, 'сдача')).to_equal(expected)


def test_run_command_should_nop_on_vend_unknown1():
    expected = True

    v = Vendor()
    _exec(v, 'внести 100')
    expect(_exec(v, 'взять lol')).to_equal(expected)


def test_run_command_should_nop_on_vend_unknown2():
    expected = True

    v = Vendor()
    _exec(v, 'внести 100')
    expect(_exec(v, 'взять')).to_equal(expected)


def test_run_command_should_reject_not_enough_balance():
    expected = """Сумма недостаточна! Внесите еще монет"""

    v = Vendor()
    _exec(v, 'внести 40')
    expect(_exec(v, 'взять JAVA')).to_equal(expected)


def test_run_command_should_reject_not_enough_stock():
    expected = """Не осталось данного напитка!"""

    v = Vendor()
    _exec(v, 'внести 300')
    for _ in range(5):
        _exec(v, 'взять JAVA')
    expect(_exec(v, 'взять JAVA')).to_equal(expected)


def test_run_command_should_normal_vend():
    expected = """Выдан JAVA!"""

    v = Vendor()
    _exec(v, 'внести 100')
    expect(_exec(v, 'взять JAVA')).to_equal(expected)
