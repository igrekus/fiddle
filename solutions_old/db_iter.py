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
    return sum(v == params[0] for v in db.values()) or '0'

def get_wal(params):
    set_com = f'SET {params[0]} '
    for log in reversed(wal):
        for com in reversed(log):
            if com == f'UNSET {params[0]}':
                return 'MULL'
            if com.startswith(set_com):
                return com.lstrip(set_com)
    return get_db(params)

def set_wal(params):
    return wal[-1].append(f'SET {params[0]} {params[1]}')

def unset_wal(params):
    return wal[-1].append(f'UNSET {params[0]}')

def begin(*args):
    commands.update({
        'GET': get_wal,
        'SET': set_wal,
        'UNSET': unset_wal,
    })
    return wal.append([])

def rollback(*args):
    if wal:
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
            execute(com)
    return wal.clear()

def nop(*args): pass

commands = {
    'GET': get_db,
    'SET': set_db,
    'UNSET': unset_db,
    'COUNTS': counts_db,
    'END': nop,
    '': nop,
    'BEGIN': begin,
    'ROLLBACK': rollback,
    'COMMIT': commit
}


def execute(com_str):
    op, *params = com_str.split()
    op = op.upper()
    if op == 'END':
        return False
    if res := commands.get(op, lambda *args: 'unknown command')(params):
        print(res)
    return True


def run():
    try:
        while execute(input('>> ').strip()):
            pass
    except EOFError:
        pass


if __name__ == '__main__':
    import sys
    from io import StringIO

    sio = StringIO()
    with open('inp.txt', 'rt', encoding='utf-8') as f:
        sys.stdin = f
        sys.stdout = sio

        run()

    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    print(""">> NULL
>> >> 10
>> 1
>> >> >> 2
>> >> NULL
>> """ == sio.getvalue())

