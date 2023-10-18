from setuptools import setup
from sudoku import VERSION

setup(
    name='modern-sudoku',
    version=VERSION,
    url='https://github.com/riverlis/sudoku-solver',
    author='riverlis',
    author_email='tienduy0123@gmail.com',
    description='a sudoku package',

    py_modules=['sudoku'],
    install_requires=['numpy', 'ortools.sat.python']
)