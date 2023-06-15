print("*** Welcome to the factor generator app ***\n")

while True:
    entered_number = int(input("Enter a number to determine all its factors : "))

    factorsList = []

    for factor in range(1 , entered_number + 1):
        if entered_number % factor == 0:
            factorsList.append(factor)

    print("\nFactors", entered_number, "are :")
    for factor in factorsList:
        print("\t" + str(factor))

    print("\nIn summary :")
    for factor in range((len(factorsList) // 2)):
        print(str(factorsList[factor]) + " * " + str(factorsList[len(factorsList) - factor - 1] ) + " = " + str(factorsList[factor] * factorsList[len(factorsList) - factor -1]))

    rep = input("\nRun again (y/n) : ").lower().strip()
    if rep.startswith('n'):
        print("\nThanks for using factor generator app.. Have a great day!\n")
        break