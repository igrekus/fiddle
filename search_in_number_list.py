'''
Дано: список n-1 чисел от 1 до n включительно, в котором отсутствует одно из чисел.
Написать функцию, определяющую отсутствующее число:
    def find_missing(seq: List[int], n: int) -> int:
        ...
Дано: список n + 1 чисел от 1 до n включительно, в котором одно из чисел продублировано.
Написать функцию, определяющую продублированное число:
    def find_duplicate(seq: List[int], n[int]) -> int:
        ...
* Решить задачу без унылого алгоритма на сетах.
'''

import random
default_list = [default for default in range(1, 30)]
n_limit = random.choice(default_list)
number_list = [numb for numb in range(1, n_limit)]
number_list.remove(random.choice(number_list))


def find_missing(seq, n: int) -> int:
    miss = 1
    m = 0
    for miss_search in range(len(sorted(seq))):
        if miss == seq[m]:
            miss += 1
            m += 1
    return miss


def find_duplicate(seq, n: int) -> int:
    duplicate = 1
    m = 0
    duplicate_number = 0
    for duplicate_search in range(len(sorted(seq))):
        if duplicate == seq[m]:
            duplicate += 1
            m += 1
        else:
            duplicate_number = duplicate - 1
    return duplicate_number


if __name__ == '__main__':
    print(number_list, n_limit)
    print(find_missing(number_list, n_limit))

