import random

min = 1
max = 6

nbOfDices = int(input("How many dices you want?  "))

test = "y"

while test == "y" :
    for i in range(nbOfDices) :
        print(random.randint(min , max))
    test = input("Do you want to continue the game?  ")
