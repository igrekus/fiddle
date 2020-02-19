# -*- coding: utf-8 -*-

"""
PIN code extractor module.

Implements the extraction of a PIN code from the passed string according to the rules:

    - input utf-8 string is guaranteed to contain only one standard-compliant JSON in the serialized form
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

Example:

    The module is to be used from a user script:

        from text_to_pin_code import text_to_pin_code

        print(text_to_pin_code('{}'))   # prints 0000

Functions with names starting with an underscore are intended for internal use and thus are not being a part of
the public API.

TODO:
- newlines?
- more than 9 entries?
- only [str, int] in list, no float, complex, decimal?
"""

import re
import json
from collections import defaultdict
from functools import singledispatch
from itertools import chain
from string import ascii_uppercase as uppercase
from typing import List, Iterator, Dict, Union


def text_to_pin_code(text: str) -> str:
    """
    Implements the PIN-code extractor as per rules defined in the module docstring.

    Part of the module public API.

    :param text: utf-8 string containing encoded PIN
    :return: string of four digits according to the encoding rules
    """
    return _get_pin(
        _extract_nums(
            _filter_pin_fields(
                json.loads(
                    _extract_json_string(text)))))


def _get_pin(num_container: Dict[int, set]) -> str:
    """
    Helper function, extracts target PIN code from the intermediate data structure.
    """
    return ''.join(f'{len(num_container.get(n_digit_num, set()))}' for n_digit_num in range(1, 5))


def _extract_nums(raw) -> Dict[int, set]:
    """
    Helper function, abstracts away number extraction steps.
    """
    return _pack_numbers(_get_numbers(raw))


def _pack_numbers(raw: Iterator[int]) -> Dict[int, set]:
    """
    Helper function, packs normalized numbers encoding PIN into an intermediate data structure.
    """
    d = defaultdict(set)
    for el in raw:
        d[len(f'{el}')].add(el)
    return d


def _get_numbers(raw: Iterator[Union[int, str, List[Union[int, str]]]]) -> Iterator[int]:
    """
    Helper function, extracts numbers from filtered JSON fields.
    """
    return _to_int(_remove_empty(_normalize_values(raw)))


def _to_int(raw: Iterator[str]) -> Iterator[int]:
    return (int(x) for x in _remove_empty(raw))


def _remove_empty(raw: Iterator[str]) -> Iterator[str]:
    return (s for s in raw if s)


def _normalize_values(raw: Iterator[Union[int, str, List[Union[int, str]]]]) -> Iterator[str]:
    """
    Helper function, normalizes all types of pin field values to a list of strings.
    """
    return chain(*(_normalize_value(v) for v in raw))


@singledispatch
def _normalize_value(value: int) -> List[str]:
    """
    Helper function, normalizes int type values.
    """
    return [f'{value}']


@_normalize_value.register
def _(value: str) -> List[str]:
    """
    Overload, normalizes str type values.
    """
    return [_filter_digits(value)]


@_normalize_value.register
def _(value: list) -> List[str]:
    """
    Overload, normalizes list type values.
    """
    return [_filter_digits(f'{v}') for v in value]


def _filter_digits(st: str) -> str:
    """
    Helper function, filters out everything except digits.
    """
    return ''.join(filter(str.isdigit, st))


def _filter_pin_fields(raw: dict) -> Iterator[Union[int, str, List[Union[int, str]]]]:
    """
    Helper function, filters out non-significant fields from the input dictionary.
    Significant field key must contain at least one latin upper case letter.
    """
    return (value for field, value in raw.items() if set(field).intersection(uppercase))


def _extract_json_string(raw_str: str) -> str:
    """
    Helper function, extracts a string between the '{' and '}' including these characters.
    """
    json_regex = re.compile(r'''^             # start of the input string    
                            .*                # any character up until the first '{'
                            (?P<json>{.*})    # capture a string between the '{' and '}' into a named group ('json')
                            .*                # any character until the end of the string
                            $                 # end of the string
                            ''', re.VERBOSE)
    return json_regex.match(raw_str.replace('\n', ' '))['json']
