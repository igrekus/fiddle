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


def execute(com_str):
    op, *params = com_str.split()
    op = op.upper()
    if op == 'GET':
        return db.get(params[0], 'NULL')
    elif op == 'SET':
        db[params[0]] = params[1]
    elif op == 'UNSET':
        db.pop(params[0], None)
        return None
    elif op == 'COUNTS':
        return sum(v == params[0] for v in db.values())
    elif op == 'END':
        return -1
        # sys.exit()
    else:
        return 'wrong command'


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
