nom = "SamiRajichi"

for i in nom :
    print(i)

t = ["A" , "B" , "C" , "D" , "E"]

for i in t :
    print(i)

for i in range(3 , len(t)) :
    print(t[i])

for i in range(0 , len(t) , 2) :  # we could consider the third parameter of range as number of steps
    print(t[i])