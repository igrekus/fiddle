from collections import namedtuple
from dataclasses import dataclass
from functools import reduce

__all__ = ['run']


Stock = namedtuple('Stock', ['brew', 'price', 'stock'])


def _parse_command(s):
    return (lambda st: st.split(maxsplit=1) if ' ' in st else (st, ''))(s)


def _help(*_):
    return _[0], f"Доступные команды: {tuple(_handlers.keys())}"


def _deposit(v, amt):
    return Vendor(balance=v._balance + 0 if not amt.isdigit() else int(amt) if int(amt) > 0 else 0, stock=v._stock), True


def _withdraw(v, _):
    return Vendor(stock=v._stock), f"Возвращено:{v._balance}"


def _buy(v, brew):
    if not brew:
        return v, True
    key = brew.lower()
    if key not in v._stock:
        return v, True
    item = v._stock[key]
    if v._balance < item.price:
        return v, f'Сумма недостаточна! Внесите еще монет'
    if item.stock <= 0:
        return v, f'Не осталось данного напитка!'
    v._stock[key] = Stock(item.brew, item.price, item.stock - 1)
    v._balance -= item.price
    return v, f'Выдан {item.brew}!'


_rpartial = lambda f, *args: lambda *a: f(*(a + args))

_handlers = {
    'помощь': _help,
    'взять': _buy,
    'внести': _deposit,
    'сдача': _withdraw,
    'выход': lambda *_: (_[0], False)
}
_handle = _rpartial(_handlers.get, lambda *_: (_[0], True))


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
    res = True
    while res is not False:
        print(f'{v}')
        v, res = _exec(v, input('Введите команду>>>:'))
        if isinstance(res, str):
            print(f'{res}')


if __name__ == '__main__':
    run()
