from colorama import init
from colorama import Fore, Back, Style
import random
# On Windows, calling init() will filter ANSI escape sequences
# out of any text sent to stdout or stderr, and replace
# them with equivalent Win32 calls.
init(autoreset=True)


moves = ['rock', 'paper', 'scissors', 'spock', 'lizard']