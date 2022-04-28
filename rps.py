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


# AI player, copies human player previous move
class ReflectPlayer(Player):
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        if self.my_move == '':
            return random.choice(moves)
        else:
            return self.their_move


# AI player, plays by cycling the moves
class CyclePlayer(Player):
    def __init__(self):
        self.index = 0

    def move(self):
        next_move = moves[self.index]
        self.index = (self.index + 1) % len(moves)
        return next_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.player1_score = 0
        self.player2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"{Fore.RED}Player 1: {move1}  {Fore.BLUE}Player 2: {move2}")
        print()

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        print(f"\t** {beats(move1, move2)}{Fore.RESET} **")
        winner = beats(move1, move2)
        if 'Player 1 Wins' in winner:
            self.player1_score += 1
        elif 'Player 2 Wins' in winner:
            self.player2_score += 1