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

# TODO:
# newlines?
# more than 9 entries?
# only [str, int] in list, no float, complex, decimal?
#

import re
import json
from collections import defaultdict
from functools import singledispatch
from itertools import chain
from string import ascii_uppercase as uppercase
from typing import List, Iterator, Dict


def text_to_pin_code(text: str) -> str:
    """
    Extracts the PIN code from the passed string. PIN code is encoded according to the rules:

    - guaranteed to contain only one standard-compliant JSON in the serialized form
    - JSON may or may not be empty
    - JSON field containing at least one uppercase latin letter guaranteed to be a part of the encoded PIN (pin field)
    - pin field guaranteed to contain at least one significant number
    - pin field may have the type of:
        * int
        * str
        * List[str, int]
    - int pin field guaranteed to be positive
    - str pin field guaranteed to contain only one number but it's digits may be separated by an arbitrary string
    - list pin field guaranteed to not contain other collections
    - list pin field guaranteed to have at least one encoding number
    - list pin field may contain strings including encoding numbers in string form

    The resulting PIN is a string of four digits, where the first digit is the number of unique single decimal place
    numbers, second digit is the number of two decimal place numbers, etc.

    Part of the public API.

    :param text: utf-8 string containing encoded PIN
    :return: string of four digits according to the encoding rules
    """
    return _extract_pin(
        _separate_numbers(
            _normalize(
                _filter_value_fields(
                    json.loads(
                        _extract_json_string(text))))))


def _extract_pin(num_container: dict) -> str:
    """
    Helper function, extracts target PIN code from the intermediate data structure.

    Not a part of the public API.
    """
    return ''.join(f'{len(num_container.get(n_digit_num, set()))}' for n_digit_num in range(1, 5))


def _separate_numbers(raw: Iterator) -> Dict[int, set]:
    """
    Helper function, separates normalized values by the number of digits into an intermediate data structure.

    Not a part of the public API.
    """
    d = defaultdict(set)
    for el in raw:
        d[len(f'{el}')].add(el)
    return d


def _normalize(raw: Iterator) -> Iterator:
    return _to_int(_filter_empty(_normalize_values(raw)))


def _to_int(raw: Iterator) -> Iterator:
    """
    Helper function, normalizes passed list of values into an iterable of strings.

    Not a part of the public API.
    """
    return (int(x) for x in _filter_empty(raw))


def _filter_empty(raw: Iterator) -> Iterator:
    return filter(bool, raw)


def _normalize_values(raw: Iterator) -> Iterator:
    return chain(*(_normalize_value(v) for v in raw))


@singledispatch
def _normalize_value(value: int) -> List[str]:
    """
    Helper function, normalizes int type values.

    Not a part of the public API.
    """
    return [f'{value}']


@_normalize_value.register
def _(value: str) -> List[str]:
    """
    Overload, normalizes str type values.

    Not a part of the public API.
    """
    return [_filter_digits(value)]


@_normalize_value.register
def _(value: list) -> List[str]:
    """
    Overload, normalizes list type values.

    Not a part of the public API.
    """
    return [_filter_digits(f'{v}') for v in value]


def _filter_digits(st: str) -> str:
    """
    Helper function, filters out everything except digits.

    Not a part of the public API.
    """
    return ''.join(filter(str.isdigit, st))


def _filter_value_fields(raw: dict) -> Iterator:
    """
    Helper function, filters out non-significant fields from the input dictionary.
    Significant field key must contain at least one latin upper case letter.

    Not a part of the public API.
    """
    return [value for field, value in raw.items() if set(field).intersection(uppercase)]


def _extract_json_string(raw_str: str) -> str:
    """
    Helper function, extracts a string between the '{' and '}' including these characters.

    Not a part of the public API.
    """
    json_regex = re.compile(r'''^             # start of the input string    
                            .*                # any character up until the first '{'
                            (?P<json>{.*})    # capture a string between the '{' and '}' into a named group ('json')
                            .*                # any character until the end of the string
                            $                 # end of the string
                            ''', re.VERBOSE)
    return json_regex.match(raw_str.replace('\n', ' '))['json']
