import random
class hangman:
    def __init__(self):
        self.words = []
        self.word = ""
        self.word_dash = ""
    def readWords(self, filename):
        file = open(filename)
        for line in file:
            line = line.strip("\n")
            self.words.append(line)
        file.close()
    def chooseWord(self):
        min = 0
        max = len(self.words) - 1
        self.word = self.words[random.randint(min, max)]
        self.word_dash = "_" * len(self.word)
    def checkGuess(self, char):
        i = 0
        for x in range(len(self.word)):
            if char == self.word[x]:
                i += 1
        if i != 0:
            return True
        else:
            return False
    def replace(self, char):
        for x in range(len(self.word)):
            if char == self.word[x]:
                self.word_dash = self.word_dash[0:x] + char + self.word_dash[x+1:]
    def checkGuessedWord(self):
        if "_" not in self.word_dash:
            return True
        else:
            return False
    def printGussedWord(self):
        print(self.word_dash)