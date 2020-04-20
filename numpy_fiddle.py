import numpy as np


def dimension(dim):
    res = np.eye(dim * 2 - 1, k=dim - 1, dtype=int) | np.eye(dim * 2 - 1, k=1 - dim, dtype=int)
    return res | res[::-1, :]


for dim in [1, 3, 4]:
    print(f'{dim=}\n', dimension(dim))


def veclen(arr: np.ndarray):
    return np.apply_along_axis(lambda ar: np.sqrt(np.sum(np.power(ar, 2))), 1, arr)


inp = np.array([[1, 1, 1], [2, 2, 2], [1, 1, 1]])
outp = veclen(inp)
print('in=\n', inp)
print('out=\n', outp)
