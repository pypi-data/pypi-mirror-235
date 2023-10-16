import json
import os
import sys
import time

from tentacule.process_pool import ProcessPool


class TestFailureError(Exception):
    pass


def _run_pytest_in_folder(dir: str, env: dict):
    sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + os.sep + 'src')

    for k, v in env.items():
        os.environ.setdefault(k, v)

    t = time.monotonic()
    os.system(' '.join(['pytest', f'--report-log="{dir}.log"', '--show-capture=all', '-x', dir, '>/dev/null']))
    print(f'Ran tests for {dir} in {time.monotonic() - t}s')


def run(test_dir: str, env: dict = None, workers: int = 1):
    env = env or {}
    pool = ProcessPool(workers=workers)
    pool.start()

    t = time.monotonic()

    test_dirs = os.listdir(test_dir)
    actual_dirs = []
    task_ids = []
    for dir in test_dirs:
        if not 'test' in dir or not os.path.isdir(f'{test_dir}/{dir}'):
            continue

        actual_dirs.append(f'{test_dir}/{dir}')
        task_id = pool.submit(
            _run_pytest_in_folder,
            f'tests/{dir}',
            {**env, 'PYTHONPATH': os.pathsep.join(sys.path)}
        )
        task_ids.append(task_id)
    _ = [pool.fetch(tid) for tid in task_ids]

    tests_results = {}
    for dir in actual_dirs:
        with open(f'{dir}.log', 'r') as log:
            lines = log.readlines()
            tests_results.setdefault(dir, [])
            for line in lines:
                if 'nodeid' in line:
                    result = json.loads(line)
                    tests_results[dir].append({'file': result['nodeid'], 'success': result['outcome'] == 'passed'})

    overall_success = True
    for k, v in tests_results.items():
        success = all(result['success'] for result in v)
        overall_success &= success
        print(k, success)

    print(f'Total run time: {time.monotonic() - t}s')
    if not overall_success:
        raise TestFailureError()