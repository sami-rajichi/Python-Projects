import random

print("Welcome to the guess my number app.\n")
name = input("What's your name : ").title().strip()

print("Well " + name + ", i'm thinking of a number between 1 and 20.\n")

ranNum = random.randint(1 , 20)

for i in range(1 , 6):
    guessed_number = int(input("Take a guess : "))
    if guessed_number < ranNum:
        print("Your guess is too low.")
    elif guessed_number > ranNum:
        print("Your guess is too high.")
    else:
        break
if guessed_number == ranNum:
    print("\nGood job " + name + ", you guessed my number in " + str(i) + " guesses.")
else:
    print("O loss " + name + ", you loose all the tries you need. By the way the number i was thinking of was " + str(ranNum))