from typing import List

def find_difference(seq: List[int], n: int):
    return abs(sum(seq) - (n**2 + n)//2)

find_duplicate = find_missing = find_difference

#Solution using lamba function
#find_difference: Callable[[List[int], int], int] = lambda seq, n: abs(sum(seq) - (n**2 + n)//2) 