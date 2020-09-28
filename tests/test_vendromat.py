from fiddle import run, Vendromat
from pyexpect import expect


def test_run_should_display_ui_on_start():
    expected = """Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 0"""

    expect(str(Vendromat())).to_equal(expected)


def test_run_command_should_display_help_on_help():
    expected = """Доступные команды: ('помощь', 'взять', 'внести', 'сдача', 'выход')"""

    expect(Vendromat().exec('помощь')).to_equal(expected)


def test_run_command_should_return_false_on_exit():
    expected = False

    expect(Vendromat().exec('выход')).to_be(expected)


def test_run_command_should_nop_on_unknown_command():
    expected = """Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 0"""

    expect(Vendromat().exec('lolcommand')).to_equal(expected)


def test_run_command_should_nop_on_empty_command():
    expected = """Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 0"""

    expect(Vendromat().exec('')).to_equal(expected)


def test_run_command_should_nop_on_wrong_update_balance_command1():
    expected = """Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 0"""

    expect(Vendromat().exec('внести 1.1')).to_equal(expected)


def test_run_command_should_nop_on_wrong_update_balance_command2():
    expected = """Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 0"""

    expect(Vendromat().exec('внести text')).to_equal(expected)


def test_run_command_should_nop_on_wrong_update_balance_command3():
    expected = """Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 0"""

    expect(Vendromat().exec('внести text ext')).to_equal(expected)


def test_run_command_should_nop_on_wrong_update_balance_command4():
    expected = """Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 0"""

    expect(Vendromat().exec('внести -1')).to_equal(expected)


def test_run_command_should_nop_on_wrong_update_balance_command5():
    expected = """Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 0"""

    expect(Vendromat().exec('внести 0')).to_equal(expected)


def test_run_command_should_update_balance():
    expected = """Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 100"""

    expect(Vendromat().exec('внести 100')).to_equal(expected)


def test_run_command_should_withdraw1():
    expected = """Возвращено: 0\nНапитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 0"""

    expect(Vendromat().exec('сдача')).to_equal(expected)


def test_run_command_should_withdraw2():
    expected = """Возвращено: 50\nНапитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 0"""

    v = Vendromat()
    v.exec('внести 50')
    expect(v.exec('сдача')).to_equal(expected)


def test_run_command_should_nop_on_vend_unknown1():
    expected = """Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 100"""

    v = Vendromat()
    v.exec('внести 100')
    expect(v.exec('взять lol')).to_equal(expected)


def test_run_command_should_nop_on_vend_unknown2():
    expected = """Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 100"""

    v = Vendromat()
    v.exec('внести 100')
    expect(v.exec('взять')).to_equal(expected)


def test_run_command_should_reject_not_enough_balance():
    expected = """Сумма недостаточна! Внесите еще монет\nНапитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 40"""

    v = Vendromat()
    v.exec('внести 40')
    expect(v.exec('взять JAVA')).to_equal(expected)


def test_run_command_should_reject_not_enough_stock():
    expected = """Не осталось данного напитка!\nНапитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 50"""

    v = Vendromat()
    v.stock['java'] = 0
    v.exec('внести 50')
    expect(v.exec('взять JAVA')).to_equal(expected)


def test_run_command_should_normal_vend():
    expected = """Выдан JAVA!\nНапитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 50"""

    v = Vendromat()
    v.exec('внести 100')
    expect(v.exec('взять JAVA')).to_equal(expected)
