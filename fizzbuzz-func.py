from functools import update_wrapper


class pipe:
    def __init__(self, fun):
        self.fun = fun
        update_wrapper(self, fun)

    def __ror__(self, other):
        return self.fun(other)

    def __call__(self, *args, **kwargs):
        return pipe(lambda x: self.fun(x, *args, **kwargs))


def fizzbuzz(num):
    return {
        (True, True): 'fizzbuzz',
        (True, False): 'fizz',
        (False, True): 'buzz',
    }.get((num % 3 == 0, num % 5 == 0), num)


@pipe
def fbmap(stream):
    yield from (fizzbuzz(el) for el in stream)


@pipe
def fbprint(steam):
    return [print(el) for el in steam]


if __name__ == '__main__':
    range(1, 16) \
        | fbmap \
        | fbprint
