import math

from typing import Tuple, Optional, List

__all__ = [
    'nearest_bus_stop',
    'pack_pastry',
    'rotate_board',
    'locate_number',
    'find_winners'
]


def nearest_bus_stop(k: int, n: int) -> int:
    sections = n // k
    distance = k * sections
    return min(abs(distance - n), abs(distance - n + k))


def pack_pastry(a: int, b: int) -> Optional[Tuple[int, int]]:
    diff = a - b
    if diff == 0:
        return a // 3, b // 3
    if abs(diff) != 1:
        return None
    common = max(a // 3, b // 3)
    if diff > 0:
        return common + 1, common
    return common, common + 1


def rotate_board(before: List[int]) -> List[int]:
    return _encode(_transpose(reversed(_decode(encoded=before, side=len(before)))))


def _transpose(board):
    return list(zip(*board))


def _decode_row(value, side):
    row = [0] * side
    row[value - 1] = 1
    return row


def _decode(encoded, side):
    return [_decode_row(v, side) for v in encoded]


def _encode(board):
        return [row.index(1) + 1 for row in board]


def locate_number(x: int) -> Tuple[int, int]:
    side = math.ceil(math.sqrt(x))
    direction = side % 2 == 0
    start = (side - 1) ** 2 + 1
    half_point = start + (side ** 2 - start + 1) // 2

    if x <= half_point:
        for idx, v in enumerate(range(start, start + side)):
            if v != x:
                continue
            if direction:
                return idx + 1, side
            return side, idx + 1

    for idx, v in enumerate(range(start + side, side ** 2 + 1)):
        if v != x:
            continue
        if direction:
            return side, side - idx - 1
        return side - idx - 1, side


def find_winners(players: List[int]) -> List[int]:
    numbered = [list(p) for p in enumerate(players)]
    return [int(_grow(player, food=numbered)) for player in numbered]


def _grow(player, food):
    target = food[0]
    if len(food) == 1:
        return player[1] > target[1]
    updated_player = player
    if player[1] > target[1] and player[0] != target[0]:
        updated_player = [player[0], player[1] + target[1]]
    return _grow(updated_player, food[1:])
