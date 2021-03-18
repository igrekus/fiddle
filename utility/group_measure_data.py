import os
import sys

import pandas as pd

from collections import defaultdict


def _get_raw_strings(source):
    with open(source, mode='rt', encoding='utf-8') as f:
        return [s.strip() for s in f.readlines()]


def _group_by_remarks(lines):
    res = []
    group = []
    for line in lines:
        if line.startswith('Remarks'):
            res.append(group)
            group = list()
        group.append(line)
    return res[1:]


def _split_into_datasets(raw):
    grouped_raw = defaultdict(list)
    for g in raw:
        _, name = g[0].split(',')
        prefix = name.split('-')[0][:-2]
        suffix = name.split('_')[-1]
        dataset_name = f'{prefix}{suffix}'
        grouped_raw[dataset_name].append(g)
    return grouped_raw


def _extract_headers(raw):
    out = {}
    for key, value in raw.items():
        out[key] = [_tidy_data(v) for v in value]
    return out


def _tidy_data(dirty_data):
    header, _, *data = dirty_data
    header = header.split(',')[1]
    return [header, *data]


def _prepare_datasets(tidy_data):
    out = []
    for key, value in tidy_data.items():
        volts = [v.split(',')[0] for v in value[0][1:]]
        headers = [v[0] for v in value]
        data = [[v.split(',')[1] for v in vals[1:]] for vals in value]
        out.append({
            'filename': key,
            'volts': volts,
            'headers': headers,
            'data': data
        })
    return out


def _make_dataframes(prepared_datasets):
    out = []
    for ds in prepared_datasets:
        df = pd.DataFrame({
            'Remarks': ds['volts'],
            **dict(zip(ds['headers'], ds['data']))
        })
        df = df.applymap(lambda x: float(x))
        out.append([ds['filename'], df])
    return out


def _export_to_files(dfs):
    txt = 'txt'
    excel = 'excel'
    os.makedirs(txt, exist_ok=True)
    os.makedirs(excel, exist_ok=True)

    for file, df in dfs:
        print(f'exporting {file}')
        df.to_csv(f'{txt}/{file}.txt', index=False)
        df.to_excel(f'{excel}/{file}.xlsx', index=False, engine='openpyxl')


def main(path):
    print(f'reading {path}')
    raw_lines = _get_raw_strings(path)
    grouped_lines = _group_by_remarks(raw_lines)
    grouped_datasets = _split_into_datasets(grouped_lines)
    with_headers = _extract_headers(grouped_datasets)
    prepared_datasets = _prepare_datasets(with_headers)
    dfs = _make_dataframes(prepared_datasets)

    print('writing files')
    _export_to_files(dfs)


if __name__ == '__main__':
    main(sys.argv[1])
