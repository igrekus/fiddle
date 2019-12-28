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
    with tarfile.open(file) as tar:
        tar.extractall(target_dir)
    tar.close()


def extract_zip(file, target_dir):
    with zipfile.ZipFile(file) as z:
        z.extractall(target_dir)
    z.close()


def process_txt(dir_):
    out_txt = list()
    for f in os.listdir(dir_):
        with open(f'{dir_}\\{f}', mode='rt', encoding='utf-8') as txt:
            out_txt += txt.readlines() + ['\n']
        if os.path.isfile(f'{dir_}\\{f}'):
            os.remove(f'{dir_}\\{f}')
    with open('res.txt', mode='at', encoding='utf-8') as out:
        out.writelines(['\n<<<\n'] + out_txt + ['\n>>>'])


def extract(source_dir, target):
    files = filter_files(source_dir)
    new_current = f'{source_dir}\\{target}'
    for f in files:
        f_path = f'{source_dir}\\{f}'
        if f.endswith('.txt'):
            process_txt(source_dir)
            return
        elif '.tar' in f:
            extract_tar(f_path, new_current)
            extract(new_current, temp)
        elif f.endswith('.zip'):
            extract_zip(f_path, new_current)
            extract(new_current, temp)

        if os.path.isfile(f_path):
            if 'Find_the_key.tar.bz2' not in f_path:
                os.remove(f_path)

    print('rmdir', new_current)
    os.rmdir(new_current)


extract(current_dir, temp)

