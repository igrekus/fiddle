from fiddle import Vendor, _exec, Stock
from pyexpect import expect


def test_run_should_display_ui_on_start():
    expect(str(Vendor())).to_equal("""Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 0""")


def test_run_command_should_display_help_on_help():
    v, msg = _exec(Vendor(), 'помощь')

    expect(v).to_equal(Vendor())
    expect(msg).to_equal("""Доступные команды: ('помощь', 'взять', 'внести', 'сдача', 'выход')""")


def test_run_command_should_return_false_on_exit():
    v, res = _exec(Vendor(), 'выход')

    expect(v).to_equal(Vendor())
    expect(res).to_equal(False)


def test_run_command_should_nop_on_unknown_command():
    v, res = _exec(Vendor(), 'lolcommand')

    expect(v).to_equal(Vendor())
    expect(res).to_equal(True)


def test_run_command_should_nop_on_empty_command():
    v, res = _exec(Vendor(), '')

    expect(v).to_equal(Vendor())
    expect(res).to_equal(True)


def test_run_command_should_nop_on_wrong_update_balance_command1():
    v, res = _exec(Vendor(), 'внести 1.1')

    expect(v).to_equal(Vendor())
    expect(res).to_equal(True)


def test_run_command_should_nop_on_wrong_update_balance_command2():
    v, res = _exec(Vendor(), 'внести text')

    expect(v).to_equal(Vendor())
    expect(res).to_equal(True)


def test_run_command_should_nop_on_wrong_update_balance_command3():
    v, res = _exec(Vendor(), 'внести text ext')

    expect(v).to_equal(Vendor())
    expect(res).to_equal(True)


def test_run_command_should_nop_on_wrong_update_balance_command4():
    v, res = _exec(Vendor(), 'внести -1')

    expect(v).to_equal(Vendor())
    expect(res).to_equal(True)


def test_run_command_should_nop_on_wrong_update_balance_command5():
    v, res = _exec(Vendor(), 'внести 0')

    expect(v).to_equal(Vendor())
    expect(res).to_equal(True)


def test_run_command_should_update_balance():
    v, res = _exec(Vendor(), 'внести 100')

    expect(v).to_equal(Vendor(balance=100))
    expect(res).to_equal(True)


def test_run_command_should_withdraw1():
    v, res = _exec(Vendor(), 'сдача')

    expect(v).to_equal(Vendor())
    expect(res).to_equal("""Возвращено:0""")


def test_run_command_should_withdraw2():
    v, _ = _exec(Vendor(), 'внести 50')
    v, res = _exec(v, 'сдача')

    expect(v).to_equal(Vendor())
    expect(res).to_equal("""Возвращено:50""")


def test_run_command_should_nop_on_vend_unknown1():
    v, _ = _exec(Vendor(), 'внести 100')
    v, res = _exec(v, 'взять lol')

    expect(v).to_equal(Vendor(balance=100))
    expect(res).to_equal(True)


def test_run_command_should_nop_on_vend_unknown2():
    v, _ = _exec(Vendor(), 'внести 100')
    v, res = _exec(v, 'взять')

    expect(v).to_equal(Vendor(balance=100))
    expect(res).to_equal(True)


def test_run_command_should_reject_not_enough_balance():
    v, _ = _exec(Vendor(), 'внести 40')
    v, res = _exec(v, 'взять JAVA')

    expect(v).to_equal(Vendor(balance=40))
    expect(res).to_equal("""Сумма недостаточна! Внесите еще монет""")


def test_run_command_should_reject_not_enough_stock():
    v, _ = _exec(Vendor(), 'внести 300')
    for _ in range(5):
        v, res = _exec(v, 'взять JAVA')

    v, res = _exec(v, 'взять JAVA')

    expect(v).to_equal(Vendor(balance=50, stock={
        'java': Stock('JAVA', 50, 0),
        'nesquick': Stock('Nesquick', 40, 5),
        'latte': Stock('Latte', 50, 5),
        'tea': Stock('Tea', 20, 5)
    }))
    expect(res).to_equal("""Не осталось данного напитка!""")


def test_run_command_should_normal_vend():
    v, _ = _exec(Vendor(), 'внести 100')
    v, res = _exec(v, 'взять JAVA')

    expect(v).to_equal(Vendor(balance=50, stock={
        'java': Stock('JAVA', 50, 4),
        'nesquick': Stock('Nesquick', 40, 5),
        'latte': Stock('Latte', 50, 5),
        'tea': Stock('Tea', 20, 5)
    }))
    expect(res).to_equal("""Выдан JAVA!""")
