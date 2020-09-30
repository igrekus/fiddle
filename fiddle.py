from dataclasses import dataclass
from functools import reduce

__all__ = ['run']


@dataclass
class Stock:
    brew: str
    price: int
    stock: int = 5


def _parse_command(s):
    return (lambda st: st.split(maxsplit=1) if ' ' in st else (st, ''))(s)


def _help(*_):
    return f"Доступные команды: {tuple(_handlers.keys())}"


def _exit(*_):
    return False


def _deposit(v, amt):
    if amt.isdigit():
        amt = int(amt)
        if amt > 0:
            v._balance += amt
    return True


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
    item.stock -= 1
    v._balance -= item.price
    return f'Выдан {item.brew}!'


def _default(*_):
    return True


_rpartial = lambda f, *args: lambda *a: f(*(a + args))

_handlers = {
    'помощь': _help,
    'взять': _buy,
    'внести': _deposit,
    'сдача': _withdraw,
    'выход': _exit
}
_handle = _rpartial(_handlers.get, _default)


class Vendor:
    def __init__(self):
        self._balance = 0
        self._stock = {
            'java': Stock('JAVA', 50),
            'nesquick': Stock('Nesquick', 40),
            'latte': Stock('Latte', 50),
            'tea': Stock('Tea', 20)
        }

    def __str__(self) -> str:
        return f"Напитки: {[b.brew for b in self._stock.values()]} Баланс: {self._balance}"

    def exec(self, com):
        return (lambda c, p: _handle(c)(self, p))(*_parse_command(com))


def run():
    v = Vendor()
    res = ''
    while res is not False:
        print(f'{v}')
        res = v.exec(input('Введите команду>>>:'))
        if isinstance(res, str):
            print(f'{res}')


if __name__ == '__main__':
    run()
