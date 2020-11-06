"""
1. Света и остановки

Остановки расставлены через каждые k метров, Света прошла n метров. Написать функцию,
принимающую на вход `k` и `n` и возвращающую расстояние до ближайшей к Свете остановки.

Сигнатура функции:
```
    def nearest_bus_stop(k: int, n: int) -> int:
        ...
```
    гбе:
        `k`, `n` - натуральное число

    Пример:
```
    >>> nearest_bus_stop(600, 2000)
    200
```
"""

from itertools import count
nearest_bus_stop = lambda k, n: next(min(k * i - n, abs(k * i - k - n)) for i in count() if k * i > n)
print(nearest_bus_stop(k=600, n=2000))

"""
2. Круассаны и эклеры

На складе лежит `a` круассанов и `b` эклеров, которые необходимо упаковать в коробки.
В каждой коробке должны быть оба вида пирожных, две штуки одного вида и одна штука второго.
Написать функцию, принимающую на вход `a` и `b` и возвращающую результат упаковки:

    * `[m, n]`, где:
        `m` - количество коробок, в которых находится два круассана и один эклер;
        `n` - количество коробок, в которых находится два эклера и один круассан; 
    * `None`, если упаковка пирожных в коробки согласно приведённому правилу невозможна без остатка
    
Сигнатура функции:
```
    def pack_pastry(a: int, b: int) -> Optional[Tuple[int]]
        ...
```
    где:
        `a`, `b` - натуральное число
    
    Пример:
```    
    >>> pack_pastry(4, 5)
    (!, 2)
    
    >>> pack_pastry(3, 5)
    None
```
"""
pack_pastry = lambda a, b:\
    None if abs(a - b) != 1 else (lambda com: (com + 1, com) if a - b > 0 else (com, com + 1))(max(a // 3, b // 3))
print(pack_pastry(a=4, b=5))

"""
3. Шахматы

На шахматной доске произвольных размеров стоят небьющие друг друга ладьи.
Шахматную доску повернули на 90 градусов по часовой стрелке, напишите функцию,
которая принимает описание расстановки ладей до поворота и возвращает описание расстановки ладей после поворота доски.
Местоположение фигур кодируется последовательностью натуральных чисел,
позиция которых в последовательности кодирует ряд, а значение -- столбец, в котором находится фигура.
Например, последовательность `[1, 2, 3]` кодирует следующую конфигурация доски:
```
  1 2 3
1 R x x
2 x R x
3 x x R
```

Сигнатура функции:
```
    def rotate_board(before: List[int]) -> List[int]:
    ...
```

Пример:
```
    >>> rotate_board([4, 2, 3, 5, 1])
    [1, 4, 3, 5, 2]
```
"""
rotate_board = lambda before: \
    [row.index(1) + 1 for row in list(zip(*reversed([[int(i == (v - 1)) for i in range(len(before))] for v in before])))]
print(rotate_board(before=[4, 2, 3, 5, 1]))

# # 5, cells
# from functools import partial
#
# raw = [
#     [1, 1, 3, 4, 7, 15],
#     [1, 1, 3, 4, 7, 16],
#     [1, 1, 3, 4, 7, 17],
#     [1, 1, 3, 8, 9, 17],
#     [1, 2, 2, 4, 8, 15],
#     [1, 1, 3, 4],
# ]
#
# res = [
#     [0, 0, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 1, 1, 1],
#     [0, 1, 1, 1, 1, 1]
# ]
#
# grow = lambda p, fs: p[1] > fs[0][1] if len(fs) == 1 else \
#     (lambda head, *tail: grow((p[0], p[1] + head[1]) if p[1] > head[1] and p[0] != head[0] else p, tail))(*fs)
#
# can_win = lambda pls: list((lambda ps: map(int, map(partial(grow, fs=ps), ps)))(list(enumerate(pls))))
#
#
# for rw, rs in zip(raw, res):
#     cw = can_win(rw)
#     assert cw == rs, f'{cw} {rs}'
#     print(rw, cw)

# # 3. chess
# n = 5
# raw = [4, 2, 3, 5, 1]
# res = [1, 4, 3, 5, 2]
# result = lambda r: [row.index(1) + 1 for row in list(zip(*[[int(i == (v - 1)) for i in range(n)] for v in r][::-1]))]
# print(result(raw))

import math

num_coords = lambda x: \
    (lambda side:
     (lambda dir, start:
      [(idx + 1, side) if dir else (side, idx + 1) for idx, v in
       enumerate(range(start, start + side)) if v == x][0]
      if x <= start + (side ** 2 - start + 1) // 2
      else
      [(side, side - idx - 1) if dir else (side - idx - 1, side) for idx, v in
       enumerate(range(start + side, side ** 2 + 1)) if v == x][0])
     (side % 2 == 0, (side - 1) ** 2 + 1))(math.ceil(math.sqrt(x)))

coords = [(i, num_coords(i)) for i in range(1, 37)]
res = [(1, (1, 1)), (2, (1, 2)), (3, (2, 2)), (4, (2, 1)), (5, (3, 1)), (6, (3, 2)), (7, (3, 3)), (8, (2, 3)),
       (9, (1, 3)), (10, (1, 4)), (11, (2, 4)), (12, (3, 4)), (13, (4, 4)), (14, (4, 3)), (15, (4, 2)), (16, (4, 1)),
       (17, (5, 1)), (18, (5, 2)), (19, (5, 3)), (20, (5, 4)), (21, (5, 5)), (22, (4, 5)), (23, (3, 5)), (24, (2, 5)),
       (25, (1, 5)), (26, (1, 6)), (27, (2, 6)), (28, (3, 6)), (29, (4, 6)), (30, (5, 6)), (31, (6, 6)), (32, (6, 5)),
       (33, (6, 4)), (34, (6, 3)), (35, (6, 2)), (36, (6, 1))]

print(coords)
for c, r in zip(coords, res):
    assert c == r, f'should be equal {c} != {r}'
