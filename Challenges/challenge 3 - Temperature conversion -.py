name = input("Enter your name : ").title().strip()
print("Hello, " + name)

print("this simple application was made to convert a Temperature in Fahrenheit to Celsius or Kelvin\n")

F = float(input("Enter a Temperature degree in Fahrenheit : "))
C = round((F - 32) * 5/9, 4)
K = round((F - 32) * 5/9 + 273.15, 4)

print("Degrees Fahrenheit:\t\t" + str(F))
print("Degrees Celsius:\t\t" + str(C))
print("Degrees Kelvin:\t\t\t" + str(K))