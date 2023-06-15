fileName = input('>>> Enter file name :')
try:
    file = open(fileName)
except:
    print("%s doesn't exist in the folder.\n" % fileName)
    quit()
line = 0
average = 0
for l in file:
    if l.startswith("X-DSPAM-Confidence"):
        line +=1
        average += float(l[l.find(':')+2 : ])
print("Average spam confidence:", average / line)
