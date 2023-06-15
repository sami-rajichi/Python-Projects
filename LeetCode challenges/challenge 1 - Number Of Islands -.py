import random

gridOfChars = int(input("How many grid of chars do you need for counting : "))
lengthOfGrid = int(input("Enter the length of each grid : "))

charsTab = []
gridTab = []
for grid in range(gridOfChars):
    for char in range(lengthOfGrid):
        ranNum = random.randint(0 , 1)
        charsTab.append(str(ranNum))
        ch = ''.join(charsTab)
        charsTab = [