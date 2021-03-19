from typing import List


def find_missing(seq: List[int], n: int):
    seq.sort()
    for i in range(seq[0], seq[-1] + 1):
        if i not in seq:
            return i


def find_duplicate(seq: List[int], n: [int]):
    for i in seq:
        if seq.count(i) > 1:
            return i
