print("*** Welcome to the even odd number sorter app ***\n")

while True:

    numbers = input("Enter in a string of numbers separated with a coma (,) : ")

    for number in numbers:
        if number == ' ':
            numbers = numbers.replace(number , '')

    numbersList = numbers.split(',')

    print("\n---- RESULT SUMMARY ----")
    odd = []
    even = []
    for number in numbersList:
        if int(number) % 2 == 0:
            print("\t" + number + " is even")
            even.append(int(number))
        else:
            print("\t" + number + " is odd")
            odd.append(int(number))

    print("\nThe following " + str(len(even)) + " numbers are even :")
    for e in sorted(even):
        print("\t" + str(e))

    print("\nThe following " + str(len(odd)) + " numbers are odd :")
    for o in sorted(odd):
        print("\t" + str(o))

    rep = input("Would you like to run out the program again (y/n) : ").lower().strip()
    if rep.startswith("n"):
        print("\nThanks for using the program.. Goodbye.")
        break