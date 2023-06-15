print("*** Welcome to the python calculator app ***\n")

def first_number():
    return float(input("Enter your first number : "))

def second_number():
    return float(input("Enter your second number : "))

def desired_operation():
    return input("Enter your desired operation (addition (a), subtraction (s), multiplication (m), division (d), or exponentiation (e)) : ").lower().strip()

def add(x , y):
    return x + y

def subtract(x , y):
    return x - y

def divide(x , y):
    if y == 0:
        print("\nYou cannot divide by zero.")
        return "DIV ERROR"
    else:
        print("\nThe quotient of " + str(x) + " and " + str(y) + " is " + str(x / y))
        return str(fn) + " / " + str(sn) + " = " + str(x / y)

def multiply(x , y):
    return x * y

def exponent(x , y):
    return x ** y

history = []
while True:
    fn = first_number()
    sn = second_number()
    do = desired_operation()

    if do == 'mutiplication' or do == 'm':
        history.append(str(fn) + " * " + str(sn) + " = " + str(multiply(fn , sn)))
        print("\nThe product of " + str(fn) + " and " + str(sn) + " is " + str(multiply(fn , sn)))
    elif do == 'divisin' or do == 'd':
        history.append(divide(fn , sn))
    elif do == 'addition' or do == 'a':
        history.append(str(fn) + " + " + str(sn) + " = " + str(add(fn , sn)))
        print("\nThe sum of " + str(fn) + " and " + str(sn) + " is " + str(add(fn , sn)))
    elif do == 'subtraction' or do == 's':
        history.append(str(fn) + " - " + str(sn) + " = " + str(subtract(fn , sn)))
        print("\nThe difference of " + str(fn) + " and " + str(sn) + " is " + str(subtract(fn , sn)))
    elif do == 'exponentiation' or do == 'e':
        history.append(str(fn) + " ** " + str(sn) + " = " + str(exponent(fn , sn)))
        print("\nThe result of " + str(fn) + " raised to the " + str(sn) + " power is " + str(exponent(fn , sn)))
    else:
        history.append("OPR ERROR")
        print("\nThis is not a valid operation .. Try again.")

    rep = input("\nWould you like to run the program again (y/n) :").lower().strip()
    while True:
        if rep.startswith('n') == False and rep.startswith('y') == False:
            rep = input("\nWould you like to run the program again (y/n) :").lower().strip()
        else:
            break
    if rep.startswith('n'):
        print("\n---------- Calculation Synopsis ----------")
        for i in history:
            print(i)
        print("\nThanks for using python calculator app.. Goodbye.")
        break