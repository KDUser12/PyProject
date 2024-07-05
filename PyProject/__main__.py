""" PyProject : Creating your project has never been easier.

This module contains tools to easily create your own projects
without having to recreate the same files.

"""

import sys

if __name__ == '__main__':
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 8):
        print("PyProject requires Python 3.8+ You are using Python {}, which is not supported by PyProject".format(python_version))
        exit(1)

import pyproject
pyproject.main()
