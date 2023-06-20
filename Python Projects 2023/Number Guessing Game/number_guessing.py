"""
Created on Tue Jun 20 13:02:53 2023

@author: Sami RAJICHI
"""

from random import randint


class NumberGuessing:

    # Define an attribute to store the number of attempts, initiated to 0
    number_of_checks: int = 0
    # Define an attribute that represents the lower bound in a range, start with 1
    lower_number: int = 1
    # Define an attribute that represents the higher bound in a range, finish with 1
    higher_number: int = 10
    # Define an attribute to verify the guess status of the user, default False
    is_guessed: bool = False

    # Initiating the class
    def __init__(self, number_of_plays: int = 1):
        self.number_of_plays = number_of_plays

    # Define a method called generate_number to produce a number for guessing
    def generate_number(self):
        return randint(self.lower_number, self.higher_number)

    # Define a method called get_user_guess to get user input
    def get_user_guess(self):
        return int(input('Please, enter your guess: '))

    # Define a method called check_guess to compare the user guess with the generated number
    # and print a feedback
    def check_guess(self, guess: int, generated_number: int):
        if guess > generated_number:
            print('* Your guess is higher\n')
        elif guess < generated_number:
            print('* Your guess is lower\n')
        else:
            print('** Right, you guessed it !\n')
            # When the guess and the generated number are equal, is_guessed should be associated to True
            self.is_guessed = True

    # Define a method as a starting point game
    def start_guessing(self):
        print('---------- Welcome to Number Guessing Game ----------\n')
        for play in range(1, self.number_of_plays+1):
            # For each game, is_guessed should be associated to False
            self.is_guessed = False
            # Create a variable to calculate the number of attempts for each game
            game_attempts = 0
            print(f'Game #{play}:')
            # Define a variable to store a random variable from the method created previously
            generated_number: int = self.generate_number()
            # All the processes will take place under a continuous loop, until the user finds the guess
            while True:
                # It's better to handle the exception while taking the user input
                try:
                    user_guess: int = self.get_user_guess()
                except ValueError:
                    print('Please, enter a valid number.')
                    # When the error is encountered, no need to execute the rest of the loop
                    # However, we restart the loop
                    continue
                # Call the check_guess method for status verification
                self.check_guess(user_guess, generated_number)
                # Increment the number of checks
                game_attempts += 1
                # If the condition evaluates to True, the loop breaks down and the game ends up.
                if self.is_guessed:
                    self.number_of_checks += game_attempts
                    break
            print(
                f'Game #{play} Attempts taken: {str(game_attempts):>4}\n')


# Main function
if __name__ == '__main__':
    number_guessing: NumberGuessing = NumberGuessing(3)
    number_guessing.start_guessing()
    print(
        f'Overall attempts taken: {str(number_guessing.number_of_checks):>4}')
