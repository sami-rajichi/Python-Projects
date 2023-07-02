"""
Created on Sun Jul  2 19:34:36 2023

@author: Sami RAJICHI

@project: Password Generator
"""

from re import search
import string
from secrets import randbelow


class PasswordGenerator:

    def __does_contain_uppercase(self, password: str) -> bool:
        return search('[A-Z]+', password) != None

    def __does_contain_symbols(self, password: str) -> bool:
        return True in list(map(lambda symbol: symbol in string.punctuation, password))

    def __compose_password(self, length_pass: int, combination: str) -> str:
        gen_pass: str = ''

        for i in range(length_pass):
            gen_pass += combination[randbelow(len(combination))]

        return gen_pass

    def generate(self, length_pass: int, has_uppers: bool, has_symbols: bool):
        combination: str = string.ascii_lowercase + string.digits
        gen_pass = self.__compose_password(length_pass, combination)

        if has_symbols:
            combination += string.punctuation
            while not self.__does_contain_symbols(gen_pass):
                gen_pass = self.__compose_password(length_pass, combination)
        if has_uppers:
            combination += string.ascii_uppercase
            while not self.__does_contain_uppercase(gen_pass):
                gen_pass = self.__compose_password(length_pass, combination)

        print(gen_pass)


if __name__ == '__main__':
    password_gen: PasswordGenerator = PasswordGenerator()
    password_gen.generate(length_pass=5, has_uppers=False, has_symbols=True)
