fname = input('>>> Enter the name of the file : ')

try:
    file = open(fname)
except:
    print("Can't find the file!")
    quit()

li = list()
for f in file:
    lineList = f.rstrip().split()
    #print(lineList)
    for word in lineList:
        if word in li:
            continue
        li.append(word)
li.sort()
print(li)
