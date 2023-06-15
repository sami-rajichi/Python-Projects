def first_function():
    print("helloWorld!")

first_function()

def second_function(name):
    print("Hello " + name)

second_function("Python")

def rectangle_area(height , width):
    return height*width

print(rectangle_area(7 , 20) , "cm")

def lists(t):
    for x in t:
        print("Bonjour " + x)

t = ["Sami", "Wael", "Bilel", "Wissem"]

lists(t)