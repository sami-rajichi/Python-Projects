import collections

print("*** Welcome to the code breakers app ***\n")
letters = list(map(chr , range(97 , 123)))
text_1 = '''To Sherlock Holmes she is always the woman. I have seldom heard him mention her under any other name. 
In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any emotion akin to love for Irene Adler. 
All emotions, and that one particularly, were abhorrent to his cold, precise but admirably balanced mind. 
He was, I take it, the most perfect reasoning and observing machine that the world has seen, but as a lover he would have placed himself in a false position. He never spoke of the softer passions, 
save with a gibe and a sneer. They were admirable things for the observer excellent for drawing the veil from men's motives and actions. 
But for the trained reasoner to admit such intrusions into his own delicate and finely adjusted temperament was to introduce a distracting factor which might throw a doubt upon all his mental results. 
Grit in a sensitive instrument, or a crack in one of his own highpower lenses, would not be more disturbing than a strong emotion in a nature such as his. 
And yet there was but one woman to him, and that woman was the late Irene Adler, of dubious and questionable memory. 
I had seen little of Holmes lately. My marriage had drifted us away from each other. My own complete happiness, and the homecentred interests which rise up around the man who first finds himself master of his own establishment, were sufficient to absorb all my attention, while Holmes, who loathed every form of society with his whole Bohemian soul, remained in our lodgings in Baker Street, buried among his old books, and alternating from week to week between cocaine and ambition, 
the drowsiness of the drug, and the fierce energy of his own keen nature. He was still, as ever, deeply attracted by the study of crime, and occupied his immense faculties and extraordinary powers of observation in following out those clues, and clearing up those mysteries which had been abandoned as hopeless by the official police. From time to time I heard some vague account of his doings: of his summons to Odessa in the case of the Trepoff murder, of his clearing up of the singular tragedy of the Atkinson brothers at Trincomalee, and finally of the mission which he had accomplished so delicately and successfully for the reigning family of Holland. 
Beyond these signs of his activity, however, which I merely shared with all the readers of the daily press, I knew little of my former friend and companion. zzz'''.lower()

for letter in text_1:
    if letter not in letters:
        text_1 = text_1.replace(letter , '')
letters_count = collections.Counter(text_1)
print("Her the frequency analysis from test 1 :\n")
print("\tLetters\t\tOccurrence\tPercentage")
for key , value in sorted(letters_count.items()):
    print("\t" + key + "\t\t\t" + str(value) + "\t\t\t" + str(round(value * 100 / len(text_1) , 2)) + "%")

orderedLetters1 = []
for pair in letters_count.most_common():
    orderedLetters1.append(pair[0])
print("\nLetters from highest to lowest :")
print(''.join(orderedLetters1) + "\n")

text_2 = '''Thanks to the field of linguistics we know much about the development of the 5,000 plus languages in existence today. We can describe their grammar and pronunciation and see how their spoken and written forms have changed over time. 
For example, we understand the origins of the Indo-European group of languages, which includes Norwegian, Hindi and English, and can trace them back to tribes in eastern Europe in about 3000 BC.
So, we have mapped out a great deal of the history of language, but there are still areas we know little about. 
Experts are beginning to look to the field of evolutionary biology to find out how the human species developed to be able to use language. So far, there are far more questions and half-theories than answers.
We know that human language is far more complex than that of even our nearest and most intelligent relatives like chimpanzees. We can express complex thoughts, convey subtle emotions and communicate about abstract concepts such as past and future. And we do this following a set of structural rules, known as grammar. 
Do only humans use an innate system of rules to govern the order of words? Perhaps not, as some research may suggest dolphins share this capability because they are able to recognise when these rules are broken.
If we want to know where our capability for complex language came from, we need to look at how our brains are different from other animals. This relates to more than just brain size; it is important what other things our brains can do and when and why they evolved that way. And for this there are very few physical clues; artefacts left by our ancestors don't tell us what speech they were capable of making. One thing we can see in the remains of early humans, however, is the development of the mouth, throat and tongue. By about 100,000 years ago, humans had evolved the ability to create complex sounds. 
Before that, evolutionary biologists can only guess whether or not early humans communicated using more basic sounds.'''.lower()

for letter in text_2:
    if letter not in letters:
        text_2 = text_2.replace(letter , '')
letters_count2 = collections.Counter(text_2)
print("Her the frequency analysis from test 2 :\n")
print("\tLetters\t\tOccurrence\tPercentage")
for key , value in sorted(letters_count2.items()):
    print("\t" + key + "\t\t\t" + str(value) + "\t\t\t" + str(round(value * 100 / len(text_2) , 2)) + "%")

orderedLetters2 = []
for pair in letters_count2.most_common():
    orderedLetters2.append(pair[0])
print("\nLetters from highest to lowest :")
print(''.join(orderedLetters2) + "\n")

chosen_option = input("Would you like to encode or decode a message : ").lower().strip()
while chosen_option != "encode" and chosen_option != "decode":
    print("Your answer should be either 'encode' or 'decode'.. Please write your option likewise i did.")
    chosen_option = input("Would you like to encode or decode a message : ").lower().strip()

message = input("Enter the message please : ").lower()
for letter in message:
    if letter not in letters:
        message = message.replace(letter , '')

if chosen_option == "encode":
    print("\nThe encoded message is :")
    for letter in message:
        print(orderedLetters2[orderedLetters1.index(letter)] , end='')
else:
    print("\nThe decoded message is :")
    for letter in message:
        print(orderedLetters1[orderedLetters2.index(letter)], end='')