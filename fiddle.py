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
from io import StringIO
string_io = StringIO()

test_commands = ['GET A', 'SET A 10', 'GET A', 'COUNTS 10', 'SET B 20', 'SET C 10', 'COUNTS 10', 'UNSET B', 'GET B', 'END']

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
    return -1


def exec_default(*args):
    return 'wrong command'

def execute(com_str):
    op, *params = com_str.split()
    op = op.upper()
    if op == 'GET':
        return exec_get(params)
    elif op == 'SET':
        return exec_set(params)
    elif op == 'UNSET':
        return exec_unset(params)
    elif op == 'COUNTS':
        return exec_counts(params)
    elif op == 'END':
        return exec_end(params)
    else:
        return exec_default(params)


def run():
    sys.stdout = string_io

    while True:
        print('>> ', end='')
        if not (com := sys.stdin.readline().strip()):
            sys.exit()
        print(com)
        res = execute(com)
        if res is not None:
            print(res)
            if res == -1:
                sys.stdout = sys.__stdout__
                output = string_io.getvalue()
                print('test pass', output == """>> GET A
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
-1
""")
                sys.exit()


if __name__ == '__main__':
    run()
