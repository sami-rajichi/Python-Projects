"""
Created on Sun Jun 18 19:57:30 2023

@author: Sami RAJICHI
"""

import os
import re
import random


class MadLibs:

    # Define the pattern for extracting the words description
    pattern: str = r"\{([\w'.]+)\}"
    # Define the directory path where stories exist
    path: str = './Templates'

    # Initiate the class
    def __init__(self, story_template: str):
        self.story_template = story_template

    @classmethod
    def random_template(cls) -> str:
        # Get existing files
        files_name: list[str] = os.listdir(cls.path)
        # Return random file name
        return random.choice(files_name)

    # Define a function called "get_template" to retrieve a template
    def get_template(self) -> str:
        # Fetch the template path using the "os" module
        fpath: str = os.path.join(self.path, self.story_template)
        # Include an exception to return error if the file doesn't exist or reading issue
        try:
            # Open and read file
            with open(fpath, 'r') as f:
                content: str = f.read()
                return content
        except:
            # Return error
            return 'Error: can\'t find file or read data'

    # Define a function called "get_words_description" to extract words descriptions
    def get_words_description(self, content: str) -> list[str]:
        # Find and extract the words wrapped in curly brackets
        matches: list[str] = re.findall(self.pattern, content)
        return matches

    # Define a function called "template_preprocessing" to keep only the brackets
    def template_preprocessing(self, content: str) -> str:
        # Remove the word and keep the brackets
        return re.sub(self.pattern, "{}", content)

    # Define a function called "start_mad_lib" to start the game
    @classmethod
    def start_mad_lib(cls, content: str, words_desc: list[str]) -> str:
        # Create a variable to store user inputs
        user_words: list[str] = []
        print(f'Please provide the following {len(words_desc)} words:\n')
        # Append all the user inputs into the variable in a capitalized format
        for ind, word in enumerate(words_desc, start=1):
            user_words.append(
                input(str(ind) + '- ' + word.capitalize() + ': '))
        return content.format(*user_words)


# Main function
if __name__ == '__main__':
    file_name: str = MadLibs.random_template()
    print(file_name)
    mad_lib: MadLibs = MadLibs(file_name)
    content: str = mad_lib.get_template()
    words_description: list[str] = mad_lib.get_words_description(content)
    cleaned_content: str = mad_lib.template_preprocessing(content)
    print(MadLibs.start_mad_lib(cleaned_content, words_description))
