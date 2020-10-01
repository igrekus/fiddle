from collections import namedtuple

__all__ = ['run']


def run():
    vend, res = Vendor(
        balance=0,
        stock={
            'java': Stock('JAVA', 50, 5),
            'nesquick': Stock('Nesquick', 40, 5),
            'latte': Stock('Latte', 50, 5),
            'tea': Stock('Tea', 20, 5)
        }
    ), True
    while res:
        *_, vend, res = (lambda v, r: (print(f'{r}') if isinstance(r, str) else None,
                                       print(f'{_show(v)}'),
                                       *_exec(v, input('Введите команду>>>:'))))(vend, res)


Vendor = namedtuple('Vendor', ['balance', 'stock'])
Stock = namedtuple('Stock', ['brew', 'price', 'stock'])


def _show(v):
    return f"Напитки: {[b.brew for b in v.stock.values()]} Баланс: {v.balance}"


def _exec(v, com):
    return (lambda c, p: _select(c)(v, p))(*_parse_command(com))


def _parse_command(s):
    return (lambda st: st.split(maxsplit=1) if ' ' in st else (st, ''))(s)


def _help(*_):
    return _[0], f"Доступные команды: {tuple(_commands)}"


def _deposit(v, amt):
    return Vendor(balance=v.balance + 0 if not amt.isdigit() else int(amt) if int(amt) > 0 else 0, stock=v.stock), True


def _withdraw(v, _):
    return Vendor(balance=0, stock=v.stock), f"Возвращено:{v.balance}"


def _buy(v, brew):
    return (lambda key: (v, True) if key not in v.stock else (lambda item:
        (v, 'Сумма недостаточна! Внесите еще монет') if v.balance < item.price else
            (v, 'Не осталось данного напитка!') if item.stock <= 0 else
                (Vendor(
                    balance=v.balance - item.price,
                    stock={
                        **v.stock,
                        key: Stock(
                            item.brew,
                            item.price,
                            item.stock - 1
                        )
                    }), f'Выдан {item.brew}!'))(v.stock[key]))(brew.lower())


def _exit(*_):
    return _[0], False


_rpartial = lambda f, *args: lambda *a: f(*(a + args))
_commands = ['помощь', 'взять', 'внести', 'сдача', 'выход']
_handlers = [_help, _buy, _deposit, _withdraw, _exit]
_select = _rpartial(dict(zip(_commands, _handlers)).get, lambda *_: (_[0], True))


if __name__ == '__main__':
    run()
