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

"""
import sys

db = dict()


def exec_get(params):
    return db.get(params[0], 'NULL')


def exec_set(params):
    db[params[0]] = params[1]
    return None


def exec_unset(params):
    db.pop(params[0], None)
    return None


def exec_counts(params):
    return sum(v == params[0] for v in db.values())


def exec_end(*args):
    sys.exit()


def exec_default(*args):
    return 'unknown command'


def exec_empty(*args):
    sys.exit()


command_selector = {
    'GET': exec_get,
    'SET': exec_set,
    'UNSET': exec_unset,
    'COUNTS': exec_counts,
    'END': exec_end,
    '': exec_empty
}


def execute(com_str):
    print_command(com_str)
    op, *params = com_str.split()
    if res := command_selector.get(op.upper(), exec_default)(params):
        print(res)
    return True


def nop(*args): pass


print_command = nop if sys.stdin.isatty() else print


def run():
    while execute(input('>> ').strip()):
        pass


if __name__ == '__main__':
    run()
