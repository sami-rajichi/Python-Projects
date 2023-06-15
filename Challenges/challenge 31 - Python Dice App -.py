import  random

print("*** Welcome to the python dice app ***\n")

while True:
    def dice_sides():
        return int(input("How many sides would you like on your dice : "))
    sides = dice_sides()
    def dices():
        return int(input("How many dices would you like to roll : "))
    nbOfDices = dices()
    print("\nYou rolled", nbOfDices, sides, "sided dice.")

    def appending_value(nd , s):
        array = []
        for i in range(nd):
            x = random.randint(1, s)
            array.append(x)
        return array
    valueOfRolledDice = appending_value(nbOfDices , sides)
    def results(array):
        print("\n---------- Results are as followed ----------")
        for value in array:
            print("\t" + str(value))

    results(valueOfRolledDice)

    def sumOfValues(valueOfRolledDice):
        s = 0
        for value in valueOfRolledDice:
            s += value
        return s
    print("The total value of your roll is " + str(sumOfValues(valueOfRolledDice)))
    def answer():
        return input("\nWould you like to roll again (y/n) : ").lower().strip()
    rep = answer()
    if rep.startswith('n'):
        print("\nThanks for using Python Dice App.")
        break