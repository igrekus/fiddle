# -*- coding: utf-8 -*-
import re
import json
from collections import defaultdict
from functools import singledispatch
from itertools import chain
from string import ascii_uppercase as uppercase


def text_to_pin_code(text):
    d = defaultdict(set)
    for el in (
            int(x) for x in (
            s for s in (
            chain(*(_normalize_value(v) for v in (
                    value for field, value in
                    json.loads(re.compile(r'^.*(?P<json>{.*}).*$', re.VERBOSE).match(text)['json']).items()
                    if set(field).intersection(uppercase)))))
            if s)):
        d[len(f'{el}')].add(el)
    return ''.join(f"{len(d.get(n_digit_num, set()))}" for n_digit_num in range(1, 5))


@singledispatch
def _normalize_value(value: int):
    return [f'{value}']


@_normalize_value.register
def _(value: str):
    return [''.join(filter(str.isdigit, f'{value}'))]


@_normalize_value.register
def _(value: list):
    return [''.join(filter(str.isdigit, f'{v}')) for v in value]
