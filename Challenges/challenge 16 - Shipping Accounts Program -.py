print("Welcome to the shipping accounts program.\n")

usrNames = ['SamR' , 'Na_wel' , 'SamiraBz' , 'Nejib_Rajichi']

getUsrName = input("Hello, What is your username : ")

if getUsrName not in usrNames:
    print("Oh sorry, you don't have an account with us.")
    rep = input("Would you like to have a shipping account (Y/N) ?  ").upper()
    if rep == 'N':
        print("What a pity!! :( , if you changed your opinion you'd have been welcomed anytime. Goodbye")
    else:
        print("we're pleased to have you in our family " + getUsrName +". Now, you are able to login anytime you want.")
        usrNames.append(getUsrName)
else:
    print("\nHello " + getUsrName + ", welcome back to your account.")
    print("Current shipping prices are as follows : \n")
    print("\tShipping orders from 0 to 100 : \t$5.10 each item")
    print("\tShipping orders from 100 to 500 : \t$5.00 each item")
    print("\tShipping orders from 500 to 1000 : \t$4.95 each item")
    print("\tShipping orders over 1000 : \t\t$4.80 each item")

    nbItems = int(input("\nHow many items would you like to ship : "))
    if nbItems >= 0 and nbItems <= 100:
        print("In order to ship " + str(nbItems) + " items you need to cost " + str(nbItems * 5.10) + " at $5.10 per item.")
    elif nbItems > 100 and nbItems <= 500:
        print("In order to ship " + str(nbItems) + " items you need to cost " + str(nbItems * 5.00) + " at $5.00 per item.")
    elif nbItems > 500 and nbItems <= 1000:
        print("In order to ship " + str(nbItems) + " items you need to cost " + str(nbItems * 4.95) + " at $4.95 per item.")
    else:
        print("In order to ship " + str(nbItems) + " items you need to cost " + str(nbItems * 4.80) + " at $4.80 per item.")

    rep = input("\nWould you like to place this order (Y/N) ? ").upper()
    if rep.startswith("N"):
        print("Okay, no order is being placed at this moment.")
    else:
        print("Okay, shipping " + str(nbItems) + " items.")