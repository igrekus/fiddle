from typing import List

def difference(seq: List[int], n: int):
    sum = lambda l, n=0: l[n] + sum(l, n+1) if n < len(l) - 1 else l[n]
    return abs(sum(seq) - (n**2 + n)//2)

def find_missing(seq: List[int], n: int):
    return difference(seq, n)

def find_duplicate(seq: List[int], n: int):
    return difference(seq, n)