fileName = input('>>> Enter file name :')
try:
    file = open(fileName)
except:
    print("%s doesn't exist in your folder\n" % fileName)
for f in file:
    print(f.rstrip().upper())
