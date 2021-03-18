def find_missing(a) -> int:
    w = 1
    for i in a:
        q = i + 1
        if q not in a:
            if w == 2:
                continue
            elif w == 1:
                w = 2
                return q


def find_duplicate(b) -> int:
    c = b
    for i in b:
        c.remove(i)
        if i in c:
            return i
