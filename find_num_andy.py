from typing import List


def find_missing(seq: List[int], n: int) -> int:
    return sum(range(1, n + 1)) - sum(seq)


def find_duplicate(seq: List[int], n: int) -> int:
    return sum(seq) - sum(range(1, n + 1))