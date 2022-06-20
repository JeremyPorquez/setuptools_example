from setuptools import setup, find_packages


def get_version():
    from pathlib import Path
    from pygit2 import Repository
    repo = Path().absolute()
    return repo.head


setup(
    name='setup_py',
    version='1.0',
    author='JP',
    packages=find_packages(),

)
