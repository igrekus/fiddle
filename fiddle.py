import itertools
import os
import tarfile
import zipfile


wrong_file = [
    'Key in another file',
    "It's not the file you're looking for",
    'The key is somewhere but not here',
]

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
    with open('res.txt', mode='at', encoding='utf-8') as out:
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


if __name__ == '__main__':
    current_dir = 'data'
    temp = 'temp'
    walk_archive(current_dir, temp)
