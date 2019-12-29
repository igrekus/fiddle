import os
import tarfile
import zipfile


current_dir = 'data'
temp = 'temp'

wrong_file = [
    'Key in another file',
    "It's not the file you're looking for",
    'The key is somewhere but not here',
]

open_func = {
    True: tarfile.open,
    False: zipfile.ZipFile
}


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


def process_arc_file(path_to_file, target_dir):
    extract(open_func[is_tar(path_to_file)], path_to_file, target_dir)


def is_txt(f):
    return f.endswith('.txt')


def is_tar(f):
    return '.tar' in f


def remove_archive(path_to_file):
    if not path_to_file.endswith('Find_the_key.tar.bz2'):
        os.remove(path_to_file)


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


walk_archive(current_dir, temp)

