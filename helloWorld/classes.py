class language :
    def __init__(e, name, creator, year, extension):
        e.name = name
        e.creator = creator
        e.year = year
        e.extension = extension

    def firstFunction(e2):
        print(e2.name + " was realized in " + e2.year + " by " + e2.creator)

obj = language("Python", "Guido Van Rossum", "1991", ".py")
obj.firstFunction()
print(obj.name)
print(obj.creator)
print(obj.year)
obj.name = "PYHON"  # this statement will change the value of name property from Python to PYTHON
print(obj.name)

del obj.extension  # this statement will delete a property of the object which is extension
print(obj.extension)

del obj  # this statement will delete the entire object
print(obj.name)