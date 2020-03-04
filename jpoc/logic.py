""" Functions for logic """

from getpass import getpass, getuser
from jira import JIRA, JIRAError
import os
from time import sleep
import pickle


""" VIEWS """
# introductory view that asks for password and displays name
def program_intro(*args):

    try:
        if args is not None:
            user_name = getuser()
            print("\t Hello! {}!".format(user_name))
            password = getpass(prompt="\t Password: ")
            server = input("\tServer Url: ")
            user = User(user_name, password, server)
            jira = jira_login(user)
            title_bar()
            return jira, user
        else:
            print("\t Hello! {}!".format(args.user_name))
            jira = jira_login(User(args.user_name, args.password, args.server))
            title_bar()
            return jira
    except Exception as e:
        print('Login Failed\n')
        print(e)

def title_bar(**args):
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
    print("\n[1] Onboard ONE Person")
    print("[q] Quit.\n")

    return input("What would you like to do?")

""" LOGIC FUNCTIONS """

def working_loop(*args):
    jira, user = args
    choice = ''
    title_bar()
    while choice != 'q':

        coice = decision_tree()

        # Response to user choice
        title_bar()

        if choice == '1':
            onboard(jira)
        elif choice == 'q':
            _quit(user)
        else:
            print("\nI didn't understand that choice.\n")

# Deletes the stored data
def delete_pickle():
    pass

def onboard(*args):
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
    user = (User.user_name, User.password, User.server)
    with open('data.pydata', 'wb') as file_object:
        try:
            pickle.dump(user, file_object)
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
