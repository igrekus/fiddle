from typing import List


def find_missing(seq: List[int], n: int) -> int:
    if n < 50000:
        one_shot_one_kill = {v: v for v in range(1, n + 2)}
        for num in seq:
            del one_shot_one_kill[num]
        return tuple(one_shot_one_kill)[0]
    else:
        seq.sort()
        first, second = 0, 1
        for _ in range(n - 2):
            if seq[second] - seq[first] != 1:
                return seq[second] - 1
            first += 1
            second += 1


def find_duplicate(seq: List[int], n: int) -> int:
    seq_dict = dict()
    for num in seq:
        if seq_dict.get(num, False):
            return num
        else:
            seq_dict[num] = num
