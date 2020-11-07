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
    (1, 2)
    
    >>> pack_pastry(3, 5)
    None
```
"""
pack_pastry = lambda a, b:\
    (a // 3, b // 3) if a - b == 0 else \
        None if abs(a - b) != 1 else \
            (lambda com: (com + 1, com) if a - b > 0 else (com, com + 1))(max(a // 3, b // 3))

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

"""
4. Число в ячейке

Дана бесконечная таблица, заполенная натуральными числами следующим образом:
```
   1  2  3  4  5  6
------------------- 
1| 1  2  9 10 25 26
2| 4  3  8 11 24 ..
3| 5  6  7 12 23 ..
4|16 15 14 13 22 ..
5|17 18 19 20 21 ..
6|.. .. .. .. .. ..
```

Написать функцию, которая получает на вход натуральное число и возвращает его координаты в приведённой таблице,
в формате (строка, столбец).

Сигнатура функции:
```
    def locate_number(n: int) -> Tuple[int, int]
        ...
```
Пример:
```
    >>> locate_number(15)
    (4, 2)
```
"""
import math
locate_number = lambda x: \
    (lambda side:
     (lambda dir, start:
      [(idx + 1, side) if dir else (side, idx + 1) for idx, v in
       enumerate(range(start, start + side)) if v == x][0]
      if x <= start + (side ** 2 - start + 1) // 2
      else
      [(side, side - idx - 1) if dir else (side - idx - 1, side) for idx, v in
       enumerate(range(start + side, side ** 2 + 1)) if v == x][0])
     (side % 2 == 0, (side - 1) ** 2 + 1))(math.ceil(math.sqrt(x)))

"""
5. Agar.io

Дан список игроков игры Agar.io с размерами их персонажей.
Написать функцию, принимающую на вход заданный список игроков и возвращающую новый список,
в котором закодирована возможность победы для каждого из игроков.

Сигнатура функции:
```
    def find_winners(players: List[int]) -> List[int]
        ...
```
Пример:
```
    >>> find_winners(players=[1, 1, 3, 4])
    [0, 0, 1, 1]
```
"""
from functools import partial

grow = lambda p, fs: p[1] > fs[0][1] if len(fs) == 1 else \
    (lambda head, *tail: grow((p[0], p[1] + head[1]) if p[1] > head[1] and p[0] != head[0] else p, tail))(*fs)
find_winners = lambda pls: list((lambda ps: map(int, map(partial(grow, fs=ps), ps)))(list(enumerate(pls))))
can_win = lambda pls: list((lambda ps: map(int, map(partial(grow, fs=ps), ps)))(list(enumerate(pls))))
