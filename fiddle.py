# -*- coding: utf-8 -*-
"""
Нашему старому знакомому, хакеру Василию стали поступать все более серьезные заказы,
на этот раз ему заказали ПО для аппарата с напитками.
Заказчик настаивает, чтобы все сообщения строго соотвествовали шаблонам из ТЗ, а вот и оно само:

Программа имитирует работу аппарата с напитками, постоянно запрашивает ввод пользователя,
команды могут быть в любом регистре после каждого действия пишет статус одной строкой:
+ 'Напитки: [список напитков] Баланс: 0' (только названия напитков, без количества и цен)

+ При наборе 'помощь' выдает список доступных команд одной строкой: 'Доступные команды: {список команд}'
+ При наборе 'взять {напиток}' если не хватает денег то пишет 'Сумма недостаточна! Внесите еще монет'
+ При наборе 'взять {напиток}' если нет такого напитка ничего не делает (предполагается что клиент всегда выберет из имеющихся)
+ При наборе 'взять {напиток}' если не осталось напитка пишет 'Не осталось данного напитка!'
+ При наборе 'взять {напиток}' если напиток в наличии и средств достаточно, то пишет 'Выдан {напиток}', уменьшает количество напитка на 1
+ При команде 'внести {сумма}', если введено не число, не положительное или не целое число то игнорирует, иначе пополняет баланс
+ При команде {сдача} возвращает все что на балансе, пишет сообщение 'Возвращено:{сумма}'
+ При команде 'выход' завершается

+ При неизвестной команде ничего не делает, возвращается к запросу ввода.
Аппарат не возвращает никаких ошибок, не зависает и умеет выполнять только вышеуказанные функции.

При старте аппарат содержит следующие напитки: ('JAVA', 'Nesquick', 'Latte', 'Tea') все в количестве 5 единиц
Java и Latte стоят по 50, Nesquick стоит 40, а Tea - 20

Пример работы программы:

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


@dataclass
class Stock:
    brew: str
    price: int
    stock: int = 5


@dataclass
class Command:
    com: str
    par: str
    @classmethod
    def parse(cls, s: str):
        s = s.lower()
        try:
            com, *params = s.split()
            param = params[0]
        except (ValueError, IndexError):
            return cls(com=s, par='')
        else:
            return cls(com=com, par=param)
    @property
    def param(self):
        return self.par
    def __eq__(self, other):
        if isinstance(other, str):
            return self.com == other


class Vendromat:
    def __init__(self):
        self.balance = 0
        self.stock = {
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
        return f"Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: {self.balance}"

    def _help(self, _):
        return "Доступные команды: ('помощь', 'взять', 'внести', 'сдача', 'выход')"
    def _exit(self, _):
        return False
    def _deposit(self, amt):
        try:
            amt = int(amt)
        except (ValueError, TypeError, IndexError):
            return self.__str__()
        if amt <= 0:
            return self.__str__()
        self.balance += amt
        return self.__str__()
    def _withdraw(self, _):
        to_return, self.balance = self.balance, 0
        return f"Возвращено: {to_return}\n{self.__str__()}"
    def _buy(self, brew):
        if not brew:
            return self.__str__()
        key = brew.lower()
        if key not in self.stock:
            return self.__str__()
        if self.balance < self.stock[key].price:
            return f'Сумма недостаточна! Внесите еще монет\n{self.__str__()}'
        if self.stock[key].stock <= 0:
            return f'Не осталось данного напитка!\n{self.__str__()}'
        self.stock[key].stock -= 1
        self.balance -= self.stock[key].price
        return f'Выдан {self.stock[key].brew}!\n{self.__str__()}'
    def _default(self, _):
        return self.__str__()
    def exec(self, com: str):
        c = Command.parse(com)
        return self._handlers.get(c.com, self._default)(c.param)


def run() -> str:
    return "Напитки: ['JAVA', 'Nesquick', 'Latte', 'Tea'] Баланс: 0"
