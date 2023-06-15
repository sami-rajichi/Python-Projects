fileName = input('>>> Enter file name : ')

try:
    fileHandle = open(fileName)
except:
    print('Cannot find out the file !')
    quit()

hours = dict()
for line in fileHandle:
    if not line.startswith('From '): continue
    words = line.rstrip().split()
    date = words[len(words) - 2].split(':')
    hours[date[0]] = hours.get(date[0], 0) + 1

for k, v in sorted(hours.items()): print(k, v)
