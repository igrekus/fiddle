from typing import List


def find_missing(seq: List[int], n: int) -> int:
    return sum((range(n - len(seq), n + 1))) - sum(seq)


def find_duplicate(seq: List[int], n: int) -> int:
    return sum(seq) - sum((range((n + 1) - (len(seq) - 1), n + 1)))


if __name__ == '__main__':
    val_missing = find_missing([8, 9, 11, 12, 13], 13)
    print(val_missing)
    val_duplicate = find_duplicate([7, 8, 9, 10, 11, 12, 13, 13, 14, 15], 15)
    print(val_duplicate)
