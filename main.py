from termcolor import colored
import time as py_time
from pure_py import make, print_str
make()
green = "green"
red = "red"
colors = [green, red]
py_time.sleep(2)
help(print_str)
print_str(colored("Success!", green))
