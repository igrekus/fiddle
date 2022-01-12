"""
вытащить все подсписки в верхний уровень
[1, 2, [1, 4], 7] -> [1, 2, 1, 4, 7]
содержимое любое, вложенность неограничена
def flatten(seq): -> list
"""

from random import choice, shuffle

base_list = list(range(1, choice(range(7, 30))))
shuffle(base_list)
x_elements = choice(range(1, 10))
x = 0
for seq_list in base_list:
    while x <= x_elements:
        seq_ = list(range(1, choice(range(1, 10))))
        base_list.insert(choice(range(1, len(base_list))), seq_)
        x += 1


def flatten(seq):
    i = 0
    for j in range(len(seq)):
        for find_list in seq:
            if isinstance(find_list, list):
                if isinstance(find_list, list):
                    pos = seq.index(find_list)
                    find_list.reverse()
                    while find_list:
                        seq.insert(pos, find_list.pop(i))
                    seq.remove(find_list)
                else:
                    seq.remove(find_list)
            else:
                continue
    return seq


if __name__ == '__main__':
    print('base =', base_list)
    print('unpack =', flatten(base_list))
