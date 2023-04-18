import random
import argparse

from typing import Set

import openpyxl


def _gen_strings(chars: str, length: int, count: int) -> Set[str]:
    ids = set()
    while len(ids) < count:
        ids.add(''.join(random.choices(chars, k=length)))
    return ids


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Generate random strings from a given set of characters')
    parser.add_argument('chars', help='available characters')
    parser.add_argument('length', type=int, help='number of characters in one string')
    parser.add_argument('count', type=int, help='number of strings to generate')
    args = parser.parse_args()

    print('Generating strings...')
    ids = list(_gen_strings(args.chars, args.length, args.count))

    print('Saving to .txt')
    with open('id_list.txt', 'wt') as f:
        f.write('\n'.join(ids))

    print('Saving to .xlsx')
    wb = openpyxl.Workbook()
    sheet = wb.active
    for id_ in ids:
        sheet.append([id_])
    wb.save('id_list.xlsx')

    print('All done')
