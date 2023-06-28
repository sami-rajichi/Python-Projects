"""
Created on Tue Jun 27 23:35:00 2023

@author: Sami RAJICHI

@project: HangMan
"""

from pygame_setup import PygameSetup
from random import choice


class HangMan:

    def __init__(self):
        """
        This method meant to initialize the game with a custom title, fetch the words 
        from a text file and initialize the class attributes.
        """
        welcome: str = 'Welcome To HangMan Game'
        print(f'{welcome:-^40}')

        # Initialize attributes
        self.__reset()

    def __reset(self):
        """
        This method meant to initialize all class attributes.
        """
        # Retrieve all the words from wordlist file
        with open('./wordlist.txt', 'r') as f:
            self.__words: list[str] = f.read().split()
            self.__word: str = choice(self.__words).upper()
        self.tries: int = 6
        self.__guessed_letters: list[str] = []
        self.__guessed_words: list[str] = []
        self.__guessed: bool = False
        self.__word_completion: str = '-' * len(self.__word)

    def __check_letter_guess(self, guess: str, word: str):
        """
        This method is executed when the user guess a letter.
        It consists of 3 tests (conditions):
            - When the letter had been already guessed.
            - When the letter doesn't exist in the secret word.
            - When the letter correctly guessed.
        """
        # When the letter had been already guessed.
        if guess in self.__guessed_letters:
            print('You have already guessed that letter. Choose again.')
        # When the letter doesn't exist in the secret word.
        elif guess not in word:
            print(f'{guess} not in the word.')
            # Decrement the number of tries and add the letter to the guessed letters list
            # So that the user get noticed to not type it again.
            self.tries -= 1
            self.__guessed_letters.append(guess)
        # When the letter correctly guessed.
        else:
            # Add the letter to the list
            self.__guessed_letters.append(guess)
            # Get the indices of the appropriate letters in the word
            indices: list[int] = [
                i for i, letter in enumerate(word) if letter == guess]
            # Replace the '-' that corresponds of the positions of the letter(s)
            word_list: list[str] = list(self.__word_completion)
            for index in indices:
                word_list[index] = guess
            self.__word_completion = ''.join(word_list)
            # If no '-' found, the guessed flag is being switched to True.
            # As a result, the game ends
            if '-' not in self.__word_completion:
                self.__guessed = True

    def __check_word_guess(self, word: str, right_word: str):
        """
        This method is executed when the user guesses a word.
        It consists of 3 tests (conditions):
            - When the word had been already guessed and not the right one.
            - When the word is not equal to the right secret word.
            - When the word correctly guessed.
        """
        # When the word had been already guessed and not the right one.
        if word in self.__guessed_words:
            print('You have already guessed that word. Think again.')
        # When the word is not equal to the right secret word.
        elif word not in right_word:
            print('This is not the correct word.')
            # Decrement the number of tries and add the letter to the guessed words list
            # So that the user get noticed to not type it again.
            self.tries -= 1
            self.__guessed_words.append(word)
        # When the word correctly guessed.
        else:
            # If no '-' found, the guessed flag is being switched to True.
            # As a result, the game ends
            self.__guessed = True
            self.__word_completion = right_word

    def __user_guides(self):
        """
        This method shows some guidelines to the user like the stages and word completion state.
        """
        print(self.__word_completion)
        if len(self.__guessed_letters) > 0:
            print('* Used Letters: ', end='')
            print(*self.__guessed_letters, sep='-')
        if len(self.__guessed_words) > 0:
            print('* Used Words: ', end='')
            print(*self.__guessed_words, sep='-')
        print('\n')

    def start_game(self):
        """
        This method represents the starting point of the game.
        """
        # Call the guidelines
        self.__user_guides()
        # Loop till the guessing evaluated to True or the number of attempts increased to 0.
        while not self.__guessed and self.tries > 0:
            # Take the user input and make it in uppercase
            user_guess = input('Guess a letter or word: ').upper()
            # This evaluates if the length of the input is equal to 1
            # and make sure it's alphabetic
            if len(user_guess) == 1 and user_guess.isalpha():
                # Call the check_letter_guess method
                self.__check_letter_guess(user_guess, self.__word)
            # This evaluates if the length of the guessed word is equal to the right word
            # and make sure it's alphabetic as well
            elif len(user_guess) == len(self.__word) and user_guess.isalpha():
                # Call the check_word_guess method
                self.__check_word_guess(user_guess, self.__word)
            else:
                print('Not a valid guess.')
            self.__user_guides()
        if self.__guessed:
            print(f'\nYes! The secret word is {self.__word}. You won !!\n')
        else:
            print(
                f'Sorry, you ran out of tries. The word was {self.__word}. Maybe next time!\n')
        # Call the reset method to initialize attributes
        self.__reset()


if __name__ == '__main__':
    hangman: HangMan = HangMan()
    pygame_setup: PygameSetup = PygameSetup()
    pygame_setup.run(hangman.tries)
