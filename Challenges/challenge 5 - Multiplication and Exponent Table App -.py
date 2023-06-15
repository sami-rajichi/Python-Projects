name = input("Enter your name : ").title().strip()
print("Hello " + name + ", Math is cool")

print("Welcome to multiplication and exponent table Application.")

number = float(input("Enter a number : "))

print("MULTIPLICATION TABLE FOR " + str(number) + " :\n")
for x in range(9):
    print(str(number) + " * " + str(x+1) + " = " + str(round(number * (x+1), 4)))

print("EXPONENT TABLE FOR " + str(number) + " :\n")
for x in range(9):
    print(str(number) + " ** " + str(x+1) + " = " + str(round(number ** (x+1), 4)))

print(name + ", math is awesome!")
print("\t" + name.lower() + ", math is awesome!".lower())
print("\t\t" + name.title() + ", math is awesome!".title())
print("\t\t\t" + name.upper() + ", math is awesome!".upper())