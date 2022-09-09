from typing import Set

from termcolor import colored
import time as py_time
isModule = True
red = "red"  # type: str
yellow = "yellow"  # type: str
blue = "blue"  # type: str
green = "green"  # type: str
colors = {red, yellow, blue}  # type: Set[str]


def make():
    global isModule
    print(colored("Script of function \"make\" found", yellow))
    py_time.sleep(2)
    print(colored("Creating threads...", blue))
    py_time.sleep(10)
    print("Is the variable \"isModule\" equal to True?")
    py_time.sleep(2)
    if isModule:
        print("Yes.")
        print("isModule =", colored(isModule, green))
        return True
