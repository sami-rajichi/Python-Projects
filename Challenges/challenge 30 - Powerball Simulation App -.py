import random

print("----------------------- Power-Ball Simulator -----------------------\n")

white_balls = int(input("How many white-balls would you like to draw for the 5 winning numbers (normally 69): "))
while white_balls < 5 or white_balls > 69:
    white_balls = int(input("How many white-balls would you like to draw for the 5 winning numbers (normally 69): "))

red_balls = int(input("How many red-balls would you like to draw for the Power-Ball (normally 26): "))
while red_balls < 1 or red_balls > 26:
    red_balls = int(input("How many red-balls would you like to draw for the Power-Ball (normally 26): "))

m = 1
for i in range(5):
    m *= (white_balls - i)
print("You have a 1 of " + str(m * red_balls / 120) + " chance of winning this lottery.")
purchasing_tickets = int(input("Purchase tickets in what interval : "))

print("\n----------------------- Welcome to the Power-Ball -----------------------\n")

winningNumbers = []
for i in range(4):
    number = random.randint(1, white_balls)
    while number in winningNumbers:
        number = random.randint(1 , white_balls)
    winningNumbers.append(number)
winningNumbers.sort()
winningNumbers.append(random.randint(1 , red_balls))
print("Tonight's winning numbers are : " , end='')
for number in winningNumbers:
    print(str(number) + " " , end="")

print()
input("Press ENTER to start purchasing tickets!!!")

nbOfDrewTickets = 0
tickets = 0
listOfPurchasedTickets = []

while True:
    nbOfDrewTickets += 1
    tickets += 1
    ticket = []
    for i in range(4):
        number = random.randint(1, white_balls)
        while number in ticket:
            number = random.randint(1, white_balls)
        ticket.append(number)
    ticket.sort()
    ticket.append(random.randint(1, red_balls))
    if ticket in listOfPurchasedTickets:
        print("Losing ticket generated; disregard..")
        print(ticket)
    else:
        listOfPurchasedTickets.append(ticket)
        print(ticket)
    if ticket == winningNumbers:
        print("\nWinning ticket numbers : ", end='')
        for number in ticket:
            print(str(number) + " ", end="")
        print()
        print("You purchased a total " + str(nbOfDrewTickets) + " tickets.")
        break
    if tickets >= purchasing_tickets:
        tickets = 0
        print(nbOfDrewTickets , "tickets purchased so far with no winners..")
        rep = input("\nKeep purchasing tickets (y/n) ? ").lower().strip()
        if rep.startswith('n'):
            print("\nYou bought " + str(nbOfDrewTickets) + " and still lost!!")
            print("Better luck next time.")
            break