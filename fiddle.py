s1 = '123456789'
s2 = '123567894'


def _recur(seq):
    if len(list(seq)) == 2:
        first, last = seq
        return first < last and last - first == 1
    head, next, *tail = seq
    return head < next and next - head == 1 and _recur([next] + tail)


def check(seq, n: int) -> bool:
    return _recur(list(map(int, seq)))


print(check(s1, 1))
