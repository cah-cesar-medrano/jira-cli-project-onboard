""" Program Entry Point for __main__.py"""

import sys
from jpoc.logic import title_bar, program_intro, restore


def main():
    title_bar()
    user = restore()
    program_intro(user) if len(user) != 0 else program_intro()
