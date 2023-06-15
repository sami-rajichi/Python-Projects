fname = input('>>> Enter the name of the file : ')

try:
    file = open(fname)
except:
    print("Can't find the file!")
    quit()

li = list()
for f in file:
    if f.startswith('From '):
        words = f.rstrip().split()
        print(words[1])
        li.append(words[1])

print('There were %d lines in the file with From as the first word' % len(li))
