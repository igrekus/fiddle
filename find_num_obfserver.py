import random


def find_missing(seq):
    print(*set(list(range(1, len(seq)))).difference(seq))


def find_duplicate(seq):
    print([x for x in seq if seq.count(x) >= 2][1])


#n = 1000


#find_duplicate код для тестирования
#Z = list(range(1,n))
#Z.append(random.randint(1,n))

#find_duplicate(Z)


#find_missing код для тестирования
#L = list(range(1,n))
#L.remove(random.randint(1,n))

#find_missind(L)
