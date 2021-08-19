"""
generate a markdown report of which corepops are compatible with which platforms
"""
import subprocess
import functools
import docker
from typing import List
from pathlib import Path
from concurrent import futures


DOCKER_CLIENT = docker.from_env()
OS_NAME = subprocess.check_output(["uname", "-s"]).decode('utf-8').lower().strip()
ARCH = subprocess.check_output(["uname", "-m"]).decode('utf-8').strip()

DEPS = {
    'ubuntu': ['libc6', 'libncurses5', 'libncurses5-dev', 'libstdc++6', 'libxext6', 'libx11-6', 'libx11-dev', 'libxt-dev', 'libmotif-dev'],
    'fedora': ['ncurses-devel', 'openmotif-devel', '']
}

CONTAINERS = [
    ('ubuntu', '16.04'),
    ('ubuntu', '18.04'),
    ('ubuntu', '20.04'),
    ('ubuntu', '21.04'),
    ('fedora', '32'),
    ('fedora', '33'),
    ('fedora', '34'),
    ('centos', '7'),
    ('centos', '8'),
]


def unpack_tuple_args(fn):
    @functools.wraps(fn)
    def wrapped(args):
        return fn(*args)
    return wrapped


def list_available_corepops() -> List[Path]:
    return sorted([p for p in (Path(OS_NAME) / ARCH).iterdir()
                   if p.name.endswith('.corepop')])


def check_corepop_is_valid_in_container(image: str, corepop: Path) -> bool:
    try:
        response = DOCKER_CLIENT.containers.run(
            image=image,
            command=f"/bin/bash -c '/corepops/{corepop} \":sysexit()\"'",
            security_opt=["seccomp=unconfined"],
            volumes={
                str(Path().absolute()): {'bind': '/corepops', 'mode': 'ro'}
            }
        ).decode('utf-8')
        if len(response.strip()) > 0:
            return False
        return True
    except docker.errors.ContainerError as e:
        #print(e.container.logs(stdout=True).decode('utf-8'))
        #print(e.stderr.decode('utf-8'))
        return False


def main():
    core_pops: List[Path] = list_available_corepops()
    configs = [(container, tag, core_pop) for container, tag in CONTAINERS for core_pop in core_pops]
    with futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(unpack_tuple_args(check_corepop_is_valid_in_container), [
            (f"{container}:{tag}", core_pop) for container, tag, core_pop in configs
        ])
        for r, (container, tag, corepop) in zip(results, configs):
            print(f"{container}:{tag}, {corepop}: {r}")

if __name__ == '__main__':
    main()
