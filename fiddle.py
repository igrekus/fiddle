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


def get(params):
    return db.get(params[0], 'NULL')


def set_(params):
    return db.update({params[0]: params[1]})


def unset(params):
    db.pop(params[0], None)
    return None


def counts(params):
    return sum(v == params[0] for v in db.values())


def end(*args):
    sys.exit()


def default(*args):
    return 'unknown command'


def nop(*args): pass


print_command = nop if sys.stdin.isatty() else print
commands = {
    'GET': get,
    'SET': set_,
    'UNSET': unset,
    'COUNTS': counts,
    'END': end,
    '': end
}


def execute(com_str):
    print_command(com_str)
    op, *params = com_str.split()
    if res := commands.get(op.upper(), default)(params):
        print(res)
    return True


def run():
    while execute(input('>> ').strip()):
        pass


if __name__ == '__main__':
    run()
