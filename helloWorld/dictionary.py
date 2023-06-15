thisIsDict = {
    "language": "Python",
    "creator": "Guido Van Rossum",
    "year": "1991"
}

print(thisIsDict)
print(thisIsDict["language"])
print(thisIsDict.get("creator"))
thisIsDict["language"] = "PYTHON" # here i just changed the value of language's key from Python to PYTHON
print(thisIsDict)
thisIsDict["website"] = "www.python.org" # this statement is meant to add a new item to dictionary
print(thisIsDict)
thisIsDict.pop("website")
print(thisIsDict)

for x in thisIsDict :
    print(x)

for x in thisIsDict.values() :
    print(x)

for x,y in thisIsDict.items() :
    print(x , y)