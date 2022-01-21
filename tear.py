import os

import pandas as pd
import seaborn as sb

from io import BytesIO
from pathlib import Path

from forgot_again.file import make_dirs

path = r'D:\work\python\nb\tear_plots\data'


def _get_dirs(path):
    for d in os.listdir(path):
        d = os.path.join(path, d)
        if os.path.isdir(d):
            yield d


def _get_files(path, ext):
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isfile(f) and f.lower().endswith(ext.lower()):
            yield f


def _parse_file(path, folder):
    p = Path(path)
    batch, measure = p.parts[-2:]
    measure = measure.lower().replace('.csv', '')
    with open(path, mode='rt', encoding='ascii') as f:
        bs = BytesIO(''.join(filter(bool, (l.replace('\x00', '') for l in f.readlines()))).encode('ascii'))
        df = pd.read_csv(bs, sep=';')
        df.columns = ['F(N)', 'L(mm)']
        df = df[df['L(mm)'] != 0]

        df = pd.concat([pd.DataFrame([{'F(N)': 0, 'L(mm)': 0}]), df], ignore_index=True)
        df.reset_index()

        df['measure'] = int(measure)
        df['batch'] = batch
        df['fdiff'] = df['F(N)'].diff()
        df['ldiff'] = df['L(mm)'].diff()
        df['deriv'] = df['fdiff'] / df['ldiff']
        df.to_excel(f'{folder}/{measure}.xlsx', engine='openpyxl', index=False)

    # ax = sb.lineplot(data=df, x='L(mm)', y='F(N)', label='raw', ax=None)
    # ax.set(xlim=(0, 4))
    # fig = ax.get_figure()
    # fig.savefig(f'{folder}/{measure}.png', dpi=200)
    # fig.clf()
    return df


def filter_df(df, folder):
    fs = df['F(N)'].values.tolist()
    ls = df['L(mm)'].values.tolist()
    ds = df['deriv'].values.tolist()
    measure = df['measure'][0]
    batch = df['batch'][0]
    tmp = []

    prev = ls[0]
    remove_indexes = set()
    for i, (f, d) in enumerate(zip(fs, ds)):
        if d == 0:
            delta = ls[i] - prev
            for j in range(i, len(ls)):
                ls[j] -= delta
            remove_indexes.add(i)
            continue
        tmp.append([f, d])
        prev = ls[i]
    ls = [el for i, el in enumerate(ls) if i not in remove_indexes]

    res = [[l, *r] for l, r in zip(ls, tmp)]
    out_df = pd.DataFrame(res, columns=['L(mm)', 'F(N)', 'deriv'])
    out_df['batch'] = batch
    out_df['measure'] = measure
    out_df.to_excel(f'{folder}/{measure:08d}_filtered.xlsx', engine='openpyxl', index=False)

    # ax = sb.lineplot(data=out_df, x='L(mm)', y='F(N)', label='filtered', ax=None)
    # ax.set(xlim=(0, 4))
    # fig = ax.get_figure()
    # fig.savefig(f'{folder}/{measure:08d}.png', dpi=200)
    # fig.clf()
    return out_df


master = pd.DataFrame()
master_filtered = pd.DataFrame()
for d in list(_get_dirs(path)):
    print(f'directory {d}')

    p = Path(d)
    batch = p.parts[-1]
    folder = p.joinpath('xlsx')
    make_dirs(folder)

    batch_df = pd.DataFrame()
    batch_df_filtered = pd.DataFrame()
    for f in list(_get_files(d, '.csv')):
        print(f'file {f}')

        df = _parse_file(f, folder)
        filtered_df = filter_df(df, folder)
        batch_df = batch_df.append(df)
        batch_df_filtered = batch_df_filtered.append(filtered_df)

    master = master.append(batch_df)
    master_filtered = master_filtered.append(batch_df_filtered)
    batch_df.to_excel(f'{folder}/{batch}.xlsx', engine='openpyxl', index=False)
    batch_df_filtered.to_excel(f'{folder}/{batch}_filtered.xlsx', engine='openpyxl', index=False)

master.to_excel(f'master.xlsx', engine='openpyxl', index=False)
master_filtered.to_excel(f'master_filtered.xlsx', engine='openpyxl', index=False)

# def filt(df):
#     fs = df['F(N)'].values.tolist()
#     ls = df['L(mm)'].values.tolist()
#     ds = df['deriv'].values.tolist()
#     measure = df['measure'][0]
#     batch = df['batch'][0]
#     tmp = []
#
#     prev = ls[0]
#     remove_indexes = []
#     for i, (f, d) in enumerate(zip(fs, ds)):
#         if d == 0:
#             delta = ls[i] - prev
#             for j in range(i, len(ls)):
#                 ls[j] -= delta
#             remove_indexes.append(i)
#             continue
#         tmp.append([f, d])
#         prev = ls[i]
#
#     remove_indexes = set(remove_indexes)
#     ls = [el for i, el in enumerate(ls) if i not in remove_indexes]
#
#     res = [[l, *r] for l, r in zip(ls, tmp)]
#     out_df = pd.DataFrame(res, columns=['L(mm)', 'F(N)', 'deriv'])
#     out_df['batch'] = batch
#     out_df['measure'] = measure
#     return out_df
#
# df = pd.read_excel(r'D:\work\python\fiddle\00000369.xlsx')
#
# f = filt(df)
#
# f.to_excel('out.xlsx', index=False)
#
# ax = sb.lineplot(data=f, x='L(mm)', y='F(N)', label='filtered', ax=None)
# sb.lineplot(data=df, x='L(mm)', y='F(N)', label='filtered', ax=None)
# ax.set(xlim=(0, 4))
# fig = ax.get_figure()
# fig.savefig(f'out.png', dpi=200)
# fig.clf()
# print(f)
