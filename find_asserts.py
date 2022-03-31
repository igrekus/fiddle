from os import listdir
from pathlib import Path

user = 'test'
repo_name = 'repo'
to_repo = f'/home/{user}/source/{repo_name}/'
targets = ['conftest.py', '__init__.py']

with open('+a-p.txt', mode='rt', encoding='utf-8') as f:
    paths = [Path(to_repo + line[1:]).absolute() for line in map(str.strip, f.readlines())]


def scan(path):
    test_path = path.parent
    candidates = []
    while not str(test_path).endswith(repo_name):
        targets_full = [_ for _ in listdir(test_path) if _ in targets]
        if targets_full:
            targets_full = [str(test_path) + f'/{_}' for _ in targets_full]
            for target in targets_full:
                with open(target, mode='rt', encoding='utf-8') as f:
                    if 'pytest_rewrite_assert' in ''.join(f.readlines()):
                        break
                    candidates.append(target)
        test_path = test_path.parent

    if candidates:
        candidates = '\n   '.join(candidates)
        print(f'\nadd rewrite for: {path}\ncandidates:\n   {candidates}')


for p in paths:
    scan(p)
