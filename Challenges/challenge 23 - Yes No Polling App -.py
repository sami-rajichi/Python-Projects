print("*** Welcome to the yes no polling app ***\n")
issue = input("What's the yes or no issue that you will be voting on : ")
nbOfVoters = int(input("How many voters you will allow to vote on the issue : "))
password = input("Enter an admin password for polling results : ")
b = True
while b:
    if (' ' in password) or (password[0] in list(map(str, range(0 , 10)))):
        print("Invalid password : Your password either contains a blank space or starts with a number!")
        password = input("Enter a password for polling results : ")
        b = True
    else:
        b = False

yes_answer = 0
no_answer = 0
votersAnswers = {}
for voter in range(nbOfVoters):
    user_full_name = input("\nEnter your full name : ").title().strip()
    if user_full_name in votersAnswers.keys():
        print("Sorry, it seems that someone with that name has already voted.")
    else:
        print("Here's your issue : " + issue)
        rep = input("What do you think.. yes or no : ").lower().strip()
        if rep.startswith('y'):
            votersAnswers[user_full_name] = 'yes'
            yes_answer += 1
        elif rep.startswith('n'):
            votersAnswers[user_full_name] = 'no'
            no_answer += 1
        else:
            print("This is not a yes or no answer, but okay..")
            votersAnswers[user_full_name] = rep
        print("Thank you " + user_full_name + ", your vote of " + votersAnswers[user_full_name] + " has been recorded.")

print("\nThe following " , len(votersAnswers) , "perons voted :")
for voter in votersAnswers.keys():
    print("\t- " + voter)

print("\nOn the following issue : " + issue)
if yes_answer > no_answer:
    print("Yes wins " + str(yes_answer) + " to " + str(no_answer) + " vote.")
elif no_answer > yes_answer:
    print("No wins " + str(no_answer) + " to " + str(yes_answer) + " vote.")
else:
    print("It a tie! " + str(yes_answer) + " votes to " + str(no_answer) + ".")

admin_password = input("To see the voting results, enter the admin password : ").strip()
if admin_password == password:
    for voter , vote in votersAnswers.items():
        print("Voter : " + voter + "\t\tVote : " + vote)
else:
    print("Sorry, that's not the correct password.. Goodbye.")

print("\nThanks for using Yes or No issue polling app!")