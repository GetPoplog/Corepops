"""
generate a markdown report of which corepops are compatible with which platforms
"""
import subprocess
import functools
import docker
from typing import List, Tuple
from pathlib import Path
from concurrent import futures


DOCKER_CLIENT = docker.from_env()
OS_NAME = subprocess.check_output(["uname", "-s"]).decode('utf-8').lower().strip()
ARCH = subprocess.check_output(["uname", "-m"]).decode('utf-8').strip()

CONTAINERS = [
    ('ubuntu', '21.04'),
    ('ubuntu', '20.04'),
    ('ubuntu', '18.04'),
    ('ubuntu', '16.04'),
    ('debian', 'unstable-slim'),
    ('debian', 'testing-slim'),
    ('debian', 'stable-slim'),
    ('debian', 'oldstable-slim'),
    ('debian', 'oldoldstable'),
    ('fedora', '34'),
    ('fedora', '33'),
    ('fedora', '32'),
    ('centos', '8'),
    ('centos', '7'),
]


def unpack_tuple_args(fn):
    @functools.wraps(fn)
    def wrapped(args):
        return fn(*args)
    return wrapped


def list_available_corepops() -> List[Path]:
    return sorted([p for p in (Path(OS_NAME) / ARCH).iterdir()
                   if p.name.endswith('.corepop')])


def run_corepop_in_container(image: str, corepop: Path) -> Tuple[int, str]:
    container = DOCKER_CLIENT.containers.run(
        image=image,
        command=f"/bin/bash -c '/corepops/{corepop} \":sysexit()\"'",
        security_opt=["seccomp=unconfined"],
        volumes={
            str(Path().absolute()): {'bind': '/corepops', 'mode': 'ro'}
        },
        detach=True
    )
    exit_code = container.wait()['StatusCode']
    response = container.logs(stdout=True, stderr=True).decode('utf-8')
    return exit_code, response


def generate_results_table(results):
    report = """\
| Corepop | Distribution | Version | Pass | Exit code | Logs |
| ------- | ------------ | ------- | ---- | --------- | ---- |
"""
    for result in results:
        pass_str = ':heavy_check_mark:' if result['pass'] else ':x:'
        if len(result['logs'].strip()) == 0:
            logs_str = ''
        else:
            logs_line = result['logs'].replace('\n', '<br>')
            logs_str = f"<details><summary>details</summary><pre>{logs_line}</pre></details>"
        report += (
            f"| {result['core_pop']} | {result['container']} | {result['tag']} " +
            f"| {pass_str} | {result['exit_code']} | {logs_str} |\n"
        )

    return report



def main():
    core_pops: List[Path] = list_available_corepops()
    configs = [(container, tag, core_pop) for core_pop in core_pops for container, tag in CONTAINERS ]
    with futures.ThreadPoolExecutor(max_workers=20) as executor:
        _results = executor.map(unpack_tuple_args(run_corepop_in_container), [
            (f"{container}:{tag}", core_pop) for container, tag, core_pop in configs
        ])
    results = [
        {
            'container': container,
            'tag': tag,
            'core_pop': core_pop,
            'exit_code': exit_code,
            'logs': logs,
            'pass': exit_code == 0 and len(logs.strip()) == 0,
        }
        for (container, tag, core_pop), (exit_code, logs) in zip(configs, _results)
    ]
    table = generate_results_table(results)
    print(table)


if __name__ == '__main__':
    main()
