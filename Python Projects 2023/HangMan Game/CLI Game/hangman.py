# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 21:06:34 2023

@author: Sami RAJICHI
"""

from random import choice


class HangMan:

    # def __new__(cls):
    #     with open('./wordlist.txt', 'r') as f:
    #         cls.__words: list[str] = f.read().split()
    #         cls.__word: str = choice(cls.__words).upper()

    def __init__(self):
        welcome: str = 'Welcome To HangMan Game'
        print(f'{welcome:-^40}')
        with open('./wordlist.txt', 'r') as f:
            self.__words: list[str] = f.read().split()
            self.__word: str = choice(self.__words).upper()
        self.__word_completion: str = '-' * len(self.__word)
        self.__tries: int = 6
        self.__guessed_letters: list[str] = []
        self.__guessed_words: list[str] = []
        self.__guessed: bool = False

    def __check_letter_guess(self, guess: str, word: str):
        if guess in self.__guessed_letters:
            print('You have already guessed that letter. Choose again.')
        elif guess not in word:
            print(f'{guess} not in the word.')
            self.__tries -= 1
            self.__guessed_letters.append(guess)
        else:
            self.__guessed_letters.append(guess)
            indices: list[int] = [
                i for i, letter in enumerate(word) if letter == guess]
            word_list: list[str] = list(self.__word_completion)
            for index in indices:
                word_list[index] = guess
            self.__word_completion = ''.join(word_list)
            if '-' not in self.__word_completion:
                self.__guessed = True

    def __check_word_guess(self, word: str, right_word: str):
        if word in self.__guessed_words:
            print('You have already guessed that word. Think again.')
        elif word not in right_word:
            print('This is not the correct word.')
            self.__tries -= 1
            self.__guessed_words.append(word)
        else:
            self.__guessed = True
            self.__word_completion = right_word

    def __display_hangman(self, tries: int):
        stages = [  # final state: head, torso, both arms, and both legs
            """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
            # head, torso, both arms, and one leg
            """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
            # head, torso, and both arms
            """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
            # head, torso, and one arm
            """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
            # head and torso
            """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
            # head
            """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
            # initial empty state
            """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
        ]
        return stages[tries]

    def __user_guides(self):
        print(self.__display_hangman(self.__tries))
        print(self.__word_completion)
        print('\n')

    def start_game(self):
        self.__user_guides()
        while not self.__guessed and self.__tries > 0:
            user_guess = input('Guess a letter or word: ').upper()
            if len(user_guess) == 1 and user_guess.isalpha():
                self.__check_letter_guess(user_guess, self.__word)
            elif len(user_guess) == len(self.__word) and user_guess.isalpha():
                self.__check_word_guess(user_guess, self.__word)
            else:
                print('Not a valid guess.')
            self.__user_guides()
        if self.__guessed:
            print(f'\nYes! The secret word is {self.__word}. You won !!')
        else:
            print(
                f'Sorry, you ran out of tries. The word was {self.__word}. Maybe next time!')


# Main function
if __name__ == '__main__':
    hangman: HangMan = HangMan()
    hangman.start_game()
    while input('Do you want to play again (Y/N)? ').upper() == 'Y':
        hangman.start_game()
