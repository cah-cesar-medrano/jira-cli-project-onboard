""" Functions for logic """

from getpass import getpass, getuser
from jira import JIRA, JIRAError
import os
import time.sleep as sleep
import pickle


""" VIEWS """
# introductory view that asks for password and displays name
def program_intro(*args):
    try:
        if(args.__len__ == 0):
            user_name = getuser()
            print("\t Hello! {}!".format(user_name))
            password = getpass(prompt="\t Password: ")
            server = input("\tServer Url: ")
            jira = jira_login(User(user_name, password, server))
            title_bar()
        else:
            jira = jira_login(User(args.user_name, args.password, args.server))
            title_bar()
    except Exception as e:
        print('Login Failed\n')
        print(e)

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

    input("What would you like to do?")

""" LOGIC FUNCTIONS """

# Deletes the stored data
def delete_pickle():
    pass

# Restores pickled user data
def restore():
    try:
        with open('data.pydata', 'rb') as data:
            return pickle.load(data)
    except Exception as e:
        print("Exception triggred: {}\n\n".format(e))
        print("There is no user data stored\n\n")
        sleep(3)
        os.system('cls')

# quits program and saves user data
def _quit(User):
    # Function dumps the names into a file, and prints a quit message
    with open('data.pydata', 'wb') as file_object:
        try:
            pickle.dump(User, file_object)
            file_object.close()
            print("\tThanks for using JPOC")
        except Exception as e:
            print("\tThanks for using JPOC, I was not able to save your data")
            print(e)

# User Login
def jira_login(User):
    return JIRA(basic_auth=(User.user_name, User.password), options={'server': User.server})


""" CLASSES """

# User Class
class User(object):
    def __init__(self, user_name, password, server):
        self.user_name = user_name
        self.password = password
        self.server = server
