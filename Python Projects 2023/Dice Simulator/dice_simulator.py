"""
Created on Wed Jun 21 22:58:37 2023

@author: Sami RAJICHI
"""

from random import randint


class DiceSimulator:

    # Define a method called get_user_input to ask the user for the number of rolls
    # To ensure that the method is private, adding two _ at the beginning is mandatory
    def __get_user_input(self) -> str:
        return input('Haw many dice would you like to roll? ')

    # Define a method called roll_dice to store each roll output
    def __roll_dice(self, number_of_rolls: int = 2) -> list[int]:
        # The number_of_rolls should be greater than 0, otherwise an error is thrown
        if number_of_rolls <= 0:
            raise ValueError
        # Return a list of rolls outputs that are generated randomly
        return [randint(1, 6) for roll in range(number_of_rolls)]

    def roll(self):
        print('---------- Welcome to Dice Simulator ----------\n')
        while True:
            # Handle exception if the user input is invalid
            try:
                user_input: str = self.__get_user_input()
                # The program will ends up once the user hits 'exit'
                if user_input.lower() == 'exit':
                    break
                # Get the rolls values
                rolls: list[int] = self.__roll_dice(int(user_input))
                print(*rolls, sep=', ')
                # Print out the sun of the outputs
                print(f'** Sum of the rolls:{sum(rolls): >5}\n')
            except ValueError:
                print('Please, enter a valid number.')


# Main function
if __name__ == '__main__':
    dice_simulator: DiceSimulator = DiceSimulator()
    dice_simulator.roll()
