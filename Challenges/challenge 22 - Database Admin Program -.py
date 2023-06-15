print("*** Welcome to the database admin program ***\n")

log_on_information = {
    "admin" : "admin0000",
    "sam20" : "20sami20",
    "dogba3" : "12345678910",
}

username = input("Enter your username : ").lower().strip()
if username not in log_on_information.keys():
    print("Username not in database..")
    rep = input("Would you like to sign up to this database (y/n) : ").lower().strip()
    if rep.startswith('y'):
        password = input("Enter your password : ").strip()
        b = True
        numbers = list(map(str , range(0 , 10)))
        while b:
            if (' ' in password) or (password[0] in numbers) or (len(password) < 8):
                print("Invalid password : Your password either contains a blank space or starts with a number or doesn't contain at least 8 characters!")
                password = input("Please re-nter your password : ").strip()
                b = True
            else:
                b = False
        log_on_information[username] = password

        print("\nWe are pleased to meet you " + username + ", Thanks for trusting us!")
    else:
        print("\nYou are welcomed anytime.. Goodbye.")
else:
    password = input("Enter your password : ").strip()
    if password != log_on_information[username]:
        print("Password incorrect!")
    else:
        print("\nHello " + username + ".. You are logged in!\n")
        if username == "admin":
            print("Here are all users database :")
            for user , passwrd in log_on_information.items():
                print("Username : " + user + "\t\tPassword : " + passwrd)
        else:
            rep = input("Would you like to change your password (y/n) : ").lower().strip()
            if rep.startswith('y'):
                password = input("Enter your password : ").strip()
                b = True
                numbers = list(map(str, range(0, 10)))
                while b:
                    if (' ' in password) or (password[0] in numbers) or (len(password) < 8):
                        print("Invalid password : Your password either contains a blank space or starts with a number or doesn't contain at least 8 characters!")
                        password = input("Please re-nter your password : ").strip()
                        b = True
                    else:
                        b = False
                log_on_information[username] = password

                print(username + ", your new password is " + password)