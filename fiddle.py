import collections

c = collections.Counter([1, 1, 1, 1, 2, 2, 2, 3, 3])

for num, times in c.items():
    for index in range(times):
        print(f'{num} - {index + 1}')
