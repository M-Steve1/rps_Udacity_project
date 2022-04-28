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


# win conditions
def beats(one, two):
    if one == 'rock' and two == 'paper':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'rock' and two == 'spock':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'paper' and two == 'rock':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'spock' and two == 'rock':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'rock' and two == 'scissors':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'rock' and two == 'lizard':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'scissors' and two == 'rock':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'lizard' and two == 'rock':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'paper' and two == 'rock':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'paper' and two == 'spock':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'rock' and two == 'paper':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'spock' and two == 'paper':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'paper' and two == 'scissors':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'paper' and two == 'lizard':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'scissors' and two == 'paper':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'lizard' and two == 'paper':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'scissors' and two == 'lizard':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'scissors' and two == 'paper':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'lizard' and two == 'scissors':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'paper' and two == 'scissors':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'spock' and two == 'rock':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'spock' and two == 'scissors':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'rock' and two == 'spock':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'scissors' and two == 'spock':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'spock' and two == 'lizard':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'spock' and two == 'paper':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'paper' and two == 'spock':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'lizard' and two == 'spock':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'lizard' and two == 'spock':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'lizard' and two == 'paper':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'spock' and two == 'lizard':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'paper' and two == 'lizard':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'lizard' and two == 'scissors':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'lizard' and two == 'rock':
        return (f"{Fore.BLUE}Player 2 Wins")
    elif one == 'scissors' and two == 'lizard':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == 'rock' and two == 'lizard':
        return (f"{Fore.RED}Player 1 Wins")
    elif one == two:
        return (f"{Fore.YELLOW}Tie")


# AI player, plays randomly
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Human player
class HumanPlayer(Player):
    def move(self):
        while True:
            humanplayer_move = input("rock, paper, scissors, "
                                     "spock, lizard? > ").lower()
            if humanplayer_move in moves:
                break
            else:
                print(f"{Fore.RED}Sorry, don't understand you")
        return humanplayer_move