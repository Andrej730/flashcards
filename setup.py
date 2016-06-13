from setuptools import setup
from setuptools import find_packages

DESCRIPTION = ("CLI application that focus on quickly creating "
               "study flash cards")

REQUIREMENTS = ['click==6.6']

setup(
    name='flashcards',
    author='Jonathan Lalande',
    author_email='jonathan.lalande.1@ens.etsmtl.ca',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    data_files=[('/etc/bash_completion.d/', ['flashcards-complete.sh'])],
    entry_points="""
        [console_scripts]
        flashcards=flashcards.main:cli
    """
)
