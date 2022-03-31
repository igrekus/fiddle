from os import listdir
from pathlib import Path


def scan(path):
    if path.parts[-1].startswith('test_'):
        return []

    test_path = path.parent
    candidates = []
    while not str(test_path).endswith(repo_name):
        candidates += _check_candidates(_build_full_paths(test_path))
        test_path = test_path.parent

    return candidates


def _check_candidates(files):
    return filter(bool, (_check_file_for_rewrite(file) for file in files))


def _build_full_paths(test_path):
    return (f'{test_path}/{_}' for _ in _scan_dir_for_targets(test_path))


def _check_file_for_rewrite(file):
    with open(file, mode='rt', encoding='utf-8') as f:
        return '' if 'pytest_rewrite_assert' in ''.join(f.readlines()) else file


def _scan_dir_for_targets(_dir):
    return filter(lambda file: file in target_files, listdir(_dir))


if __name__ == '__main__':
    user = 'test'
    repo_name = 'repo'
    to_repo = f'/home/{user}/source/{repo_name}/'
    target_files = ['conftest.py', '__init__.py']

    with open(f'./+a-p.txt', mode='rt', encoding='utf-8') as f:
        paths = [Path(to_repo + line[1:]).absolute() for line in map(str.strip, f.readlines())]

    for p in paths:
        cs = scan(p)
        if cs:
            cs = '\n   '.join(cs)
            print(f'\nadd rewrite for: {p}\ncandidates:\n   {cs}')

