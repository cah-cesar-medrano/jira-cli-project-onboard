""" Program Entry Point for __main__.py"""

import sys
from jpoc import Jpoc

__version__ = "0.0.5"

def main():
    print("Executing JPOC version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])


class Boo(Jpoc):
    pass
