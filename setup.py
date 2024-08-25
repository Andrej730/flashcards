import sys
import os
from setuptools import setup
from setuptools import find_packages
from setuptools.command.install import install

DESCRIPTION = ("CLI application that focus on quickly creating "
               "study flash cards")

REQUIREMENTS = ['click==6.6']

class CustomInstallCommand(install):
    def run(self):
        if os.name != 'nt':  # Skip on Windows
            self.distribution.data_files = [('/etc/bash_completion.d/', ['flashcards-complete.sh'])]
        else:
            self.distribution.data_files = []
        install.run(self)

setup(
    name='pyflashcards',
    author='Jonathan Lalande',
    author_email='jonathan.lalande.1@ens.etsmtl.ca',
    version='1.0.2',
    license='MIT',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    cmdclass={
        'install': CustomInstallCommand,
    },
    entry_points="""
        [console_scripts]
        flashcards=flashcards.main:cli
    """
)
