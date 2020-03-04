""" Program Entry Point for __main__.py"""

import sys
from getpass import getpass, getuser
from jpoc.logic import title_bar, jira_login, User


def main():
    title_bar()

    try:
        user_name = getuser()  # input("\tUser Name: ")
        print("\t Hello! {}!".format(user_name))
        password = getpass(prompt="\t Password: ")
        server = input("\tServer Url: ")
        jira = jira_login(User(user_name, password, server))
        title_bar()
        print(jira.user(user_name))
    except Exception as e:
        print('Login Failed\n')
        print(e)
