fileName = input(">>> Enter the file name : ")

try:
    fileHandle = open(fileName)
except:
    print("Cannot find the file !")
    quit()

adresses = dict()
for line in fileHandle:
    if not line.startswith("From "):
        continue
    words = line.rstrip().split()
    adresses[words[1]] = adresses.get(words[1], 0) + 1

mostOccurredAdresse = None
nbOfTime = None
for key, value in adresses.items():
    if nbOfTime == None or value > nbOfTime:
        mostOccurredAdresse = key
        nbOfTime = value

print(mostOccurredAdresse, nbOfTime)
