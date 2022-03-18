import random

# default_list = [default for default in range(1, 30)]
# n_limit = random.choice(default_list)
# number_list = [numb for numb in range(1, n_limit + 1)]
# number_list.remove(random.choice(number_list))
# number_list.reverse()

default_list = [default for default in range(1, 30)]
n_limit = random.choice(default_list)
number_list = [numb for numb in range(1, n_limit + 1)]
x = random.choice(number_list)
number_list.insert(x, x)
number_list.reverse()


def find_duplicate(seq, n: int) -> int:
    seq_sorted = sorted(seq)
    duplicate = 1
    m = 0
    duplicate_number = int
    for duplicate_search in range(len(seq_sorted)):
        if duplicate == seq_sorted[m]:
            duplicate += 1
            m += 1
        else:
            duplicate_number = duplicate - 1
    return duplicate_number


def find_missing(seq, n):
    seq_sorted = sorted(seq)
    miss = 1
    m = 0
    for search_miss in range(len(seq_sorted)):
        if miss == seq_sorted[m]:
            miss += 1
            m += 1
    return miss


if __name__ == '__main__':
    print(number_list, n_limit)
    print(find_missing(number_list, n_limit))
    print(number_list, n_limit)
    print(find_duplicate(number_list, n_limit))
