import random
default_list = [default for default in range(1, 30)]
n_limit = random.choice(default_list)
number_list = [numb for numb in range(1, n_limit + 1)]
x = random.choice(number_list)
number_list.insert(x, x)

def find_duplicate(seq: list[int], n: int) -> int:
    miss = 1
    m = 0
    miss_number = int
    for miss_search in range(len(sorted(seq))):
        if miss == seq[m]:
            miss += 1
            m += 1
        else:
            miss_number = miss - 1
    return miss_number

if __name__ == '__main__':
    print(number_list, n_limit)
    print(find_missing(number_list, n_limit))