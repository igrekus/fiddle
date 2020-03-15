# -*- coding: utf-8 -*-
import re
import json
from functools import singledispatch
from itertools import chain, groupby
from string import ascii_uppercase as uppercase


def text_to_pin_code(text):
    return ''.join(f"{len({n: set(vals) for n, vals in groupby(sorted((int(x) for x in (s for s in (chain(*(_normalize_value(v) for v in (value for field, value in json.loads(re.compile(r'^.*(?P<json>{.*}).*$', re.VERBOSE).match(text)['json']).items()if set(field).intersection(uppercase))))) if s))), key=lambda x: len(f'{x}'))}.get(n_digit_num, set()))}" for n_digit_num in range(1, 5))


@singledispatch
def _normalize_value(value: int):
    return [f'{value}']


@_normalize_value.register
def _(value: str):
    return [''.join(filter(str.isdigit, f'{value}'))]


@_normalize_value.register
def _(value: list):
    return [''.join(filter(str.isdigit, f'{v}')) for v in value]
