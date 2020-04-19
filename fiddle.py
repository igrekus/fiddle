"""
Сделать маленький вариант базы данных. Никакого сетевого
взаимодействия не нужно. Данные читаются из stdin.
База лежит в оперативной памяти. Одна строка, всегда ровно один запрос. Аргументы
команд пробелов не содержат. Также в вводе должен распознаваться EOF, который означает конец ввода и завершение приложения.
Команды:
•	SET - сохраняет аргумент в базе данных.
•	GET - возвращает, ранее сохраненную переменную. Если такой переменной
•	не было сохранено, возвращает NULL
•	UNSET - удаляет, ранее установленную переменную. Если значение не было
•	установлено, не делает ничего.
•	COUNTS - показывает сколько раз данные значение встречается в базе данных.
•	END - закрывает приложение.
Пример:
>> GET A
NULL
>> SET A 10
>> GET A
10
>> COUNTS 10
1
>> SET B 20
>> SET C 10
>> COUNTS 10
2
>> UNSET B
>> GET B
NULL
>> END
---

Транзакции
>> BEGIN
>> SET A 10
>> BEGIN
>> SET A 20
>> SET A 30
>> GET A
30
>> ROLLBACK
>> GET A
10
>> COMMIT
>> GET A
10
"""
import sys

db = dict()
wal = list()


def get_db(params):
    return db.get(params[0], 'NULL')

def set_db(params):
    return db.update({params[0]: params[1]})

def unset_db(params):
    db.pop(params[0], None)
    return None

def counts_db(params):
    return sum(v == params[0] for v in db.values())


def get_wal(params):
    for com in reversed(wal[-1]):
        set_com = f'SET {params[0]} '
        unset_com = f'UNSET {params[0]}'
        if com == unset_com:
            return 'MULL'
        if com.startswith(set_com):
            return com.lstrip(set_com)
    return 'NULL'

def set_wal(params):
    return wal[-1].append(f'SET {params[0]} {params[1]}')

def unset_wal(params):
    return wal[-1].append(f'UNSET {params[0]}')

def counts_wal(params):
    tmp = counts_db(params)
    for log in reversed(wal):
        for com in reversed(log):
            if com.startswith(f'UNSET {params[0]}'):
                tmp -= 1
    return 'counts wal'


def end(*args):
    sys.exit()


def begin(*args):
    commands.update({
        'GET': get_wal,
        'SET': set_wal,
        'UNSET': unset_wal,
    })
    return wal.append([])


def rollback(*args):
    wal.pop(-1)
    return None


def commit(*args):
    commands.update({
        'GET': get_db,
        'SET': set_db,
        'UNSET': unset_db,
    })
    for log in reversed(wal):
        for com in reversed(log):
            execute(com, silent=True)
    return wal.clear()


def default(*args):
    return 'unknown command'


def nop(*args): pass


print_command = nop if sys.stdin.isatty() else print

commands = {
    'GET': get_db,
    'SET': set_db,
    'UNSET': unset_db,
    'COUNTS': counts_db,
    'END': end,
    '': end,
    'BEGIN': begin,
    'ROLLBACK': rollback,
    'COMMIT': commit
}


def execute(com_str, silent=False):
    if not silent:
        print_command(com_str)
    op, *params = com_str.split()
    if res := commands.get(op.upper(), default)(params):
        if not silent:
            print(res)
    return True


def run():
    try:
        while execute(input('>> ').strip()):
            pass
    except EOFError:
        pass


if __name__ == '__main__':
    run()
