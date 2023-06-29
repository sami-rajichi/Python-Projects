"""
Created on Tue Jun 27 23:35:00 2023

@author: Sami RAJICHI

@project: HangMan
"""

from random import choice


class HangMan:

    def __init__(self):
        """
        This method meant to initialize fetch the words 
        from a text file and initialize the class attributes.
        """
        # Initialize attributes
        self.reset()

    def reset(self):
        """
        This method meant to initialize all class attributes.
        """
        # Retrieve all the words from wordlist file
        with open('./wordlist.txt', 'r') as f:
            self.words: list[str] = f.read().split()
            self.word: str = choice(self.words).upper()
        self.tries: int = 6
        self.guessed_letters: list[str] = []
        self.guessed: bool = False
        self.word_completion: str = '-' * len(self.word)

    def check_letter_guess(self, guess: str, word: str):
        """
        This method is executed when the user guess a letter.
        It consists of 2 tests (conditions):
            - When the letter doesn't exist in the secret word.
            - When the letter correctly guessed.
        """
        if guess not in word:
            # Decrement the number of tries and add the letter to the guessed letters list
            # So that the user get noticed to not type it again.
            self.tries -= 1
            self.guessed_letters.append(guess)
        # When the letter correctly guessed.
        else:
            # Add the letter to the list
            self.guessed_letters.append(guess)
            # Get the indices of the appropriate letters in the word
            indices: list[int] = [
                i for i, letter in enumerate(word) if letter == guess]
            # Replace the '-' that corresponds of the positions of the letter(s)
            word_list: list[str] = list(self.word_completion)
            for index in indices:
                word_list[index] = guess
            self.word_completion = ''.join(word_list)
            # If no '-' found, the guessed flag is being switched to True.
            # As a result, the game ends
            if '-' not in self.word_completion:
                self.guessed = True

    def start_game(self, user_guess: str):
        """
        This method represents the starting point of the game.
        """
        # This evaluates if the length of the input is equal to 1
        # and make sure it's alphabetic
        if len(user_guess) == 1 and user_guess.isalpha():
            # Call the check_letter_guess method
            self.check_letter_guess(user_guess, self.word)
        else:
            print('Not a valid guess.')
        # self.reset()
