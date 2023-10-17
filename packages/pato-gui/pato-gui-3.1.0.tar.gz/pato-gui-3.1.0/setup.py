#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Setup
"""

import sys
from setuptools import find_packages
from setuptools.command.test import test as TestCommand
from distutils.core import setup

# To prevent importing about and thereby breaking the coverage info we use this
# exec hack
about = {}
with open('src/utils/about.py', mode='r', encoding="utf-8") as fp:
    exec(fp.read(), about)


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', 'Arguments to pass to pytest')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)

# copy of src/program/requirements.txt
install_requires = [
    'wxpython>=4.1.0',
    'Gooey>=1.0.8'
]

# copy of test_requirements.txt
tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-flakes',
    'pytest-pycodestyle',
    'flake8',
    'mypy'
]


if sys.argv[-1] == 'info':
    for k, v in about.items():
        print('%s: %s' % (k, v))
    sys.exit()


if __name__ == '__main__':
    with open('README.md', mode='r', encoding="utf-8") as f:
        readme = f.read()

    with open('CHANGELOG.md', mode='r', encoding="utf-8") as f:
        changes = f.read()

    setup(
        name=about['__package_name__'],
        version=about['__version__'],
        author=about['__author__'],
        author_email=about['__email__'],
        description=about['__description__'],
        url=about['__url__'],
        license=about['__license__'],
        keywords=["Oracle", "PATO", "GUI"],
        packages=find_packages('src'),
        package_dir={'': 'src'},
        #namespace_packages=[about['__package_name__']],
        long_description=readme + changes,
        long_description_content_type='text/markdown',
        #include_package_data=True,
        install_requires=install_requires,
        tests_require=tests_require,
        setup_requires=[
            'setuptools>=42',
        ],
        zip_safe=True,
        cmdclass={'test': PyTest},
        extras_require={'test': tests_require},
        entry_points = {
            'gui_scripts': [
                'pato-gui = program.pato_gui:main',
            ],
        },
        classifiers=[
            'Development Status :: 6 - Mature',
            'Programming Language :: Python :: 3',
            'Natural Language :: English',
            'Topic :: Utilities',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'License :: OSI Approved :: ' + about['__license__']
        ],
    )
