import random

n = 1000
seq = list(range(1, n))
seq.append(random.randint(1, n))
seq.remove(random.randint(1, n))


def find_missing(seq:list, n:int) -> int:
    a = set(list(range(1, n))).difference(seq)
    for i in a:
        return i


def find_duplicate(seq:list, n:int) -> int:
    return [x for x in seq if seq.count(x) >= 2][1]


print(find_duplicate(seq=seq, n=n))
print(find_missing(seq=seq, n=n))
