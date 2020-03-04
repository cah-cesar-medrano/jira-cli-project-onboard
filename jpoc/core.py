""" Program Entry Point for __main__.py"""

import sys
from jpoc.logic import title_bar, program_intro, restore


def main():
    title_bar()
    program_intro(restore())
