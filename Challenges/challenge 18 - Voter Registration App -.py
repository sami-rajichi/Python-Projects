print("Welcome to the voter registration app.\n")

name = input("Please enter your name : ").title().strip()
age = int(input("Please enter your age : "))

political_parties = ["Republican" , "Democratic" , "Independent" , "Libertarian" , "Green"]

if age < 18:
    print("\nYou are not old enough to register and vote.")
else:
    print("\nCongratulations " + name + ", You are old enough to register and vote.")
    print("\nHere is the list of political parties to join :")
    for party in political_parties:
        print("\t\t- " + party)
    party = input("\nWhat partie would you like to join : ").title().strip()
    if party in political_parties:
        print("\nCongratulations " + name + ", You have just joined the " + party + " party.")
        if party == "Republican" or party == "Democratic":
            print("That is a major party.")
        elif party == "Independent":
            print("You are an independent person.")
        else:
            print("That is not a major party.")
    else:
        print("\nSorry the " + party + " party didn't run for the election this season.")