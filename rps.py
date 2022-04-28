from colorama import init
from colorama import Fore, Back, Style
import random
# On Windows, calling init() will filter ANSI escape sequences
# out of any text sent to stdout or stderr, and replace
# them with equivalent Win32 calls.
init(autoreset=True)


moves = ['rock', 'paper', 'scissors', 'spock', 'lizard']


# Parent class for all Players
class Player:
    def __init__(self):
        self.my_move = ''
        self.their_move = ''

    def move(self):
        return 'rock'

    # Inform players of opponent's move
    def learn(self, my_move, their_move):
        pass