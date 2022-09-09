from typing import Set
from termcolor import colored
import time as py_time
isModule = True  # type: bool
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
        print(colored("Yes!", green))
        print("isModule =", colored("True", green))
        return 0
    else:
        print("No...")
        print("isModule =", colored(isModule, red))
        return 1
