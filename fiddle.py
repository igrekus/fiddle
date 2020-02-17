# Код хранится в текстовом файле, который помимо случайного текста содержит также и json,
# в котором есть все нужные данные (остальная информация не важна)
# В каждом файле гарантированно находится только 1 json, но он(жсон) может быть и пустым (в таком случае пин-код '0000').
# В файле гарантированно нет больше фигурных скобок, кроме тех, что обрамляют json. Жсон гарантированно даст валидный пин-код.
# Необходимые числа находятся только в тех парах ключ-значение, в которых ключ содержит хотя бы 1 заглавную букву (далее "значимые поля")
# Результат работы нашей программы это строка содержащая 4 цифры от '0000' до '9999', где первая цифра это количество уникальных однозначных чисел во всех значимых полях,
# вторая цифра это количество уникальных двузначных и так далее.
# Каждое значимое поле содержит минимум 1 число (не может не содержать чисел)
# Значения могут быть целым числом, строкой или списком.
# Если значение представлено строкой, то она может содержать только 1 число, но его цифры могут быть разделены любыми занками,
# например '2 3 4 '=234
# Если значение представлено целым числом то оно обязательно будет положительным
# Список обязательно содержит хоть 1 число, но не обязан содержать только числа, список не может содержать другие коллекции (списки,словари и т.п.),
# Например [1, '2', 'f'] - валидный список, который дает 1 и 2
# Пример
# если на вход подается текст 'example test for testing {"fieldOne":1, "fields":2, "fielD":[1,"22", "e3r4"], "fieldN":"2 3 4"} more unnecessary data'
# то ответ '1210'

# + 1 extract json (only one json, may be empty)
# + 2 extract value fields -- fields with at least one uppercase letter, guaranteed to have at least one number
# + 3 normalize fields (one int, one list, one string) -> set of nums:
#   + int, guaranteed to be positive
#   + string, filter and concat digits: '2 3 4 ' -> 234
#   + list, guaranteed to be flat, [1, '2', 'f'] -> [1, 2]
# + 4 collect info from normalized fields
# + 5 extract result from collected info
# + 6 return -- string with 4 digits, 1st - n of unique one-digit nums, 2nd -- n of unique two-digit nums, etc.
import re
import json
import string
from functools import singledispatch
from collections import defaultdict
from itertools import chain

test_str = 'example test for testing {"fieldOne":1, "fields":2,\n"fielD":[1,"22", "e3r4"], "fieldN":"2 3 4"} more unnecessary data'
upper_set = set(string.ascii_uppercase)


def _extract_json(raw_str):
    return re.compile('^.*(?P<json>{.+?}).*$').match(raw_str.replace('\n', ' '))['json']


def _filter_value_fields(raw: dict):
    return [v for k, v in raw.items() if set(k).intersection(upper_set)]


def _filter_digits(st):
    return int(''.join(filter(str.isdigit, st)))


def _normalize_list_value(lv):
    return [v if isinstance(v, int) else _filter_digits(v) for v in lv]


@singledispatch
def _normalize_value(value: int):
    return [value]


@_normalize_value.register
def _(value: str):
    return [_filter_digits(value)]


@_normalize_value.register
def _(value: list):
    return _normalize_list_value(value)


def _normalize_values(raw: list):
    return [o for o in chain(*(_normalize_value(v) for v in raw))]


def _separate_by_digit_number(raw: list):
    d = {i + 1: set() for i in range(4)}
    for el in raw:
        d[len(f'{el}')].add(el)
    return d


def _extract_pin(raw: dict):
    return ''.join([f'{len(v)}' for k, v in raw.items()])


def text_to_pin_code(text: str) -> str:
    js = json.loads(_extract_json(text))
    filtered = _filter_value_fields(js)
    normalized = _normalize_values(filtered)
    separated = _separate_by_digit_number(normalized)
    pin = _extract_pin(separated)
    print('\nfilt', filtered)
    print('normd', normalized)
    print('septd', separated)
    return pin


if __name__ == '__main__':
    print(text_to_pin_code(test_str))
