import collections

print("*** Welcome to the frequency analysis app ***\n")

letters = list(map(chr , range(97 , 123)))
nbOfPhrases = int(input("How many phrases would you like to be analyzed : "))

for nb in range(nbOfPhrases):
    phrase = input("Enter a word or a phrase to count the occurrence of each letter : ").lower().strip()
    for letter in phrase:
        if letter not in letters:
           phrase = phrase.replace(letter , '')
    letter_count = collections.Counter(phrase)
    print("\nHere's the Frequency Analysis from phrase " + str(nb + 1) + " : \n")
    print("\t\t Letter\t\tOccurrence\t Percentage")
    for i in sorted(letter_count.most_common()):
        print("\t\t " + str(i[0]) + "\t\t\t" + str(i[1]) + "\t\t\t " + str(round((i[1] * 100) / sum(letter_count.values()) , 2)) + '%')
    print("\nLetters ordered from highest to lowest :")
    for letter in letter_count.most_common():
        print(letter[0] , end='')
    print("\n")