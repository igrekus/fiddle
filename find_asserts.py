import re
import sys

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

    # with open(f'./+a-p.txt', mode='rt', encoding='utf-8') as f:
    #     paths = [Path(to_repo + line[1:]).absolute() for line in map(str.strip, f.readlines())]
    #
    # for p in paths:
    #     cs = scan(p)
    #     if cs:
    #         cs = '\n   '.join(cs)
    #         print(f'\nadd rewrite for: {p}\ncandidates:\n   {cs}')

    # run:
    # grep --include=\*.{,py} -rl ./ -e "assert " | xargs grep -rL " pytest" | tee ~/+a-p.txt
    # cat ~/+a-p.txt | xargs -I % python3 find_asserts.py %

    lib_re = re.compile('lib/(\S+).py')
    libs_re = re.compile('libs/(\S+).py')
    auto_tests_re = re.compile('auto_tests/(\S+).py')
    testing_re = re.compile('testing/(\S+).py')
    integration_re = re.compile('integration/(\S+).py')
    app_re = re.compile('app/(\S+).py')
    db_re = re.compile('db/(\S+).py')
    kata_scan_re = re.compile('source/kata_scan(\S+).py')
    utils_re = re.compile('utils/(\S+).py')
    settings_re = re.compile('settings(\S+).py')
    config_re = re.compile('config(\S+).py')
    tool_re = re.compile('tool(\S+).py')
    api_re = re.compile('api/(\S+).py')
    build_re = re.compile('build/(\S+).py')
    deploy_re = re.compile('deploy/(\S+).py')

    p = Path(to_repo + sys.argv[1][1:]).absolute()
    cs = scan(p)
    if cs:
        cs = '\n   '.join(cs[:1])
        if not lib_re.search(cs) and not libs_re.search(cs) and not auto_tests_re.search(cs) and not testing_re.search(cs)\
                and not integration_re.search(cs) and not app_re.search(cs) and not db_re.search(cs) \
                and not kata_scan_re.search(cs) and not utils_re.search(cs) and not settings_re.search(cs) \
                and not config_re.search(cs) and not tool_re.search(cs) and not api_re.search(cs) \
                and not build_re.search(cs) and not deploy_re.search(cs):
            print(f'\nrewrite: {p}\nclosest: {cs}')

        # cs = '\n   '.join(cs)
        # print(f'\nadd rewrite for: {p}\ncandidates:\n   {cs}')
