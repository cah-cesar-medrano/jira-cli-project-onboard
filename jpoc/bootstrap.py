# -*- coding: utf-8 -*-


"""bootstrap.bootstrap: provides entry point main()."""


__version__ = "0.0.1"


import sys
from .jpoc import Jpoc


def main():
    print("Executing bootstrap version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
    print("Stuff and Boo():\n%s\n%s" % (Jpoc, Boo()))


class Boo(Jpoc):
    pass
