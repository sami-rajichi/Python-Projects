import random

print("*** Welcome to thesaurus app ***\n")

print("Choose a word from the thesaurus and I will give you a synonym.\n")

thesaurus_word = {
    "hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
}

print("here are the words in the thesaurus :")
for word in thesaurus_word.keys():
    print("\t\t " + word)

chosed_word = input("\nWhat word would you like a synonym for : ").lower().strip()
if chosed_word in thesaurus_word.keys():
    ranNum = random.randint(0 , 4)
    print("The synonym for " + chosed_word + " is : " + (thesaurus_word[chosed_word][ranNum]))
else:
    print("I'm sorry.. that word is not currently in the thesaurus.\n")

rep = input("Would you like to see the whole thesaurus (y/n) : \n").lower().strip()
if rep.startswith('y'):
    for key in thesaurus_word.keys():
        print(key.title() , "synonyms are :")
        for value in thesaurus_word[key]:
            print("\t- " + value)
        print("\n")
else:
    print("I hope you enjoyed the program.. Goodbye!")