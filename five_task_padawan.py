# Светофоры и девушка
def nearest_bus_stop(a, b):
    if (b - (b // a) * a) < (a - (b - (b // a) * a)):
        return (b - (b // a) * a)
    else:
        return (a - (b - (b // a) * a))


# Эклеры и пирожные
def pack_pastry(a: int, b: int):
    cor = [0, 0]
    if (a + b) % 3 != 0 or (b // a > 2) or (a // b > 2):
        return None
    else:
        ec = a
        pir = b
        while ec > 0 and pir > 0 and pir + ec >= 3:
            if ec > pir:
                ec -= 2
                pir -= 1
                cor[0] += 1
            else:
                ec -= 1
                pir -= 2
                cor[1] += 1
        if ec == 0 and pir == 0:
            return tuple(cor)
        else:
            return None


def rotate_board(l):
    N = len(l)
    ret = []
    ladies = {}
    res = [x for x in range(N, 0, -1)]
    for i in range(N):
        ladies[l[i]] = i + 1
    for i in range(1, N + 1):
        ret.append(res[ladies[i] - 1])
    return (ret)


#  Решетка с числами
def locate_number(N: int):
    x = 1
    while x ** 2 < N:
        x += 1
    delta = (x ** 2 - (x - 1) ** 2 - 1) / 2
    ad = x ** 2 - N
    if ad <= delta:
        if x % 2 == 0:
            return tuple([x, ad + 1])
        else:
            return tuple([ad + 1, x])
    elif ad == delta:
        return tuple([x, x])
    else:
        if x % 2 == 0:
            return tuple([2 * x - 1 - ad, x])
        else:
            return tuple([x, 2 * x - 1 - ad])


def find_winners(bakt):
    flag = 1
    N = len(bakt)
    ret = []
    res = []
    if bakt[-1] > bakt[0]:
        res.append(flag)
    else:
        flag = 0
        res.append(flag)
    for i in range(N - 2, -1, -1):
        if flag == 0:
            res.append(flag)
            continue
        else:
            if bakt[i] > bakt[0]:
                sum_weight_do_i = 0
                for j in range(i):
                    sum_weight_do_i += bakt[j]

                if bakt[i] + sum_weight_do_i > bakt[i + 1]:
                    res.append(flag)
                    continue
                else:
                    flag = 0
                    res.append(flag)
                    continue
            else:
                flag = 0
                res.append(flag)
                continue
    for i in range(N - 1, -1, -1):
        ret.append(res[i])
    return ret
