import os
import tarfile
import zipfile


root_arc = 'find_the_key.tar.bz2'
current_dir = 'data'
temp = 'temp'

wrong_file = [
    'Key in another file',
    "It's not the file you're looking for",
    'The key is somewhere but not here',
]


def filter_files(l):
    return [f for f in os.listdir(l) if '.tar' in f or f.endswith('.zip') or f.endswith('.txt')]


def extract_tar(file, target_dir):
    extract(tarfile.open, file, target_dir)


def extract_zip(file, target_dir):
    extract(zipfile.ZipFile, file, target_dir)


def extract(func, file, target_dir):
    with func(file) as arc:
        arc.extractall(target_dir)


def process_txt(path):
    out_txt = list()
    for f in os.listdir(path):
        with open(f'{path}\\{f}', mode='rt', encoding='utf-8') as txt:
            out_txt += txt.readlines() + ['\n']
        os.remove(f'{path}\\{f}')
    with open('res.txt', mode='at', encoding='utf-8') as out:
        out.writelines(['\n<<<\n'] + out_txt + ['\n>>>'])


def process_archive(path, file, target_dir):
    if is_tar(file):
        extract_tar(f'{path}\\{file}', target_dir)
    elif is_zip(file):
        extract_zip(f'{path}\\{file}', target_dir)


def is_text(f):
    return f.endswith('.txt')


def is_tar(f):
    return '.tar' in f


def is_zip(f):
    return f.endswith('.zip')


def remove_archive(source_dir, f):
    if 'Find_the_key.tar.bz2' not in f'{source_dir}\\{f}':
        os.remove(f'{source_dir}\\{f}')


def walk_archive(source_dir, target):
    new_current_dir = f'{source_dir}\\{target}'
    for f in filter_files(source_dir):
        if is_text(f):
            process_txt(source_dir)
            return

        process_archive(source_dir, f, new_current_dir)
        walk_archive(new_current_dir, temp)
        remove_archive(source_dir, f)

    print('rmdir', new_current_dir)
    os.rmdir(new_current_dir)


walk_archive(current_dir, temp)

