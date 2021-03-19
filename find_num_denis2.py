from typing import List


def find_missing(seq: List[int], n: int) -> int:
    seq_dict = {v: v for v in seq}
    for num in range(1, n + 1):
        if not seq_dict.get(num, False):
            return num


def find_duplicate(seq: List[int], n: int) -> int:
    seq_dict = dict()
    for num in seq:
        if seq_dict.get(num, False):
            return num
        else:
            seq_dict[num] = num
