from typing import List


def find_missing(seq: List[int], n: int) -> int:
    for element in range(1, n + 1):
        if element not in seq:
            return element


def find_duplicate(seq: List[int], n: int) -> int:
    for index in range(n + 1):
        if seq[index] in seq[index + 1:]:
            return seq[index]
