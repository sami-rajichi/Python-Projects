import time

print("*** Welcome to the prime number app ***\n")

while True:
    print("Enter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all the prime numbers within a set range.")
    choice = input("Enter your choice 1 or 2 : ")
    while choice != '1' and choice != '2':
        choice = input("Enter your choice 1 or 2 : ")

    if choice == '2':
        lowerBound = int(input("Enter the lower bound of your range : "))
        upperBound = int(input("Enter the upper bound of your range : "))
        start_time = time.time()
        prime_numbers = []
        for element in range(lowerBound , upperBound + 1):
            if element <= 1:
                continue
            else:
                prime_status = True
                for element2 in range(2 , element):
                    if element % element2 == 0:
                        prime_status = False
                        break
                if prime_status == True:
                    prime_numbers.append(element)
        end_time = time.time()
        #time.sleep(end_time - start_time)
        print("\nCalculation took a total of " + str(round(end_time - start_time , 4)) + " seconds.")
        print("The following numbers between " + str(lowerBound) + " and " + str(upperBound) + " are prime :")
        input("Click enter to see them out")
        for number in prime_numbers:
            print("\t" + str(number))
    else:
        entered_number = int(input("Enter a number to determine if it's prime or not : "))
        prime_status = True
        for number in range(2 , entered_number):
            if entered_number % number == 0:
                prime_status = False
                break
        if entered_number == 1 or prime_status == False:
            print(entered_number , "is not prime!")
        else:
            print(entered_number , "is prime!")
    rep = input("\nWould you like to run the game again (y/n) : ").lower().strip()
    if rep.startswith('n'):
        print("\nThanks for using prime number app.. Have a nice day!")
        break
    print("\n")
