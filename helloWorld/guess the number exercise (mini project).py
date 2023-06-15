import random

min = 0
max = 1999

randNb = random.randint(min , max)
print(randNb)

playerGuess = int(input("Give your guess :  "))

while playerGuess < 0 or playerGuess > 1999 :
    playerGuess = int(input("Give your guess :  "))

i = 1
while playerGuess != randNb and i <= 6 :
    print("Wrong guess!")
    i += 1
    if playerGuess > randNb :
        print("Hint: go lower")
    else:
        print("Hint: go higher")
    playerGuess = int(input("Give your guess again:  "))
if i > 6 :
    print("too bad, you lost")
else:
    print("Congratulations, you guessed it right")