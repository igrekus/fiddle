# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class Stock:
    brew: str
    price: int
    stock: int = 5


@dataclass
class Command:
    com: str
    param: str

    @classmethod
    def parse(cls, s: str):
        s = s.lower()
        try:
            com, *params = s.split()
            param = params[0]
        except (ValueError, IndexError):
            return cls(com=s, param='')
        else:
            return cls(com=com, param=param)


class Vendromat:
    def __init__(self):
        self._balance = 0
        self._stock = {
            'java': Stock('JAVA', 50),
            'nesquick': Stock('Nesquick', 40),
            'latte': Stock('Latte', 50),
            'tea': Stock('Tea', 20)
        }
        self._handlers = {
            'помощь': self._help,
            'выход': self._exit,
            'внести': self._deposit,
            'взять': self._buy,
            'сдача': self._withdraw
        }

    def __str__(self):
        return f"Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: {self._balance}"

    def _help(self, _):
        return "Доступные команды: ('помощь', 'взять', 'внести', 'сдача', 'выход')"

    def _exit(self, _):
        return False

    def _deposit(self, amt):
        try:
            amt = int(amt)
        except (ValueError, TypeError):
            pass
        else:
            if amt > 0:
                self._balance += amt
        return True

    def _withdraw(self, _):
        to_return, self._balance = self._balance, 0
        return f"Возвращено: {to_return}"

    def _buy(self, brew):
        if not brew:
            return True
        key = brew.lower()
        if key not in self._stock:
            return True
        if self._balance < self._stock[key].price:
            return f'Сумма недостаточна! Внесите еще монет'
        if self._stock[key].stock <= 0:
            return f'Не осталось данного напитка!'
        self._stock[key].stock -= 1
        self._balance -= self._stock[key].price
        return f'Выдан {self._stock[key].brew}!'

    def _default(self, _):
        return True

    def exec(self, com: str):
        c = Command.parse(com)
        return self._handlers.get(c.com, self._default)(c.param)


def run():
    v = Vendromat()
    res = ''
    while res is not False:
        print(f'{v}')
        res = v.exec(input('Введите команду>>>:'))
        if isinstance(res, str):
            print(f'{res}')


if __name__ == '__main__':
    run()
