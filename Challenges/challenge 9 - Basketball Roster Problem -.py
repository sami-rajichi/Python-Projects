import random
import datetime

print("Welcome to baseball roster program ")
time = datetime.datetime.now()
print("The current date and time is "+time.strftime("%d/%m/%Y  %H:%M:%S")+"\n")

nbPosition = int(input("Enter the number of positions of your team, Coach :"))
roster = {}
for i in range(0,nbPosition):
    playerPosition = input("Enter a position :").title().strip()
    ppName = input("Enter a player's name for this position :").title().strip()
    roster[playerPosition] = ppName
position = []
pn = []
for x in roster:
    position.append(x)
for x in roster.values():
    pn.append(x)

print("\n")
print("\t\tYour starting",nbPosition,"of the upcoming basketball season :")
for x,y in roster.items():
    print("\t\t\t\t"+x+" :\t\t"+y)

ranNum = random.randint(0,nbPosition-1)

print("\nOh no,",pn[ranNum],"is injured")
print("your roster only has",len(roster)-1)
replace_player = input("Who will take "+pn[ranNum]+"'s spot :").title().strip()
roster[position[ranNum]] = replace_player

print("\n\t\tYour starting",nbPosition,"of the upcoming basketball season :")
for x,y in roster.items():
    print("\t\t\t\t"+x+" :\t\t"+y)
print("\nGood luck "+replace_player+" you will do great")
print("your roster has "+str(len(roster))+" players")