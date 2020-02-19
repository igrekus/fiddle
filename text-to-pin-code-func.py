# -*- coding: utf-8 -*-
import re
import json
from collections import defaultdict
from functools import singledispatch, update_wrapper
from itertools import chain
from string import ascii_uppercase as uppercase


class pipe:
    def __init__(self, fun):
        self.fun = fun
        update_wrapper(self, fun)

    def __ror__(self, other):
        return self.fun(other)

    def __call__(self, *args, **kwargs):
        return pipe(lambda x: self.fun(x, *args, **kwargs))


def text_to_pin_code(text):
    return list(
        text
        | _to_json_string
        | _to_json
        | _filter_pin_fields
        | _normalize_values
        | _remove_empty
        | _to_int
        | _pack_numbers
        | _get_pin
    )[0]


@pipe
def _to_json_string(raw_str):
    yield from [re.compile(r'''^.*(?P<json>{.*}).*$''', re.VERBOSE).match(raw_str.replace('\n', ' '))['json']]


@pipe
def _to_json(json_str):
    yield from [json.loads(next(json_str))]


@pipe
def _filter_pin_fields(raw):
    yield from [(value for field, value in next(raw).items() if set(field).intersection(uppercase))]


@pipe
def _normalize_values(raw):
    yield from [chain(*(_normalize_value(v) for v in next(raw)))]


@singledispatch
def _normalize_value(value: int):
    return [f'{value}']


@_normalize_value.register
def _(value: str):
    return [_filter_digits(value)]


@_normalize_value.register
def _(value: list):
    return [_filter_digits(f'{v}') for v in value]


def _filter_digits(st):
    return ''.join(filter(str.isdigit, st))


@pipe
def _remove_empty(raw):
    yield from [(s for s in next(raw) if s)]


@pipe
def _to_int(raw):
    yield from [(int(x) for x in next(raw))]


@pipe
def _pack_numbers(raw):
    d = defaultdict(set)
    for el in next(raw):
        d[len(f'{el}')].add(el)
    yield from [d]


@pipe
def _get_pin(num_container):
    c = next(num_container)
    yield from [''.join(f'{len(c.get(n_digit_num, set()))}' for n_digit_num in range(1, 5))]
