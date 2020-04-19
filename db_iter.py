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
    unset_com = f'UNSET {params[0]}'
    for log in reversed(wal):
        for com in reversed(log):
            if com == unset_com:
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
            execute(com, silent=True)
    return wal.clear()

def default(*args):
    return 'unknown command'

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


def execute(com_str, silent=False):
    op, *params = com_str.split()
    op = op.upper()
    if op == 'END':
        return False
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
