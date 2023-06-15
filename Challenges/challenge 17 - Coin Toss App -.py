import random

print("Welcome to the coin toss app.\n")

print("I will flip you a coin a set number of times.")
nbFlips = int(input("How many times would you like me to flip the coin : "))
rep = input("Would you like to see out the result of each individual flip (y/n) ? ").lower().strip()

print("\nFLIPPING!!!!\n")

heads = 0
tails = 0

for i in range(1 , nbFlips + 1):
    numRan = random.randint(0, 1)
    if numRan == 0:
        heads += 1
    else:
        tails += 1
    if rep.startswith('n'):
        if heads == tails:
            print("At",i,"times, the number of heads and tails were equal at",heads,"each")
    else:
        if numRan == 0:
            print("HEADS")
        else:
            print("TAILS")
        if heads == tails:
            print("At",i,"times, the number of heads and tails were equal at",heads,"each")

print("\nresults of FLIPPING a coin " + str(nbFlips) + " Times : \n")
print("Side\t\t\tCount\t\t\tPercentage")
print("HEADS\t\t\t" + str(heads) + "/" + str(nbFlips) + "\t\t\t" + str(round((heads * 100) / nbFlips , 2)))
print("TAILS\t\t\t" + str(tails) + "/" + str(nbFlips) + "\t\t\t" + str(round((tails * 100) / nbFlips , 2)))