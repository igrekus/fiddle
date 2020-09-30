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
    return Vendor(balance=v.balance + 0 if not amt.isdigit() else int(amt) if int(amt) > 0 else 0, stock=v.stock), True


def _withdraw(v, _):
    return Vendor(stock=v.stock), f"Возвращено:{v.balance}"


def _buy(v, brew):
    return (lambda key: (v, True) if key not in v.stock else
        (v, 'Сумма недостаточна! Внесите еще монет') if v.balance < v.stock[key].price else
            (v, 'Не осталось данного напитка!') if v.stock[key].stock <= 0 else
                (Vendor(
                    balance=v.balance - v.stock[key].price,
                    stock={
                        **v.stock,
                        key: Stock(
                            v.stock[key].brew,
                            v.stock[key].price,
                            v.stock[key].stock - 1
                        )
                    }), f'Выдан {v.stock[key].brew}!'))(brew.lower())


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
        self.balance = balance
        self.stock = {
            'java': Stock('JAVA', 50, 5),
            'nesquick': Stock('Nesquick', 40, 5),
            'latte': Stock('Latte', 50, 5),
            'tea': Stock('Tea', 20, 5)
        } if stock is None else stock

    def __str__(self) -> str:
        return f"Напитки: {[b.brew for b in self.stock.values()]} Баланс: {self.balance}"

    def __eq__(self, other):
        return self.balance == other.balance and self.stock == other.stock


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
