"""
Created on Fri Jun 30 12:31:39 2023

@author: Sami RAJICHI

@project: Rock - Paper - Scissor
"""

from random import choice
import sys


class RPS:

    def __init__(self):
        """
        This method initiates each class instance while displaying a welcome message and 
        defining the game variables.
        """
        # Setting a welcome message and a notice
        welcome = 'Welcome to Rock Paper Scissor Game'
        print(f'{welcome:-^45}\n')
        print('NOTE: just type in the first letter of the move (r-rock, p-paper or s-scissor) or exit to quit the game.')
        # Game variables
        self.rps: dict = {'r': '✊', 'p': '✋', 's': '✂'}
        self.rps_keys: list[str] = tuple(self.rps.keys())
        self.user_wins, self.computer_wins, self.total = (0, 0, 0)

    def play(self):
        """
        This method is responsible of starting the game. 
        It takes a user input and generates the computer choice.
        It evaluates the user input to ensure everything goes well.
        """
        # Taking the user input and computer's move
        self.user_input: str = input(
            '\nRock, Paper or Scissor (r, p or s)? >>> ').lower()
        self.computer_input: str = choice(self.rps_keys)

        # Quitting the game once the user types 'exit'
        if self.user_input == 'exit':
            print('\nThanks for playing..')
            sys.exit()

        # Checking whether the input exists in the rps tuple or not
        if self.user_input not in self.rps_keys:
            print('Not a valid move.. Try Again.')
            return self.play()

        # Counting the number of games for every play
        self.total += 1
        # Displaying guides and results
        self.__display_choices()
        self.__check_result()

    def __display_choices(self):
        """
        This method guides the user by printing down some messages.
        """
        print(
            f'\nGame #{self.total}:')
        print('=' * 6)
        print(f'You:  {self.rps[self.user_input]}')
        print(f'Comp: {self.rps[self.computer_input]}')
        print('=' * 6)

    def __check_result(self):
        """
        This method compares the user input with the computer's one.
        Then displays the comparison's output.
        """
        # Evaluating all the positive possibilities of a user win
        when_user_win: bool = (self.user_input == 'r' and self.computer_input == 's') or \
                              (self.user_input == 'p' and self.computer_input == 'r') or \
                              (self.user_input == 's' and self.computer_input == 'p')

        # Showing results
        if self.user_input == self.computer_input:
            print('It\'s a tie.. 🤝')
        elif when_user_win:
            print('You WON 🎊')
            self.user_wins += 1
        else:
            print('Computer WON 🖥')
            self.computer_wins += 1

        print(f'🧑: {self.user_wins}\t\t🖥: {self.computer_wins}')


# Main function
if __name__ == '__main__':
    rps: RPS = RPS()
    while True:
        rps.play()
