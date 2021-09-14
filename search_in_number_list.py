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
number_list = [numb for numb in range(1, (n_limit - 1) + 2)]
number_list.remove(random.choice(number_list))

'''
Унылый алгоритм на сетах, потому что могу
'''
def find_missing_set(seq: list[int], n: int) -> int:
    find_list = [find for find in range(1, n + 1)]
    miss_number = set.difference(set(find_list), set(seq))
    return miss_number.pop()

def find_missing(seq: list[int], n: int) -> int:
    miss = 1
    m = 0
    for miss_search in range(len(sorted(seq))):
        if miss == seq[m]:
            miss += 1
            m += 1
    return miss

if __name__ == '__main__':
    print(number_list)
    print(find_missing_set(number_list, n_limit))
    print(find_missing(number_list, n_limit))

