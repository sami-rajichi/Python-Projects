from hangMan import hangman

hangman = hangman()
hangman.readWords("hangManWords.txt")
hangman.chooseWord()

fails = 0

while fails <= 5:
    print(hangman.printGussedWord())
    char = input("Enter a character :  ")
    if hangman.checkGuess(char):
        print("correct guess")
        hangman.replace(char)
    else:
        print("wrong guess")
        fails += 1
    if hangman.checkGuessedWord():
        print("bravo, you have found the word")
        hangman.printGussedWord()
        break
    print("attempts left : " + str(fails))
else:
    print("unfortunately, you failed")