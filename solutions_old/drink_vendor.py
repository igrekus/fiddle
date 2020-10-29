"""
This module emulates a beverage vending machine.

Implements a CLI user interface, capable of handling a set of commands:

    помощь       -- display the help message
    взять <brew> -- sell the selected beverage, if requirements are met
    внести <sum> -- deposit <sum> to the session balance
    сдача        -- retrieve the deposited money
    выход        -- exit the current vending session

Business rules:

    - the vending session is a REPL cycle
    - commands and parameters can be input in any register
    - command prompt is preceded by a status message:

        Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 0
        Введите команду>>>:

    - unknown commands are ignored
    - commands with unknown malformed parameters are ignored
    - no error messages
    - 'помощь' displays 'Доступные команды: <список команд>'
    - 'взять <brew>':
        - displays 'Сумма недостаточна! Внесите еще монет' message and rejects the operation
          if not enough credit is deposited
        - displays 'Не осталось данного напитка!' message and rejects the operation if selected beverage is out of stock
        - displays 'Выдан <brew>' message and updates the internal machine state if both conditions are satisfied
    - 'внести <sum>' updates credit balance if parameter is a natural number
    - 'сдача' displays 'Возвращено:<balance>' message and resets the machine balance to 0
    - 'выход' shuts down the current vending session
    - upon launch, the machine has ['JAVA', 'Nesquick', 'Latte', 'Tea'] beverages available, 5 units each in stock
    - beverage prices are:
        JAVA: 50
        Latte: 50
        Nesquick: 40
        Tea: 20

Example:

    Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea']
    Баланс: 0
    Введите команду>>>:помощь
    Доступные команды: ('помощь', 'взять', 'внести', 'сдача', 'выход')
    Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea']
    Баланс: 0
    Введите команду>>>:внести 100
    Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea']
    Баланс: 100
    Введите команду>>>:взять JAVA
    Выдан java
    Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea']
    Баланс: 50
    Введите команду>>>:сдача
    Возвращено:50
    Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea']
    Баланс: 0
    Введите команду>>>:выход

    Process finished with exit code 0
"""
from dataclasses import dataclass
from typing import Union

__all__ = ['run']


@dataclass
class Stock:
    """
    Helper, stores machine stock entry information.

    Not a part of the public API.
    """
    brew: str
    price: int
    stock: int = 5


@dataclass
class Command:
    """
    Helper, processes the user input.

    Not a part of the public API.
    """
    com: str
    param: str

    @classmethod
    def parse(cls, s: str):
        """
        Parses the input string into command name and parameter.

        :param s: raw input string to parse
        """
        s = s.lower()
        try:
            com, *params = s.split()
            param = params[0]
        except (ValueError, IndexError):
            return cls(com=s, param='')
        else:
            return cls(com=com, param=param)


class Vendor:
    """
    Helper, handles the emulated machine state changes.

    Not a part of the public API.
    """
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
            'взять': self._buy,
            'внести': self._deposit,
            'сдача': self._withdraw,
            'выход': self._exit
        }

    def __str__(self) -> str:
        return f"Напитки: {[b.brew for b in self._stock.values()]} Баланс: {self._balance}"

    def _help(self, _) -> str:
        """Builds and returns the help message."""
        return f"Доступные команды: {tuple(self._handlers.keys())}"

    def _exit(self, _) -> bool:
        """Returns the exit flag."""
        return False

    def _deposit(self, amt: int) -> bool:
        """
        Deposits the credit to the session balance.

        :param amt: - natural number, amount to deposit
        :return: bool flag
        """
        try:
            amt = int(amt)
        except (ValueError, TypeError):
            pass
        else:
            if amt > 0:
                self._balance += amt
        return True

    def _withdraw(self, _) -> str:
        """
        Withdraws the remaining credits.

        :return: report message
        """
        to_return, self._balance = self._balance, 0
        return f"Возвращено:{to_return}"

    def _buy(self, brew: str) -> Union[str, bool]:
        """
        Vends the requested beverage and updates the machine state if enough credit is on the balance
        and the beverage is in stock.

        :param brew: requested beverage name
        :return: report message on error or bool flag on success
        """
        if not brew:
            return True
        key = brew.lower()
        if key not in self._stock:
            return True
        item = self._stock[key]
        if self._balance < item.price:
            return f'Сумма недостаточна! Внесите еще монет'
        if item.stock <= 0:
            return f'Не осталось данного напитка!'
        item.stock -= 1
        self._balance -= item.price
        return f'Выдан {item.brew}!'

    def _default(self, _) -> bool:
        """
        Handles unrecognised commands.

        :return: bool flag
        """
        return True

    def exec(self, com: str) -> Union[str, bool]:
        """
        Selects a command handler based on the user input.

        :return: either a status message ot a bool flag
        """
        c = Command.parse(com)
        return self._handlers.get(c.com, self._default)(c.param)


def run():
    """
    Runs the vending session REPL.

    Part of the public API
    """
    v = Vendor()
    res = ''
    while res is not False:
        print(f'{v}')
        res = v.exec(input('Введите команду>>>:'))
        if isinstance(res, str):
            print(f'{res}')


if __name__ == '__main__':
    run()
