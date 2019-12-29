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


def extract(func, file, target_dir):
    with func(file) as arc:
        arc.extractall(target_dir)


def process_txt(txt_dir):
    out_txt = list()
    for f in os.listdir(txt_dir):
        with open(f'{txt_dir}\\{f}', mode='rt', encoding='utf-8') as txt:
            out_txt += txt.readlines() + ['\n']
        os.remove(f'{txt_dir}\\{f}')
    with open('res.txt', mode='at', encoding='utf-8') as out:
        out.writelines(['\n<<<\n'] + out_txt + ['\n>>>'])


def process_archive(path_to_file, target_dir):
    open_func = tarfile.open if is_tar(path_to_file) else zipfile.ZipFile
    extract(open_func, path_to_file, target_dir)


def is_text(f):
    return f.endswith('.txt')


def is_tar(f):
    return '.tar' in f


def remove_archive(path_to_file):
    if not path_to_file.endswith('Find_the_key.tar.bz2'):
        os.remove(path_to_file)


def walk_archive(source_dir, target):
    new_current_dir = f'{source_dir}\\{target}'
    for f in filter_files(source_dir):
        if is_text(f):
            process_txt(source_dir)
            return

        process_archive(f'{source_dir}\\{f}', new_current_dir)
        walk_archive(new_current_dir, temp)
        remove_archive(f'{source_dir}\\{f}')

    print('rmdir', new_current_dir)
    os.rmdir(new_current_dir)


walk_archive(current_dir, temp)

