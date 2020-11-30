# Светофоры и девушка
def nearest_bus_stop(n, k):
    if (k - (k // n) * n) < (n - (k - (k // n) * n)):
        return (k - (k // n) * n)
    else:
        return (n - (k - (k // n) * n))


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


def rotate_board(before):
    N = len(before)
    ret = []
    ladies = {}
    res = [x for x in range(N, 0, -1)]
    for i in range(N):
        ladies[before[i]] = i + 1
    for i in range(1, N + 1):
        ret.append(res[ladies[i] - 1])
    return (ret)


#  Решетка с числами
def locate_number(n: int):
    x = 1
    while x ** 2 < n:
        x += 1
    delta = (x ** 2 - (x - 1) ** 2 - 1) / 2
    ad = x ** 2 - n
    if ad <= delta:
        if x % 2 == 0:
            return x, ad + 1
        else:
            return ad + 1, x
    elif ad == delta:
        return x, x
    else:
        if x % 2 == 0:
            return 2 * x - 1 - ad, x
        else:
            return x, 2 * x - 1 - ad


def find_winners(players):
    flag = 1
    N = len(players)
    ret = []
    res = []
    if players[-1] > players[0]:
        res.append(flag)
    else:
        flag = 0
        res.append(flag)
    for i in range(N - 2, -1, -1):
        if flag == 0:
            res.append(flag)
            continue
        else:
            if players[i] > players[0]:
                sum_weight_do_i = 0
                for j in range(i):
                    sum_weight_do_i += players[j]

                if players[i] + sum_weight_do_i > players[i + 1]:
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
