import numpy as np


def dimension(dim):
    res = np.eye(dim * 2 - 1, k=dim - 1, dtype=int) | np.eye(dim * 2 - 1, k=1 - dim, dtype=int)
    res[1:dim - 1] |= res[dim:-1][::-1, :]
    res[dim:-1] |= res[1:dim - 1][::-1, :]
    return res


for dim in [1, 3, 4]:
    print(f'{dim=}\n', dimension(dim))


def veclen(arr: np.ndarray):
    return np.apply_along_axis(lambda ar: np.sqrt(np.sum(np.power(ar, 2))), 1, arr)


inp = np.array([[1, 1, 1], [2, 2, 2], [1, 1, 1]])
outp = veclen(inp)
print('in=\n', inp)
print('out=\n', outp)
