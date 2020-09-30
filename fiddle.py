from collections import namedtuple
from dataclasses import dataclass
from functools import reduce

__all__ = ['run']


Stock = namedtuple('Stock', ['brew', 'price', 'stock'])


def _parse_command(s):
    return (lambda st: st.split(maxsplit=1) if ' ' in st else (st, ''))(s)


def _help(*_):
    return f"Доступные команды: {tuple(_handlers.keys())}"


def _deposit(v, amt):
    return Vendor(balance=v._balance + 0 if not amt.isdigit() else int(amt) if int(amt) > 0 else 0, stock=v._stock)


def _withdraw(v, _):
    to_return, v._balance = v._balance, 0
    return f"Возвращено:{to_return}"


def _buy(v, brew):
    if not brew:
        return True
    key = brew.lower()
    if key not in v._stock:
        return True
    item = v._stock[key]
    if v._balance < item.price:
        return f'Сумма недостаточна! Внесите еще монет'
    if item.stock <= 0:
        return f'Не осталось данного напитка!'
    v._stock[key] = Stock(item.brew, item.price, item.stock - 1)
    v._balance -= item.price
    return f'Выдан {item.brew}!'


_rpartial = lambda f, *args: lambda *a: f(*(a + args))

_handlers = {
    'помощь': _help,
    'взять': _buy,
    'внести': _deposit,
    'сдача': _withdraw,
    'выход': lambda *args: False
}
_handle = _rpartial(_handlers.get, lambda *args: True)


def _exec(v, com):
    return (lambda c, p: _handle(c)(v, p))(*_parse_command(com))


class Vendor:
    def __init__(self, balance=0, stock=None):
        self._balance = balance
        self._stock = {
            'java': Stock('JAVA', 50, 5),
            'nesquick': Stock('Nesquick', 40, 5),
            'latte': Stock('Latte', 50, 5),
            'tea': Stock('Tea', 20, 5)
        } if stock is None else stock

    def __str__(self) -> str:
        return f"Напитки: {[b.brew for b in self._stock.values()]} Баланс: {self._balance}"

    def __eq__(self, other):
        return self._balance == other._balance and self._stock == other._stock


def run():
    v = Vendor()
    res = ''
    while res is not False:
        print(f'{v}')
        v, msg = _exec(v, input('Введите команду>>>:'))
        if msg:
            print(f'{msg}')


if __name__ == '__main__':
    run()
