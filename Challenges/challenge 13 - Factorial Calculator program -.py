import math

print("Welcome to the factorial program.\n")
factNb = int(input("What number would you like to compute the factorial of : "))

print(str(factNb)+"! = ", end='')
for i in range(factNb):
    print(str(i+1)+"*", end="")
print(factNb)

print("\nHere is the result from the math library : ")
print("The factorial of",factNb,"is",math.factorial(factNb))

print("\nHere is the result from my own algorithm : ")
f = 1
for i in range(factNb):
    f *= (i+1)
print("The factorial of",factNb,"is",f)

print("\nIt's shown twice that "+str(factNb)+"! =",f)