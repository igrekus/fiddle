def find_missing(list_int: list, n):
    list_int.sort()
    missing = int(list_int[-1] * (list_int[-1] + list_int[0]) / 2 - sum(list_int))
    return missing


def find_duplicate(list_int: list, n):
    for i in list_int:
        if list_int.count(i) > 1:
            return i
