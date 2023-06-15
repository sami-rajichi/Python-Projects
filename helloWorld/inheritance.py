class person:
    def __init__(e, fname, lname, age):
        e.fname = fname
        e.lname = lname
        e.age = age
    def printName(e2):
        print(e2.fname, e2.lname, e2.age)
class student(person):
    pass
obj = student("Sami", "RAJICHI", 19)
obj.printName()

class Professor(person):
    def __init__(e, fname, lname, age, CIN):
        person.__init__(e, fname, lname, age)
        e.CIN = CIN
    def printNameP(e2):
        print(e2.fname, e2.lname, e2.age, e2.CIN)
obj2 = Professor("Sami", "RAJICHI", 19, 14606156)
obj2.printNameP()