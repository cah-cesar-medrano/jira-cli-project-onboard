""" Functions for logic """

import os
import pickle


def title_bar():
    __version__ = "0.0.5"
    # Clears cli between cycles and displays title bar
    os.system('cls')
    # Display a title bar.
    print("\t**********************************************")
    print("\t***            Welcome to JPOC!            ***")
    print("\t**********************************************")
    print("            Executing JPOC version {}.\n".format(__version__))


def decision_tree():
    # let users know what they can do.
    print("\n[1] See a list of friends.")
    print("[2] Tell me about someone new.")
    print("[q] Quit.\n")

    return input("What would you like to do?")

def _quit(roles):
    # Function dumps the names into a file, and prints a quit message
    try:
        file_object = open('names.pydata', 'wb')
        pickle.dump(roles, file_object)
        file_object.close()
        print("\nThanks for playing. I will remember these good friends.")
    except Exception as e:
        print("\nThanks for playing. I won't be able to remember these names.")
        print(e)
