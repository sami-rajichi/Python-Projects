import random

print("*** Welcome to the guess the word app ***\n")

categories = {
    "films" : ["science" , "adventure" , "mystery" , "action" , "documentary" , "thriller" , "animation"],
    "furniture" : ["chair" , "table" , "desk" , "lamp" , "cushion" , "rug" , "stove"],
    "fruits" : ["banana" , "apple" , "strawberry" , "plum" , "pineapple" , "date" , "pear"],
    "sports" : ["football" , "basketball" , "baseball" , "gymnastics" , "volleyball" , "golf" , "skiing"],
    "classes" : ['english', 'history', 'science', 'mathematics', 'art', 'health'],
    "colors" : ['orange', 'yellow', 'purple', 'aquamarine', 'violet', 'gold' , "black"],
}

keys = []
values = []
for key , value in categories.items():
    keys.append(key)
    values.append(value)

while True:
    ranKey = random.randint(0 , len(keys) -1)
    ranValue = random.randint(0 , len(values[ranKey]) -1)
    print("Guess a " + str(len(categories[keys[ranKey]][ranValue])) + " letter word from the following the category : " + keys[ranKey])
    dash_word = len(categories[keys[ranKey]][ranValue]) * '-'
    print(dash_word)
    guesses = 0
    attempts = 5
    while attempts > 0:
        guessed_word = input("\nEnter a guess :").lower().strip()
        guesses += 1
        computerGuessedWord = categories[keys[ranKey]][ranValue]
        if guessed_word == categories[keys[ranKey]][ranValue]:
            print("Correct!! you guessed the word in " + str(guesses) + " guesses.")
            break
        else:
            attempts -= 1
            print("Sorry, this is not the correct guess .. Hence, in this case, only " + str(attempts) + " attempts remain for you.")
            for i in range(len(guessed_word)):
                if computerGuessedWord[i] == guessed_word[i]:
                    dash_word = dash_word[0:i] + computerGuessedWord[i] + dash_word[i+1:]
            if attempts <= 2:
                print("Because we don't want you to lose, we'll be helping you through revealing a letter in each remaining attempt.")
                ranNum = random.randint(0 , len(computerGuessedWord) - 1)
                while dash_word[ranNum] != '-':
                    ranNum = random.randint(0, len(computerGuessedWord) - 1)
                dash_word = dash_word[0:ranNum] + computerGuessedWord[ranNum] + dash_word[ranNum + 1:]
            print(dash_word)
    rep = input("\nWould you like to run the game again (y/n) : ").lower().strip()
    if rep.startswith('n'):
        print("\nWe hope you enjoyed the game .. We look forward to playing it again.")
        break