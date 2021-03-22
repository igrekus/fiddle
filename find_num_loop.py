def find_missing(seq, n):
    missing = 0
    for i in range(1, n + 1):
        missing ^= i
    for i in seq:
        missing ^= i
    return missing

find_duplicate = find_missing
