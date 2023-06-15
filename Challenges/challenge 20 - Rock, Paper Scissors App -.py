import random

print("Welcome to a game of Rock, Paper, Scissors.\n")

nbOfRounds = int(input("How many rounds would you like to play : "))

computer = 0
player = 0
rps = ["rock" , "paper" , "scissors"]

for i in range(nbOfRounds):
    print("\nRound : " + str(i + 1))
    print("Player :", player, "\t\tComputer", computer)
    player_choice = input("Time to pick...rock, paper, scissors : ").lower().strip()
    if player_choice not in rps:
        print("This is not a valid game option!")
        print("Computer gets the point!")
        computer += 1
    else:
        ranNum = random.randint(0, 2)
        print("\t\tComputer : " + rps[ranNum])
        print("\t\tPlayer : " + player_choice)
        if player_choice == rps[ranNum]:
            print("\t\tThis is a tie ... How boring!")
            print("\t\tThis round was a tie!")
        elif player_choice == "rock" and rps[ranNum] == "paper":
            print("\t\tPaper Covers rock!")
            print("\t\tComputer wins round : " + str(i + 1))
            computer += 1
        elif player_choice == "rock" and rps[ranNum] == "scissors":
            print("\t\tRock breaks scissors!")
            print("\t\tYou win round : " + str(i + 1))
            player += 1
        elif player_choice == "paper" and rps[ranNum] == "rock":
            print("\t\tPaper smashes rock!")
            print("\t\tYou win round : " + str(i + 1))
            player += 1
        elif player_choice == "paper" and rps[ranNum] == "scissors":
            print("\t\tScissors cuts paper!")
            print("\t\tComputer wins round : " + str(i + 1))
            computer += 1
        elif player_choice == "scissors" and rps[ranNum] == "rock":
            print("\t\tRock defeats scissors!")
            print("\t\tComputer wins round : " + str(i + 1))
            computer += 1
        elif player_choice == "scissors" and rps[ranNum] == "paper":
            print("\t\tScissors cuts paper!")
            print("\t\tYou win round : " + str(i + 1))
            player += 1

print("\nFinal game results :\n")
print("\t\tRounds played :", nbOfRounds)
print("\t\tComputer score :", computer)
print("\t\tPlayer score :", player)
if player > computer:
    print("\t\tWinner : PLAYER!!!")
elif computer > player:
    print("\t\tWinner : COMPUTER :(")
else:
    print("\t\tNo winner .. The game ended up with a tie!")