""" Functions for logic """

from jira import JIRA, JIRAError
import os
import pickle


def title_bar():
    # Current Version
    __version__ = "0.5"
    # Clears cli between cycles and displays title bar
    os.system('cls')
    # Display a title bar.
    print("\t**********************************************")
    print("\t***            Welcome to JPOC!            ***")
    print("\t**********************************************")
    print("\t********  Executing JPOC version: {} ********\n".format(__version__))


def decision_tree():
    # let users know what they can do.
    print("\n[1] See a list of friends.")
    print("[2] Tell me about someone new.")
    print("[q] Quit.\n")

    return input("What would you like to do?")

def _quit(User):
    # Function dumps the names into a file, and prints a quit message
    with open('names.pydata', 'wb') as file_object:
        try:
            pickle.dump(User, file_object)
            file_object.close()
            print("\nThanks for playing. I will remember these good friends.")
        except Exception as e:
            print("\nThanks for playing. I won't be able to remember these names.")
            print(e)

# User Login
def jira_login(User):
    return JIRA(basic_auth=(User.user_name, User.password), options={'server': User.server})

# User Class
class User(object):
    def __init__(self, user_name, password, server):
        self.user_name = user_name
        self.password = password
        self.server = server
