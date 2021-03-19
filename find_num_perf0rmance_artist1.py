from typing import List

def find_missing(seq: List[int], n: int):
    sum = lambda l, n=0: l[n] + sum(l, n+1) if n < len(l) - 1 else l[n]
    return sum([i for i in range(1, n+1)]) - sum(seq)

def find_duplicate(seq: List[int], n: int):
    sum = lambda l, n=0: l[n] + sum(l, n+1) if n < len(l) - 1 else l[n]
    return sum(seq) - sum([i for i in range(1, n+1)])