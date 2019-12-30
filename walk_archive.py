import argparse
import itertools
import os
import tarfile
import zipfile
import sys


open_func = {
    True: tarfile.open,
    False: zipfile.ZipFile
}


def walk_archive(source_dir, target):
    new_current_dir = f'{source_dir}\\{target}'
    for f in filter_files(source_dir):
        if is_txt(f):
            process_txt(source_dir)
            return
        arc_path = f'{source_dir}\\{f}'
        process_arc_file(arc_path, new_current_dir)
        walk_archive(new_current_dir, temp)
        remove_archive(arc_path)

    print('rmdir', new_current_dir)
    os.rmdir(new_current_dir)


def filter_files(path):
    return [f for f in os.listdir(path) if '.tar' in f or f.endswith('.zip') or f.endswith('.txt')]


def is_txt(f):
    return f.endswith('.txt')


def process_txt(txt_dir):
    log_data([collect_txt_data(f'{txt_dir}\\{f}') for f in os.listdir(txt_dir)])


def log_data(data):
    with open(log_file, mode='at', encoding='utf-8') as out:
        out.writelines(list(itertools.chain(*data)))


def collect_txt_data(file):
    with open(file, mode='rt', encoding='utf-8') as txt:
        data = txt.readlines() + ['\n']
    os.remove(file)
    return ['\n###\n'] + data + ['\n$$$']


def process_arc_file(path_to_file, target_dir):
    extract(open_func[is_tar(path_to_file)], path_to_file, target_dir)


def extract(func, file, target_dir):
    with func(file) as arc:
        arc.extractall(target_dir)


def is_tar(f):
    return '.tar' in f


def remove_archive(path_to_file):
    if not path_to_file.endswith('Find_the_key.tar.bz2'):
        os.remove(path_to_file)


def find_key(raw_file):
    with open(raw_file, mode='rt', encoding='utf-8') as raw_f:
        files = ''.join(raw_f.readlines()).split('$$$\n###')

    wrong_file = {
        "It's not the file you're looking for",
        "You're close, check another file",
        "Key in another file",
        "The key is somewhere but not here",
        "Key in another castle!",
        "Key is not here!"
    }

    key = list(filter(lambda l: l.strip().split('\n')[0] not in wrong_file, files[1:]))[0].strip().split('\n')[0]
    with open(key_file, mode='wt', encoding='utf-8') as out_f:
        out_f.write(key)


if __name__ == '__main__':
    temp = 'temp'
    log_file = 'res.txt'
    key_file = 'key.txt'

    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to the root archive', default='.')
    args = parser.parse_args()

    if args.path == 'Find_the_key.tar.bz2':
        current_dir = '.'
    elif 'Find_the_key.tar.bz2' in args.path:
        current_dir = args.path[:-(len('Find_the_key.tar.bz2') + 1)]
    else:
        current_dir = args.path

    walk_archive(current_dir, temp)
    find_key(log_file)

    os.startfile(key_file)
