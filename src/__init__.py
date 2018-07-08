from kaucherpy.kaucher import *
from kaucherpy.kaucher.Kaucher import *
from kaucherpy.core import *
from kaucherpy.support import *


def _test():
    from doctest import DocTestSuite
    from inspect import getmodule
    from os import walk
    from os.path import abspath, dirname, join
    from unittest import TestSuite, TextTestRunner
    test_suite = TestSuite()
    for root, dirs, files in walk(dirname(abspath(__file__))):
        module_files = [join(root, file) for file in files if \
            file.endswith(".py")]
        test_suite.addTests(DocTestSuite(getmodule(None, file)) for file in \
            module_files)
    TextTestRunner().run(test_suite)


if __name__ == "__main__":
    _test()
