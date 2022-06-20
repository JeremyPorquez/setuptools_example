from setuptools import setup
from setuptools.command.install import install
from subprocess import check_call


class PreInstallCommand(install):
    def run(self):
        check_call("sh install/setup.sh".split())
        install.run(self)


with open('requirements.txt') as f:
    deps = f.read().split("\n")

setup(
    install_requires=deps
)
