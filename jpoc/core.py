""" Program Entry Point for __main__.py"""

import sys
from jpoc.logic import title_bar, program_intro, restore, working_loop, User


def main():
    title_bar()
    user = restore()
    if user is not None:
        old = User(user[0], user[1], user[2])
        program_intro(old)
    else:
        jira, user = program_intro()

    working_loop(jira, user)
