from functools import partial


def fizz_buzz(fizz=3, buzz=5, seq=None):
    return '\n'.join(map(partial(lambda lo, hi, num: {
        (True, True): 'FizzBuzz',
        (True, False): 'Fizz',
        (False, True): 'Buzz',
    }.get((num % lo == 0, num % hi == 0), str(num)), fizz, buzz), seq if seq else range(1, 16)))


if __name__ == '__main__':
    print(fizz_buzz(seq=range(1, 31)))
