"""
Created on Wed Jun 21 22:58:37 2023

@author: Sami RAJICHI
"""

from random import randint


class DiceSimulator:

    def __init__(self):
        self.dice_art: dict = {
            1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
            2: ("┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘"),
            3: ("┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘"),
            4: ("┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"),
            5: ("┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"),
            6: ("┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘")
        }

    def __get_user_input(self) -> str:
        """
            Defines a method called get_user_input to ask the user for the number of rolls.
            To ensure that the method is private, adding two _ at the beginning is mandatory
        """
        return input('Haw many dice would you like to roll? ')

    def __roll_dice(self, number_of_rolls: int = 2) -> list[int]:
        """
            Defines a method called roll_dice to store each roll output
        """
        # The number_of_rolls should be greater than 0, otherwise an error is thrown
        if number_of_rolls <= 0:
            raise ValueError
        # Return a list of rolls outputs that are generated randomly
        self.rand_rolls: list[int] = [
            randint(1, 6) for roll in range(number_of_rolls)]
        return [self.dice_art[roll] for roll in self.rand_rolls]

    def __dice_artworks_displayer(self, user_input: str):
        """
        Displaying all the generated dice artworks on the screen
        """
        rolls: list[str] = self.__roll_dice(int(user_input))
        for roll in range(5):
            for line in range(len(rolls)):
                print(rolls[line][roll], end=' ')
            print()  # Jumping to a new line

    def roll(self):
        """
            Presents the starter of the game
        """
        print('---------- Welcome to Dice Simulator ----------\n')
        while True:
            # Handle exception if the user input is invalid
            try:
                user_input: str = self.__get_user_input()
                # The program will ends up once the user hits 'exit'
                if user_input.lower() == 'exit':
                    break
                # Get the rolls values
                self.__dice_artworks_displayer(user_input)
                # Print out the sun of the outputs
                print(f'** Sum of the rolls:{sum(self.rand_rolls): >5}\n')
            except ValueError:
                print('Please, enter a valid number.')


# Main function
if __name__ == '__main__':
    dice_simulator: DiceSimulator = DiceSimulator()
    dice_simulator.roll()
