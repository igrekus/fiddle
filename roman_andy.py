from functools import lru_cache

int2roman = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
    20: 'XX',
    30: 'XXX',
    40: 'XL',
    50: 'L',
    60: 'LX',
    70: 'LXX',
    80: 'LXXX',
    90: 'XC',
    100: 'C',
    200: 'CC',
    300: 'CCC',
    400: 'CD',
    500: 'D',
    600: 'DC',
    700: 'DCC',
    800: 'DCCC',
    900: 'CM',
    1000: 'M',
    2000: 'MM',
    3000: 'MMM'
}


@lru_cache(maxsize=1)
def all_romans():
    return {to_roman(_): _ for _ in range(1, 4000)}


def to_roman(n: int) -> str:
    num_parts = list(filter(lambda x: x, [int(_ + '000'[:-i]) for i, _ in enumerate(str(n), start=1 - len(str(n)))]))
    return ''.join(int2roman.get(_) for _ in num_parts)


def parse_roman(roman: str) -> int:
    return all_romans().get(roman) or -1


if __name__ == '__main__':
    while 1:
        inp = input('Input integer (1..3999): ')
        to_r = to_roman(int(inp))
        print(inp, to_r, sep=' | ')

        # inp = input('Input valid roman value: ')
        # print(inp, parse_roman(inp), sep=' | ')

        # print(all_romans.cache_info())
