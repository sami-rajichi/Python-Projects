thisIsTuple = ("A", "B", "C", "D") # tuples are different to lists because they're immutable (can't be changed)

print(thisIsTuple)
print(thisIsTuple[0])

for x in thisIsTuple :
    print(x)

thisIsSet = {"A", "B", "C", "D"} # sets are like lists but they differ in one thing which is they are unordered

print(thisIsSet) # y can only print all set's elements together but you can't print an element

for x in thisIsSet :
    print(x)

thisIsSet.add("E")
thisIsSet.update(["F", "G", "H"])
thisIsSet.remove("E")
thisIsSet.discard("F")
thisIsSet.pop()
print(thisIsSet)