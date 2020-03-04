""" Program Entry Point for __main__.py"""

import sys
from jpoc.logic import title_bar, jira_login, User


def main():
    title_bar()

    try:
        user_name = input("\tUser Name: \n")
        password = input("\tPassword: \n")
        server = input("\tServer Url: \n")
        jira = jira_login(User(user_name, password, server))
    except Exception as e:
        print('Login Failed\n')
        print(e)
