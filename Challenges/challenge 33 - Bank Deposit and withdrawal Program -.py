print("*** Welcome to the python first national bank ***\n")

def get_info():
    info_dict = {}
    info_dict['name'] = input("Hello, what's your name : ").title().strip()
    info_dict['savings'] = int(input("How much money would you like to set up your savings account with : "))
    info_dict['checking'] = int(input("How much money would you like to set up your checking account with : "))
    return info_dict

def display_info(dict):
    print("\nCurrent account informations :")
    print("Name : " + dict['name'])
    print("Savings : $" + str(dict['savings']))
    print("Checking : $" + str(dict['checking']))

def make_deposit(dict , option , money):
    dict[option] += money
    print("\nDeposited $" + str(money) + " into " + dict['name'] + "'s " + option + " account.")

def make_withdrawal(dict , option , money):
    if dict[option] - money < 0:
        print("\nSorry, by withdrawing $" + str(money) + " you will have a negative balance.")
    else:
        dict[option] -= money
        print("\nWithdrew $" + str(money) + " from " + dict['name'] + "'s " + option + " account.")

user_info_account = {}
user_info_account = get_info()
while True:
    display_info(user_info_account)
    accessed_account = input("\nWhat account would you like to access (Savings or Checking) : ").lower().strip()
    transaction = input("What type of transaction would you like to make (Deposit or Withdrawal) : ").lower().strip()
    money = int(input("How much money : "))

    if accessed_account == "savings" or accessed_account == "checking":
        if transaction == "deposit":
            make_deposit(user_info_account , accessed_account , money)
        elif transaction == "withdrawal":
            make_withdrawal(user_info_account , accessed_account , money)
        else:
            print("\nI'm sorry, it seems you entered an unavailable option.")
    else:
        print("\nI'm sorry, it seems you entered an unavailable option.")

    rep = input("Would you like to make another transaction (y/n) : ").lower().strip()
    while rep.startswith('n') == False and rep.startswith('y') == False:
        rep = input("Would you like to make another transaction (y/n) : ").lower().strip()

    if rep.startswith('n'):
        break
print("\nThank you .. Have a great day!")